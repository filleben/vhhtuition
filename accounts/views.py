from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from assessments.models import Assessment
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated')
        else:
            messages.error(request, 'Error updating profile, please check your'
                                    'form and try again.')
    else:
        form = UserProfileForm(instance=profile)

    assessments = Assessment.objects.filter(user=profile)

    context = {
        'profile': profile,
        'form': form,
        'assessments': assessments,
    }

    return render(request, 'accounts/profile.html', context)
