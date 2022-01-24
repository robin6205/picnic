from django.urls import path

from . import views

urlpatterns = [
    # ex: /stores/
    path('', views.home, name='home'),

    path('about/', views.about, name='about'),
    path('storepage/', views.storepage, name='storepage'),
    path('DamsoBBQ/', views.storepage, name='damso'),
    path('Lahaciente/', views.storepage, name ='Lahaciente'),
    path('Yatagrasu/', views.storepage, name ='Yatagrasu'),
    path('HappyChina/', views.storepage, name ='HappyChina'),
] 