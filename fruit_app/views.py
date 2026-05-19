from django.shortcuts import render
from django.http import JsonResponse
from .dummy_data import FRUITS_LIST
# Create your views here.

def send_fruits(request):
    data = {
        'fruits': FRUITS_LIST
    }
    return JsonResponse(data)