from django.shortcuts import render


def display_courses(request):
    return render(request, 'courses/courses.html')
