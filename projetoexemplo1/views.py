from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello, world!')

def sobre(request):
    return HttpResponse('Sobre')

def autor(request):
    return HttpResponse('Autor')

def noticias(request):
    return HttpResponse('Noticias')

def empresa(request):
    return HttpResponse('Empresa')