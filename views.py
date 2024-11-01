from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return HttpResponse("Hello, this is my Calculator app.")

def add_page(request):
    result = None
    if request.method == "POST":
        number1 = int(request.POST.get("number1", 0))
        number2 = int(request.POST.get("number2", 0))
        result = number1 + number2
    return render(request, 'add_page.html', {'result': result})

def subtract_page(request):
    result = None
    if request.method == "POST":
        number1 = int(request.POST.get("number1", 0))
        number2 = int(request.POST.get("number2", 0))
        result = number1 - number2
    return render(request, 'subtract_page.html', {'result': result})

def multiply_page(request):
    result = None
    if request.method == "POST":
        number1 = int(request.POST.get("number1", 0))
        number2 = int(request.POST.get("number2", 0))
        result = number1 * number2
    return render(request, 'multiply_page.html', {'result': result})

def divide_page(request):
    result = None
    if request.method == "POST":
        number1 = int(request.POST.get("number1", 0))
        number2 = int(request.POST.get("number2", 1))
        result = number1 / number2
    return render(request, 'divide_page.html', {'result': result})