from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_expense, name='submit_expense'),
    path('submit/expense/', views.submit_expense, name='submit_expense'),
    path('submit/income/', views.submit_income, name='submit_income'),
#   path('expense/', views.submit_expense),
    ]   
