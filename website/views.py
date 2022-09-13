from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from website.forms import ContactForm, NewsLetterForm

def home(request):
    return render(request, 'website/index.html', )


def elements(request):
    return render(request, 'website/elements.html', )


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'your contact submitted successfully')
        else:
            messages.add_message(request, messages.ERROR, 'contact submission has been failed')
    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})


def about(request):
    return render(request, 'website/about.html', )


def newsletter(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


