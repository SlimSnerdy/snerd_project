from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse
from django.views import generic

from .models import Game

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'games/index.html'
    context_object_name = 'game_list'

    def get_queryset(self):
        return Game.objects.order_by('title')
     
class DetailView(generic.DetailView):
    model = Game
    template_name = 'games/detail.html'