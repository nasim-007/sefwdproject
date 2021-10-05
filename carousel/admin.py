from django.contrib import admin
from .models import Carusel


class CarouselAdmin(admin.ModelAdmin):

    list_display = ['title', 'image']
    search_fields = ['title']

admin.site.register(Carusel, CarouselAdmin)

