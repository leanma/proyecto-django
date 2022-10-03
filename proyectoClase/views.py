from pipes import Template
from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template,loader
import random

from home.models import Persona

def hola(request):
    return HttpResponse("Buenasss")

def fecha(request):
    fecha_actual=datetime.now()
    return HttpResponse(f"<h1>La hora y fecha actual es {fecha_actual}</h1>")

def calcular_fecha(request,edad):
    fecha=datetime.now().year - edad
    return HttpResponse(f"Tu fecha de nacimiento para {edad} es {fecha}")

def mi_template(request):
    
    cargar_archiv=open(r"C:\Users\User\Documents\UNLAM\ZCODERHOUSE\Proyecto\proyecto\proyectoClase\plantillas\template.html", "r")
    template=Template(cargar_archiv.read())
    cargar_archiv.close()
    contexto=Context()
    template_renderizado=template.render(contexto)
    return HttpResponse(template_renderizado)

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

def crear_persona(request,nombre,apellido):
    
    persona=Persona(nombre=nombre,apellido=apellido,edad=random.randrange(1,99),fecha_nacimiento=datetime.now())
    persona.save()
    template = loader.get_template('crear_persona.html')
    template_renderizado=template.render({'persona':persona})
    
    return HttpResponse(template_renderizado)

def ver_personas(request):
    
    personas=Persona.objects.all()
    template = loader.get_template('ver_persona.html')
    template_renderizado=template.render({'personas':personas})
    
    return HttpResponse(template_renderizado)