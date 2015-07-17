from django.contrib import admin
from .models import IceCream, IceCreamBrand

# Register your models here.


class FlavorInline(admin.TabularInline):
    model = IceCream

class IceCreamAdmin(admin.ModelAdmin):
    inlines = [FlavorInline]

admin.site.register(IceCream)
admin.site.register(IceCreamBrand, IceCreamAdmin)