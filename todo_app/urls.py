from django.urls import path
from . import views

urlpatterns = [
    path('', views.activity),
    path('<month>', views.render_html),   
    path('<int:month>', views.activities2),
    path('<str:month>', views.activities, name='monthly-activity'),
] 