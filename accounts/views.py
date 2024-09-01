from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'navin'})


def add(request):
    n1=int(request.POST['nums1'])
    n2=int(request.POST['nums2'])
    s=n1+n2
    return render(request,"result.html",{'res':s})