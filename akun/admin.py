from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class MapelAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'bio', 'birth_date', 'location')