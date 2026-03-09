from django.contrib import admin
from django.urls import path
from django.conf.urls import include

#tutaj znajduja sie nasze domeny wchodzace do urls wyzej
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('home.urls')),
]
#tutaj pozwoli nam znalesc gdzie sa zdjecia