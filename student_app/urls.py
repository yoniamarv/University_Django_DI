from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='students'),
    path('student/<int:student_id>', views.details, name='student'),
    ]