from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static


#domeny do glowej strony, one wchodza do views.py

urlpatterns = [
    path('', views.strona_startowa, name='startowa'),
    path('wykonywanie_cwiczen/', views.wykonywanie_cwiczen, name='wykonywanie_cwiczen'),
    path('protipy/', views.protipy, name='protipy'),

    
    path('login/', auth_views.LoginView.as_view(template_name='home/login.html'), name='login'), #logowanie
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),                            #wylogowywanie
    
    path('dodaj_do_planu/<int:exercise_id>/', views.dodaj_do_planu, name='dodaj_do_planu'),
    path('szczegoly_planu/<int:plan_id>/', views.szczegoly_planu, name='szczegoly_planu'),



    path('usun_z_planu/<int:exercise_id>/', views.usun_z_planu, name='usun_z_planu'),
    path('lista_planow/', views.lista_planow, name='lista_planow'),
    path('stworz_plan/', views.stworz_plan, name='stworz_plan'),

    path("usun_plan/<int:plan_id>/", views.usun_plan, name="usun_plan"),

    path('progress/', views.progress, name='progress'),
  #  path('zapisz_trening/<int:exercise_id>/', views.zapisz_trening, name='zapisz_trening'),

    path("plan/<int:plan_id>/", views.szczegoly_planu, name="szczegoly_planu"),

    path("dodaj-trening/", views.szczegoly_planu, name="szczegoly_planu"),
    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  #jezeli ktos odwiedzi strone to musi doprowadzic gdzie znadjuja sie filmy (jezeli ktos szuka media czyli filmow szuka to w media.root w tym komputerze)
