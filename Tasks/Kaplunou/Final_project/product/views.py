from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string

gear_dict = {
    'regulators' : '1',
    'suits' : '2',
    'BCD' : '3',
    'masks' : '4',
    'fins' : '5'
}

def get_gear(request, gear):
    description = gear_dict.get(gear, None)
    response = render_to_string('product/store_page.html')
    if description:    
        return HttpResponse(response)
    else:
        return HttpResponseNotFound(f"not found")

def index(request):
    response = render_to_string('product/start_page.html')    
    return HttpResponse(response)