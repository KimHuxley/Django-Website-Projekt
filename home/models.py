from django.db import models
from django.contrib.auth.models import User


# twojrzenie modelu
##tutaj zaczałelm 1 czesc##!!!!!!!!!!!!!!

class Exercise(models.Model): #tworzymy obiekt o nazwie Excercise w bazie danych
    title = models.CharField(max_length=200, verbose_name="Nazwa ćwiczenia")  #dodajemy tytuł z ogarniczona liczą znakow
    description = models.TextField(verbose_name="Opis ćwiczenia")  #dodajemy opis z wieksza liczba znakow 
    video = models.FileField(upload_to='exercise_videos/', verbose_name="Film instruktażowy") #FF to przechowywania filmow, przechowywanie filmow

    def __str__(self):
        return self.title #nadanie stylistyczne tytułu / (bez obcjest (1))



class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workouts")
    exercise_name = models.CharField(max_length=100)
    weight_1 = models.FloatField()
    reps_1 = models.PositiveIntegerField()
    set_number = models.PositiveIntegerField(default=1)  
    date = models.DateTimeField(auto_now_add=True)
    custom_date = models.DateField(null=True, blank=True, verbose_name="Data wykonania")
    custom_time = models.TimeField(null=True, blank=True, verbose_name="Godzina wykonania")

    def __str__(self):
        return f"{self.exercise_name} - Seria {self.set_number} - {self.custom_date or self.date.date()}"






class TrainingPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="training_plans")  
    title = models.CharField(max_length=50, verbose_name="Nazwa planu")  
    exercises = models.ManyToManyField('Exercise', blank=True, related_name="training_plans")

    class Meta:   #dodatkowa opcja - sortowanie, unikalnosc 
        unique_together = ('user', 'title')  # unikalna nazwa dla uzytkownikak (uzytkownik nie moze miec takiej samej nazwy)

    def __str__(self):
        return f"{self.title} - {self.user.username}"

