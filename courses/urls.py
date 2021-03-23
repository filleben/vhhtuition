from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_courses, name='display_courses'),
    path('<int:course_id>/', views.view_course,
         name='view_course'),
]
