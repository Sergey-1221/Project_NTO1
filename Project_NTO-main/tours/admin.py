from django.contrib import admin

# Register your models here.
from .models import *
from jet.filters import RelatedFieldAjaxListFilter

"""
@admin.register(Tour_order) 
class Tour_orderAdmin(admin.ModelAdmin):
    list_display = ("сlient", "payment", "tour", "price_tmp","people", "total_price", "colored_status")
    list_filter = (
        ("сlient", RelatedFieldAjaxListFilter),
    )
    #exclude = ['status']

@admin.register(Client) 
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "contact_person", "phone", "option")

@admin.register(Tours)
class ToursAdmin(admin.ModelAdmin):
    list_display = ("hotel", "days_nights", "date_of_stay", "night", "date_of_exit", "food", "price", "description")
    fields = "hotel", ("date_of_stay", "date_of_exit"), "night", "food", "price", "description"

@admin.register(Hotel) 
class HotelAdmin(admin.ModelAdmin):
    list_display = ("name", "manager", "phone", "location", "description")


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "comment", "image")
"""