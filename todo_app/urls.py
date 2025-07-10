from django.urls import path
from . import views

urlpatterns = [
    path('<int:month>', views.activities2),
    path('<str:month>', views.activities),
    
] 