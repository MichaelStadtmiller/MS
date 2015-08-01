from django.shortcuts import render
# i think i can remove these - this was back when I could connect urls to views
#from django.http import HttpResponse
#from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return render(request, 'partysource/index.html')
