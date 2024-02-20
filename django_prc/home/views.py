from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# this comes from django template
def home(request):
    peoples = [
        {'name':'abhijeet', 'age':34},
        {'name':'jeet', 'age':46},
        {'name':'manish', 'age':54},
        {'name':'manjeet', 'age':14},
        {'name':'nikhil', 'age':24},
    ]

    
    return render(request , "public/index.html" ,context={'peoples' : peoples})


def about(request):
    return HttpResponse("this is about page")