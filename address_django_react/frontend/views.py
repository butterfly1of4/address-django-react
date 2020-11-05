from django.shortcuts import render

# Create your views here.
#this function renderst the html page 
def index(request):
    return render(request, 'frontend/index.html')