from django.shortcuts import render
from django.http import HttpResponse
from .models import shop_item

# Create your views here.
def home(request):
    
    dest_1 = shop_item()
    dest_1.name = 'Zak'
    dynamic_dict = {
        'long_text' : """NOTE**: THIS IS JUST SAMPLE TEXT TO SHOW THAT THIS IS A DYNAMIC 
                    TEXT SECTION FOR WHATEVER USES YOU MAY HAVE ~ Zak \n\n
                    "Whatever may come, fast or progressive, forcefully or quietly, abrasive or other. 
                    Do not waiver, do not weaken, do not fall. Failure may feel like
                    the heaviest weight, but in reality, nothing is heavier than despair" """
    }             
    dynamic_dict[dest_1] = dest_1
 
    #return render(request, 'web_practice_1.html', dynamic_dict)
    return render(request, 'web_practice_1.html', {'dest_1':dest_1})

    # Custon function
