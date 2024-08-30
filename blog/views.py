from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def root(request):
    return render(request, template_name='blog/index.html')


def index(request):
    return render(request, template_name='blog/index.html')


def about(request):
    context = {
        'name': 'Дмитрий',
        'lastname': 'Горим',
        'email': 'd.gorin@mail.ru',
        'title': 'О сайте'
    }
    return render(request, template_name='blog/about.html', context=context)

def send_data(request):
    data = {'name': 'Elena', 'age': 36}
    return JsonResponse(data=data)