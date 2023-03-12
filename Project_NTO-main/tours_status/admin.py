from django.contrib import admin
from .models import *
from tours.models import Tours

from jet.filters import RelatedFieldAjaxListFilter
#from jet.filters import DateRangeFilter

# Register your models here.
'''
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("date", "tour_order", "price")

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ("date", "tour_order", "booking", "сlient", "payment_type", "price_tmp", "people", "price")
    """
    list_filter = (
        ('date', DateRangeFilter),
    )
    """

@admin.register(Stats)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = ("name", "order_count", "order", "sales_count", "sales")
'''