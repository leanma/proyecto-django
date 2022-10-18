from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template,loader
from django.shortcuts import render, redirect
import random

from home.forms import HumanoFormulario, BusquedaHumanoFormulario
from home.models import Persona



def hola(request):
    return HttpResponse("Buenasss")

def fecha(request):
    fecha_actual=datetime.now()
    return HttpResponse(f"<h1>La hora y fecha actual es {fecha_actual}</h1>")

def calcular_fecha(request,edad):
    fecha=datetime.now().year - edad
    return HttpResponse(f"Tu fecha de nacimiento para {edad} es {fecha}")

# def mi_template(request):
    
#     cargar_archiv=open(r"C:\Users\User\Documents\UNLAM\ZCODERHOUSE\Proyecto\proyecto\proyectoClase\plantillas\template.html", "r")
#     template=Template(cargar_archiv.read())
#     cargar_archiv.close()
#     contexto=Context()
#     template_renderizado=template.render(contexto)
#     return HttpResponse(template_renderizado)

def tu_template(request,nombre):
    
    # cargar_archiv=open(r"C:\Users\User\Documents\UNLAM\ZCODERHOUSE\Proyecto\proyecto\proyectoClase\plantillas\template.html", "r")
    # template=Template(cargar_archiv.read())
    # cargar_archiv.close()
    # contexto=Context({'persona':nombre})
    # template_renderizado=template.render(contexto)
    # return HttpResponse(template_renderizado)
    template = loader.get_template('tu_template.html')
    template_renderizado=template.render({'persona':nombre})
    return HttpResponse(template_renderizado)

def prueba_template(request):
    mi_contexto={
        'rango':list(range(1,11)),
        'valor_aleatorio':random.randrange(1,11),
        }
    template = loader.get_template('prueba_template.html')
    template_renderizado=template.render(mi_contexto)
    return HttpResponse(template_renderizado)

def crear_persona(request):
    
    if request.method=='POST':
        
        formulario=HumanoFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre=data['nombre']
            apellido=data['apellido']
            edad=data['edad']
            
            fecha_creacion=data['fecha_creacion']
            if not fecha_creacion:
                fecha_creacion=datetime.now()
            
            # fecha_creacion=data['fecha_creacion'] or datetime.now()
            
            persona=Persona(nombre=nombre,apellido=apellido,edad=edad,fecha_creacion=fecha_creacion)
            persona.save()
        
        return redirect('ver_persona')
    
    formulario=HumanoFormulario()


    return render(request,'home/crear_persona.html',{'formulario':formulario})

def ver_personas(request):
    
    nombre=request.GET.get('nombre',None)
    
    if nombre:
        personas = Persona.objects.filter(nombre__icontains=nombre) 
    else:
        personas=Persona.objects.all()
    
    formulario=BusquedaHumanoFormulario()
    
    return render(request,'home/ver_persona.html',{'personas': personas,'formulario':formulario})

def index(request):
    fecha_actual=datetime.now()
    return render(request,'home/index.html',{'fecha_actual':fecha_actual})