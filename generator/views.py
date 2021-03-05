import random

from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def generator(request):
    characters = list('abcdefg')

    if request.GET.get('capital'):
        characters.extend(list('ABCDEFG'))

    if request.GET.get('number'):
        characters.extend(list('123456'))

    length = int(request.GET.get('length', default=3))

    thepassword = ''
    for i in range(0, length, 1):
        thepassword += random.choice(characters)

    return render(request, 'generator.html', {'password': thepassword})
