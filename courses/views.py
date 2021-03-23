from django.shortcuts import render
from .models import Course


def display_courses(request):
    courses = Course.objects.all().order_by('id')
    context = {
        'courses': courses,
    }
    return render(request, 'courses/courses.html', context)


def view_course(request, course_id):
    courses = Course.objects.filter(id=course_id)
    context = {
        'courses': courses,
    }
    return render(request, 'courses/view_courses.html', context)
