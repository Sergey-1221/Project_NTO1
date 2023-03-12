from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from .models import Tour_order, Client
from tours_status.models import Payment
import htmlToPDF
from datetime import datetime
import json

# Create your views here.
def get_total_price(request, id_people):
	price = sum(Tour.total_price() for Tour in Tour_order.objects.filter(сlient=int(id_people)))
	json_data = {"id": price}
	json_data = json.dumps(json_data)
	return HttpResponse(json_data, content_type="application/json")

def get_profit(request):
	price = sum(Tour.total_price() for Tour in Tour_order.objects.filter(status='Завершен'))
	json_data = {"id": price}
	json_data = json.dumps(json_data)
	return HttpResponse(json_data, content_type="application/json")

def statement(request):
	name = {"name":"Иван"}
	return render(request, "Output.html", context=name)

