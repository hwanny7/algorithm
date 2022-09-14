from django.shortcuts import render, redirect
import random

# Create your views here.


def calculator(request, pk, pk1):
    if pk1 == 0:
        div = 0
        mul = 0
    else:
        div = pk / pk1
        mul = pk * pk1
    context = {'pk':pk, 'pk1':pk1, 'div':div, 'mul':mul}
    return render(request, 'articles/calculator.html', context)

