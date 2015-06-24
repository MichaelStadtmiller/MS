from django.shortcuts import render
#from django.http import HttpResponse
#from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return render(request, 'partysource/index.html')
