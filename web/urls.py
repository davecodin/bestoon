from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit/expense/', views.submit_expense, name='submit_expense'),
    path('submit/income/', views.submit_income, name='submit_income'),
    path('q/generalstat/', views.generalstat, name='generalstat'),
    path('accounts/register/', views.register, name='register'),
   
    ]   
