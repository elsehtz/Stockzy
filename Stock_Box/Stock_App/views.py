from django.shortcuts import render
from django.http import HttpResponse
import csv
# Create your views here.

# PAGES
def home(request):
    #response = HttpResponse("Hello world, this is the home page")
    # pass the request, html file, and dicitonary holding any info, 
    # that can be accesed by calling the dictionaries index like,
    # for example, {{name}} (in html file) for a dict {'name':'Zak'}
    # passed as a third parameter  
    return render(request, 'home.html', {'name':'Zak'})

def settings(request):
    return HttpResponse("Settings WIP")

def sign_in(request):
    return HttpResponse("WIP")

def ayo_home(request):
    return render(request, 'web_practice_1.html')

def visual_examples(request):
    # Example graphs using MSFT df and a HTML/CSV header
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
    return response

# ACTIONS
def add(request):

    val_1 = request.POST['num_1']
    val_2 = request.POST['num_2']
    res = int(val_1) + int(val_2)
    return render(request, 'result.html', {'result':res})