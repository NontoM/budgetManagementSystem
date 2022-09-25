from django.shortcuts import render

# Create your views here.

def indexPageView(request):
    return render(request, '../templates/main_pages/index.html')

def deshboardView(request):
    return render(request, '../templates/main_pages/dashboard.html')

