from pipes import Template
from django.http import HttpResponse
from datetime import datetime
from django.template import Context


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