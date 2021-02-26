from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from .models import Contact
from .forms import ContactForm


def contact(request):
    """
    Checks contact form is valid then saves the form data
    """
    if request.method == 'POST':
        form_data = {
            'name': request.POST['name'],
            'contact_email': request.POST['contact_email'],
            'contact_phone': request.POST['contact_phone'],
            'subject': request.POST['subject'],
            'message': request.POST['message'],
        }

        contact_form = ContactForm(form_data)

        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.save()

            return redirect(reverse('contact_success',
                                    args=[contact.contact_number]))

        else:
            messages.error(request, "Sorry there was a problem, "
                           "please check the information you have provided")

    contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
    }

    return render(request, 'contact/contact.html', context)


def contact_success(request, contact_number):
    """
    Displays contact success page with a summary of contact info
    """
    contact = get_object_or_404(Contact, contact_number=contact_number)
    context = {
        'contact': contact,
    }
    return render(request, 'contact/contact_success.html', context)
