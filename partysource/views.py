from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import TemplateView, View
from .models import Bottle


def index(request):
    all_bottles = Bottle.objects.order_by('name')
    template = loader.get_template('partysource/index.html')
    context = RequestContext(request, {'all_bottles': all_bottles,},)
    return HttpResponse(template.render(context))


class BottleDetailsView(TemplateView):
    template_name = 'partysource/bottle_details.html'
    
    def get_context_data(self, **kwargs):
        context = super(BottleDetailsView, self).get_context_data(**kwargs)
        PSID = kwargs.get('PSID')
        context['bottle_details'] = self.get_bottle_details_context(PSID)
        return context

    def get_bottle_details_context(self, PSID):
        context = {}
        thisbottle = Bottle.objects.filter(PSID=PSID)
        context['items'] = thisbottle
        
        for b in thisbottle:
            UOM = b.UOM
            price = b.price
            size = b.size
            imgsrc = 'https://www.thepartysource.com/express/' + b.img

        conv_size = size
        if UOM == 'L':
            conv_size = conv_size*1000
        context['PPU'] = round(price*(750/conv_size),5)
        context['imgsrc'] = imgsrc

        # to add the calculated values, do I add them to the context['items'] = thisBottle
        # e.g. context['items'] = thisBottle + context['PPU'] + context['imgsrc']
        return context

