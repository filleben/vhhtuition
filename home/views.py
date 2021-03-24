from django.shortcuts import render
from courses.models import Course


def home(request):
    courses = Course.objects.order_by('-course_views')[:3]

    context = {
        'courses': courses,
    }
    return render(request, 'home/index.html', context)


def privacy(request):
    return render(request, 'home/privacy_policy.html')


def cookie(request):
    return render(request, 'home/cookie_policy.html')
