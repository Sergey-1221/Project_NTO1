from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.html import format_html

from tours.models import Tour_order, Tours
#from rangefilter.filter import DateRangeFilter as OriginalDateRangeFilter
# Create your models here.

class Payment(models.Model):
	class Meta:
		verbose_name = "Оплата тура"
		verbose_name_plural = "Оплаты туров"

	tour_order = models.OneToOneField(Tour_order, on_delete = models.CASCADE, primary_key = True, related_name="+", verbose_name='Заказ')
	def price(self):
		return self.tour_order.total_price()

	date = models.DateTimeField(auto_now=True, verbose_name='Дата')
	price.short_description = 'Стоимость'

	def __str__(self):
		return f"{self.tour_order}"


	"""
	def __str__(self):
		return self.name
	"""
class Sale(models.Model):
	class Meta:
		verbose_name = "Продажа тура"
		verbose_name_plural = "Продажи туров"

	tour_order = models.OneToOneField(Payment, on_delete = models.CASCADE, primary_key = True, related_name="+", verbose_name='Заказ')
	booking_type = [
		("Да","Да"),
		("Нет","Нет")
	]
	booking = models.CharField(max_length=100, verbose_name='Бронь номеров', choices=booking_type)

	date = models.DateTimeField(auto_now=True, verbose_name='Дата')

	@staticmethod
	def autocomplete_search_fields():
		return "date"

	def сlient(self):
		return self.tour_order.tour_order.сlient
	сlient.short_description = 'Клиент'

	def payment_type(self):
		return self.tour_order.tour_order.payment
	payment_type.short_description = 'Вид оплаты'

	def price_tmp(self):
		return self.tour_order.tour_order.price_tmp
	price_tmp.short_description = 'Цена'

	def people(self):
		return self.tour_order.tour_order.people
	people.short_description = 'Количество человек'

	def price(self):
		return self.tour_order.price()
	price.short_description = 'Стоимость'


	def save(self, *args, **kwargs):
		tour = Tour_order.objects.get(id=self.tour_order.tour_order.id)
		tour.status = "Завершен"
		tour.save()
		super(Sale, self).save(*args, **kwargs)

	def __str__(self):
		return f"{self.tour_order}"

class Stats(Tours):
	class Meta:
		proxy = True
		verbose_name = "Статистика"
		verbose_name_plural = "Статистика"

	def name(self):
		return self.description
	name.short_description = "Тур"

	def order_count(self):
		tour = Tour_order.objects.filter(tour=self)
		return len(tour)

	order_count.short_description = 'Заказано (Кол)'

	def order(self):
		tour = Tour_order.objects.filter(tour=self)
		return sum(x.total_price() for x in tour)

	order.short_description = 'Заказано (Руб)'

	def sales_count(self):
		tour = Sale.objects.filter(tour_order__tour_order__tour__id=self.id)
		#tour = Sale.objects.all()
		#print(tour[1].tour_order.tour_order.tour.id)
		return len(tour)

	sales_count.short_description = 'Продано (Кол)'

	def sales(self):
		tour = Sale.objects.filter(tour_order__tour_order__tour__id=self.id)
		#tour = Sale.objects.all()
		#print(tour[1].tour_order.tour_order.tour.id)
		return sum(x.price() for x in tour)

	sales.short_description = 'Продано (Руб)'

	@staticmethod
	def autocomplete_search_fields():
		return "date"
