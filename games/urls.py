from django.urls import path

from games import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us/', views.AboutUs, name='about_us'),
    path('about-school/' , views.Aboutschool , name='about_school'),
    path('<slug:s>/' , views.GameDetail , name='game_details'),
]
