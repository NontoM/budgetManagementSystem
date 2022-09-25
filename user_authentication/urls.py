from django.urls import path
from user_authentication import views

urlpatterns = [
    path('register/',views.user_registerView, name='register'),
    path('login/',views.user_loginView, name='login'),
    path('user_profile/',views.user_profileView, name='user_profile'),
    path('logout/', views.logout_View, name='logout'),
    path('add_budget/', views.add_budgetView, name='add_budget'),
    path('add_new_budget/', views.add_new_budgetView, name='add_new_budget'),
    path('spend/', views.spendView, name='spend'),
    path('save_expenses/', views.save_expensesView, name='save_expenses'),
    path('all_expenses/', views.all_expensesView, name='all_expenses'),


]