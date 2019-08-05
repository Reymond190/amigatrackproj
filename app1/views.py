from django.shortcuts import render
from django.http import  request

def home_page(request):
    return render(request,'file1.html')
