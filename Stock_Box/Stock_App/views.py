from django.shortcuts import render
from django.http import HttpResponse
from .models import ex_obj, stock_cls
import pandas as pd
import csv
# Create your views here.

# PAGES
def home(request):
    item_1 = ex_obj()
    item_2 = ex_obj()

    item_1.name = 'Zak'
    item_2.name = 'Ayo'

    ex_obj_list = [item_1, item_2]
    return render(request, 'home.html', {'ex_obj_list': ex_obj_list})

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

# ACTIONS
def add(request):

    val_1 = request.POST['num_1']
    val_2 = request.POST['num_2']
    res = int(val_1) + int(val_2)
    return render(request, 'result.html', {'result':res})

def get_Stock(request):
    aapl = stock_cls()
    aapl.name = 'AAPL'
    aapl.df = pd.DataFrame({'id': [1, 2, 3, 4],
                   'a': ['on', 'on', 'off', 'off'],
                   'b': ['on', 'off', 'on', 'off']})

    return render(request, 'result.html', {'result':aapl})