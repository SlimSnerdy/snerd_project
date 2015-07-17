from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse
from django.views import generic
# from django.views.generic import DetailView
from .models import Amiibo
# from .models import Amiibo, AmiiboSeries, AmiiboUniverse


# Create your views here.


class IndexView(generic.ListView):
    template_name = 'amiibo/index.html'
    context_object_name = 'amiibo_list'

    def get_queryset(self):
        return Amiibo.objects.order_by('name')
           
# class IndexView(generic.ListView):
    # template_name = 'amiibo/index.html'
    # context_object_name = 'amiibo_series_list'

    # def get_queryset(self):
        # return AmiiboSeries.objects.order_by('name')
    
    # def get_context_data(self, **kwargs):
        # context = super(IndexView, self).get_context_data(**kwargs)
        # context['amiibo_universe_list'] = AmiiboUniverse.objects.order_by('name')
        # return context
        
# class SeriesDetailView(generic.DetailView):
    # model = AmiiboSeries
    # template_name = 'amiibo/series_detail.html'
   
# class UniverseDetailView(generic.DetailView):
    # model = AmiiboUniverse
    # template_name = 'amiibo/universe_detail.html'
    
class DetailView(generic.DetailView):
    template_name = 'amiibo/detail.html'
    model = Amiibo