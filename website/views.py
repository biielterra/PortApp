from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'website/index.html')

def sobre(request):
    return render(request, 'website/sobre.html')