from django.urls import path
from main_pages import views

urlpatterns = [
    path('',views.indexPageView, name='index'),
    path('dashboard/',views.deshboardView, name='dashboard'),

]
