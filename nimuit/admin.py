from django.contrib import admin
from .models import Expert, Project, Testimonial
# Register your models here.

class ExpertAdmin(admin.ModelAdmin):

    list_display = ['title', 'designation', 'image']
    search_fields = ['title']

admin.site.register(Expert, ExpertAdmin)

class ProjectAdmin(admin.ModelAdmin):

    list_display = ['title', 'image']

admin.site.register(Project, ProjectAdmin)

class TestimonialAdmin(admin.ModelAdmin):

    list_display = ['title', 'image']

admin.site.register(Testimonial, TestimonialAdmin)