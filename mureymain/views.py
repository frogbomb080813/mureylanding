from re import template
from django.http import HttpResponse
from django.shortcuts import render

#Create your views here.
def contact_view(request):
    template_name = 'index.html'
    return render(request, template_name)

def card_view(request):
    template_name = 'card.html'
    return render(request, template_name)