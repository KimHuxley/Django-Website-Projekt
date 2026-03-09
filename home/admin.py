from django.contrib import admin
from .models import Exercise

# Register your models here.
# home/admin.py


@admin.register(Exercise)   #rejestracja modelu excercise 
class ExerciseAdmin(admin.ModelAdmin):      #ułatwienie zarzadzanymi danymi
    list_display = ('title', 'description')   #wyswiatelnaie tytulu i opisu