from django.shortcuts import render
from django.http import HttpResponse
import csv
# Create your views here.


def home(request):
    #response = HttpResponse("Hello world, this is the home page")
    response = render(request, 'home.html')
    return response

def settings(request):
    return HttpResponse("Settings WIP")

def sign_in(request):
    return HttpResponse("WIP")

def visual_examples(request):
    # Example graphs using MSFT df and a HTML/CSV header
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
    return response