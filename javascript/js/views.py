from django.shortcuts import render

# Create your views.

def calculator(request):
    return render(request, 'js/calculator.html')
