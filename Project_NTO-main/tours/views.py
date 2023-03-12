from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from .models import Tour_order
from tours_status.models import Payment
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
  date = Payment.objects.all()[0].date
  
  date = date.strftime("%d.%m.%Y")
  date_now = datetime.now().strftime("%d.%m.%Y")
  json_data = {"id": price, "date": date+" - "+date_now}
  json_data = json.dumps(json_data)
  return HttpResponse(json_data, content_type="application/json")

