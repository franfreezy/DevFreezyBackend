from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse

# Create your views here.
def homepage(request):
    return HttpResponse("Dev Freezy Backend!")

def api_data(request):
    # Return some JSON data
    data = {
        "message": "Hello from Freezy Backend"
    }
    return JsonResponse(data)

from django_daraja.mpesa.core import MpesaClient

def index(request):
    cl = MpesaClient()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    phone_number = '0729634366'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://devfreezy.netlify.app'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)

def stk_push_callback(request):
        data = request.body
        
        return HttpResponse("STK Push in Django👋")