from django.contrib import admin
from .models import Amiibo, AmiiboUniverse, AmiiboSeries

# Register your models here.


class AmiiboInline(admin.TabularInline):
    model = Amiibo
    
class AmiiboAdmin(admin.ModelAdmin):
    inlines = [
        AmiiboInline,
   ]

admin.site.register(Amiibo)
admin.site.register(AmiiboUniverse, AmiiboAdmin)
admin.site.register(AmiiboSeries, AmiiboAdmin)