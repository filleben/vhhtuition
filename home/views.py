from django.shortcuts import render


def home(request):
    return render(request, 'home/index.html')


def privacy(request):
    return render(request, 'home/privacy_policy.html')


def cookie(request):
    return render(request, 'home/cookie_policy.html')
