from django.http import HttpResponse
from .models import Exercise, TrainingPlan
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Workout, Exercise
from .models import TrainingPlan, Workout
from .models import TrainingPlan, Exercise, Workout
from .forms import WorkoutForm



TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

#tutaj przeszły nasze resposny
#render wchodzimy do tempaltes, wykorzystalem settingsy do znalezienia folderu templates w home
@login_required(login_url='login')
def wykonywanie_cwiczen(request):
    exercises = Exercise.objects.all()   #pobranie wszystkich obiektow z models.py 
    return render(request, 'home/wykonywanie_cwiczen.html', {'exercises': exercises})#renderowanie dancyh, tworzenie słownika, exercises bedzie jako lista cwiczen

def protipy(request):
    return render(request, 'home/protipy.html')

def strona_startowa(request):
    return render(request, 'home/startowa.html')

def wybor_planu_treningowego(request):
    return render(request, 'home/wybor_planu_treningowego.html')








# tutaj znajduja sie plany treningowe
@login_required
def lista_planow(request):
    plany = TrainingPlan.objects.filter(user=request.user)
    return render(request, "home/lista_planow.html", {"plany": plany})


@login_required
def stworz_plan(request):
    if request.method == "POST":
        nazwa_planu = request.POST.get("title")  #pobieranie nazwy w formularza
        if nazwa_planu:
            #tworzymy nowy plan treningowy dla użytkownika   z okreslonym ID
            TrainingPlan.objects.create(user=request.user, title=nazwa_planu)
            return redirect('lista_planow')  #przekierowanie na listę planów

    return render(request, 'home/stworz_plan.html')  #wyświetlenie formularza


@login_required
def usun_plan(request, plan_id):
    plan = get_object_or_404(TrainingPlan, id=plan_id, user=request.user)

    if request.method == "POST":
        plan.delete()  
        return redirect("lista_planow")

    return render(request, "home/lista_planow.html", {"plany": TrainingPlan.objects.filter(user=request.user)})


@login_required
def szczegoly_planu(request, plan_id):
    plan = get_object_or_404(TrainingPlan, id=plan_id, user=request.user)   

    if request.method == "POST":
        selected_exercises = request.POST.getlist("exercise")
        date = request.POST.get("date")
        time = request.POST.get("time")

        for exercise_id in selected_exercises:
            exercise = get_object_or_404(Exercise, id=exercise_id)
            sets = int(request.POST.get(f"sets_{exercise_id}", 1))  #int domsylnie chcemy mieć calkowite a nie STRING!!!

            for i in range(sets):
                reps = request.POST.get(f"reps_{exercise_id}_{i}", 0)
                weight = request.POST.get(f"weight_{exercise_id}_{i}", 0)

                if reps and weight:
                    Workout.objects.create(
                        user=request.user,
                        exercise_name=exercise.title,
                        weight_1=weight,
                        reps_1=reps,
                        custom_date=date,
                        custom_time=time,
                    )

        return redirect("szczegoly_planu", plan_id=plan.id)  

    return render(request, "home/szczegoly_planu.html", {"plan": plan})





#tworzenie planów treningowych TUTAJ!
@login_required
def dodaj_do_planu(request, exercise_id):
    exercise = get_object_or_404(Exercise, id=exercise_id)
    plan_id = request.POST.get('plan_id')  # Pobieramy ID wybranego planu

    training_plan = get_object_or_404(TrainingPlan, id=plan_id, user=request.user)
    training_plan.exercises.add(exercise)

    return redirect('lista_planow')



@login_required
def usun_z_planu(request, exercise_id):
    exercise = get_object_or_404(Exercise, id=exercise_id)
    plan_id = request.POST.get('plan_id')

    training_plan = get_object_or_404(TrainingPlan, id=plan_id, user=request.user)
    training_plan.exercises.remove(exercise)

    return redirect('lista_planow')













#progress

@login_required
def progress(request):
    #pobierz wszystkie zapisane treningi użytkownika, (order_by) posortuj je po dacie i godzinie    / - od największej do najmneijszej
    workouts = Workout.objects.filter(user=request.user).order_by('-custom_date', '-custom_time')

    #tu grupujemy treningi po dacie
    grouped_workouts = {}       #tworzenie słownika
    for workout in workouts:
        #jeśli data nie istnieje w słowniku, dodajemy ją z pustą listą    // tworzy to tylko jedna date
        if workout.custom_date not in grouped_workouts:
            grouped_workouts[workout.custom_date] = []          
        # Dodajemy ćwiczenie do odpowiedniej daty
        grouped_workouts[workout.custom_date].append(workout)   #dodajemy do listy caly obiekt 

    # Przekaż dane do szablonu
    return render(request, 'home/progress.html', {'grouped_workouts': grouped_workouts})
