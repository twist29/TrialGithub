'''
Created on 05/06/2018

@author: twist
'''
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
