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