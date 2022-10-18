from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
# from django.contrib.auth import login as mi_login
from django.contrib.auth import login
from accounts.forms import MiFormularioDeCreacion

def mi_login(request):
    
    if request.method =='POST':
        formulario=AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario=formulario.get_user()
            login(request,usuario)
            return redirect('index')
    else:
        formulario=AuthenticationForm()
        
    return render(request,'accounts/login.html',{'formulario':formulario})


def registrar(request):
    
    if request.method=='POST':
        formulario=MiFormularioDeCreacion(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
    else:
        formulario=MiFormularioDeCreacion()
    
    return render(request,'accounts/registrar.html',{'formulario':formulario})
