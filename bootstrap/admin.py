from django.contrib import admin
from .models import Corousel
# Register your models here.

class CarouselAdmin(admin.ModelAdmin):

    list_display = ['title', 'image']
    search_fields = ['title']

admin.site.register(Corousel, CarouselAdmin)