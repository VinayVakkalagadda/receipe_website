from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    peoples={
        "name":"Vinay","age":34
    }
    return render(request ,"index.html",context={'peoples':peoples})

def success(request):
    print(10 * '*')
    return HttpResponse("<h1> Success Page</h1>")