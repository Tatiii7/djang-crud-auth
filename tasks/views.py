from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
## from django.http import HttpResponse -- para mostar algo en html-- return HttpResponse('Hello World')
# Create your views here.
def home (request):
    return render(request, 'home.html')

def signup (request):

    if request.method == 'GET':
         return render(request, 'signup.html', {
        'form': UserCreationForm
    })

    else :
        if request.POST['password1'] == request.POST['password2']:
            #Se crea este try para intentar manear un error y no se caiga toda la base de datos
            try:
                #Register user
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'] )
                user.save()
                return HttpResponse('User created successfully')
            except:
                return HttpResponse('Username already exists')
        return HttpResponse('Password do not match')
    
def signin (request):
    
    return render(request, 'signin.html')

def generos (request):
    
    return render(request, 'generos.html')

def recomendaciones (request):
    
    return render(request, 'recomendaciones.html')

def peliculasFavoritas(request):
    
    return render(request, 'peliculasFavoritas.html')