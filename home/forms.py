from asyncio.windows_events import NULL
from mailbox import NoSuchMailboxError
from django import forms

class HumanoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fecha_creacion = forms.DateField(required=False)
    
class BusquedaHumanoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30, required=NULL)