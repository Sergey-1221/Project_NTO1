from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.html import format_html

# Create your models here.
import uuid

def directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'images/{uuid.uuid4()}/{filename}'

class Manager(models.Model):
	class Meta:
		verbose_name = "Контактное лицо"
		verbose_name_plural = "Контактные лица"

	name = models.CharField(max_length=100, verbose_name='Фамилия Имя Отчество')
	phone = PhoneNumberField(null=True, blank=False, unique=True, verbose_name='Контактный номер')
	email = models.EmailField(max_length = 254, null=True, blank=False, verbose_name='E-mail')
	comment = models.TextField(max_length=500, null=True, blank=False, verbose_name='Комментарий')
	image = models.ImageField(upload_to=directory_path, null=True)

	def __str__(self):
		return self.name



class Hotel(models.Model):
	class Meta:
		verbose_name = "Отель"
		verbose_name_plural = "Отели"

	file = open(r'cities.txt', 'r', encoding='utf-8')
	text = file.readlines()
	file.close()
	cities = []
	for i in range(len(text)):
		if '\n' in text[i]:
			text[i] = text[i][:-1]
		cities.append((text[i], text[i]))
	cities = tuple(cities)

	name = models.CharField(max_length=200, verbose_name='Название отеля')
	manager = models.ForeignKey(Manager, on_delete=models.CASCADE, verbose_name='ФИО управляющего')
	phone = PhoneNumberField(null=False, blank=False, unique=True, verbose_name='Контактный номер')
	location = models.CharField(max_length=200, verbose_name='Местоположение', choices=cities)
	description = models.TextField(max_length=500, verbose_name='Описание отеля')

	def __str__(self):
		return self.name

class Tours(models.Model):
	class Meta:
		verbose_name = "Тур"
		verbose_name_plural = "Туры"

	FOOD_TYPE = [
		("0","Без питания"), 
		("1","С завтраком"), 
		("2","3-х разовое")
	]

	hotel = models.ForeignKey(Hotel, on_delete = models.CASCADE, verbose_name='Отель')
	date_of_stay = models.DateField(auto_now = False, auto_now_add = False, verbose_name='Дата заезда')
	date_of_exit = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Дата выезда')
	night = models.IntegerField(default=1, verbose_name='Ночи')
	food = models.CharField(max_length=200, verbose_name='Вид питания', choices=FOOD_TYPE)
	price = models.FloatField(verbose_name='Стоимость тура (Руб)')
	description = models.TextField(max_length=500, verbose_name='Описание тура')

	def days_nights(self):
		days = self.date_of_exit - self.date_of_stay
		nights = self.date_of_exit - self.date_of_stay
		return f"{days.days} \\ {nights.days-1}"

	days_nights.short_description = 'Дней \\ Ночей'

	def __str__(self):
		return self.description


class Client(models.Model):
	name = models.CharField(max_length=100, verbose_name='Клиент')
	contact_person = models.ForeignKey(Manager, on_delete=models.CASCADE, verbose_name='Контактное лицо')
	options = (('Физическое лицо','Физическое лицо'),
		('Юридическое лицо', 'Юридическое лицо'))
	option = models.CharField(max_length=100, verbose_name='Вид клиента', choices=options)

	def phone(self):
		return self.contact_person.phone
	phone.short_description = 'Телефон'

	class Meta:
		verbose_name = "Клиент"
		verbose_name_plural = "Клиенты"

	def __str__(self):
		return self.name

class Tour_order(models.Model):
	class Meta:
		verbose_name = "Заказ тура"
		verbose_name_plural = "Заказ тура"

	сlient = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
	payment_type = [
		("Предоплата","Предоплата"),
		("Кредит","Кредит")
	]
	payment = models.CharField(max_length=100, verbose_name='Вид оплаты', choices=payment_type)
	tour = models.ForeignKey(Tours, on_delete=models.CASCADE, verbose_name='Тур')
	price_tmp = models.FloatField(verbose_name='Цена')
	people = models.IntegerField(default=1, verbose_name='Количество человек')
	status_type = [
		("Отменен","Отменен"),
		("Действует","Действует"),
		("Завершен","Завершен"),
	]
	status = models.CharField(default="Действует",max_length=100, verbose_name='Cтатус', choices=status_type)

	def colored_status(self):
		if self.status == "Отменен":
			return format_html('<b style="color: #FF0000;"> {} </b>', self.status)
		elif self.status == "Действует":
			return format_html('<b style="color: #FFAA00;"> {} </b>', self.status)
		else:
			return format_html('<b style="color: #01A214;"> {} </b>', self.status)

	colored_status.short_description = 'Статус'

	"""
	def edit_status_completed(self):
		self.status = "Завершен"
	"""
	
	def total_price(self):
		return round(self.price_tmp*self.people,2)

	total_price.short_description = 'Стоимость'

	@staticmethod
	def autocomplete_search_fields():
		return 'сlient'

	def __str__(self):
		return f"{self.tour} | {self.сlient.contact_person}"
	