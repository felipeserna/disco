from django.shortcuts import render
import os
##SETTINGS_PATH = os.path.dirname(os.path.dirname('justColor/index.hmtl'))


#Request: Para realizar peticiones.
#HttpResponse: Para enviar la respuesta usando el protocolo HTTP.

#Esto es una vista:
def home(request): #pasamos un objeto de tipo request como primer arg.
    return render(request, 'index.html')
