from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def sudokuboard(request):
    return render(request, 'sudokuboard.html', {'sudokuboard':sudokuboard})