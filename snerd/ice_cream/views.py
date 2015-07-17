from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse
from django.views import generic

from .models import IceCreamBrand

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'ice_cream/index.html'
    context_object_name = 'ice_cream_list'

    def get_queryset(self):
        return IceCreamBrand.objects.order_by('name')
     
class DetailView(generic.DetailView):
    model = IceCreamBrand
    template_name = 'ice_cream/detail.html'