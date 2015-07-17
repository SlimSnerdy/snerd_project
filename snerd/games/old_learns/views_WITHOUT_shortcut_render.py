from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Game

# Create your views here.

def index(request):
#   output = Game.objects.all()
#   return HttpResponse(Game.objects.get(pk=0))
    game_list = Game.objects.all()
    template = loader.get_template('games/index.html')
    context = RequestContext(request, {'game_list': game_list,})
    return HttpResponse(template.render(context))
    
def detail(request, game_id):
    return HttpResponse("You're looking at game %s." % game_id)