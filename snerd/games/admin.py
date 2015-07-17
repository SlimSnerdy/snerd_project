from django.contrib import admin
#from games.models import Game, GameCompany, GamePlatform
from .models import Game, GameCompany, GamePlatform

# Register your models here.


class PlatformInline(admin.TabularInline):
    model = Game.platform.through

class CompanyInline(admin.TabularInline):
    model = Game.company.through

class GamePlatformAdmin(admin.ModelAdmin):
    inlines = [
        PlatformInline,
    ]
    
class GameCompanyAdmin(admin.ModelAdmin):
    inlines = [
        CompanyInline,
    ]
    
class GameAdmin(admin.ModelAdmin):
    inlines = [
        CompanyInline,
        PlatformInline,
    ]
    exclude = ('company', 'platform',)
    list_display = ('title', 'release_date', 'rating', 'get_gamecompany', 
    'get_gameplatform')
    search_fields = ['title']
    
admin.site.register(Game, GameAdmin)
admin.site.register(GameCompany, GameCompanyAdmin)
admin.site.register(GamePlatform, GamePlatformAdmin)