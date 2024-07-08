from django.shortcuts import render


def home(request):
    # seu código aqui
    context = {}  # adicione seu contexto aqui
    return render(request, 'global/home.html', context)
