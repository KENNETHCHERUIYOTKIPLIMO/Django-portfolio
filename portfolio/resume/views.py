from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def languages(request):
    return render(request, 'languages.html')


def services(request):
    return render(request, 'services.html')


def contacts(request):
    return render(request, 'contacts.html')

