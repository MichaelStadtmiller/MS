# from django.shortcuts import render
# i think i can remove these - this was back when I could connect urls to views
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Bottle

# Create your views here.
#def index(request):
#    return render(request, 'partysource/index.html')

#this will overtake the entire /partysource/index.html page.
#instead of httpresponse, i need to pass output to the template.

def index(request):
    all_bottles = Bottle.objects.order_by('name')
    template = loader.get_template('partysource/index.html')
    context = RequestContext(request, {'all_bottles': all_bottles,})
    return HttpResponse(template.render(context))
