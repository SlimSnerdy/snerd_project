from django.shortcuts import get_object_or_404, render

from .models import Game

# Create your views here.

def index(request):
    game_list = Game.objects.order_by('title')
    context = {'game_list': game_list}
    return render(request, 'games/index.html', context)
    
def detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'games/detail.html', {'game': game})