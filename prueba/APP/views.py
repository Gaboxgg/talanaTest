from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from models import Auto , Cliente , HojaDeVida , Reserva
import datetime

from django.http import JsonResponse

def noArrendado(fecha):
    if fecha==None or fecha == '': return True
    
    horas_anadidas = datetime.timedelta(hours = 2)
    fecha=fecha+horas_anadidas

    if fecha<dateTime.now():
        return True
    else:
        return False    

def buscar_autos(request):
    cant_puertas = request.GET.get('cant_puertas', None)
    diesel = request.GET.get('diesel', None)
    tamano = request.GET.get('tamano', None)

    preData = Auto.objects.filter(diesel=diesel,tamano=tamano,puertas=cant_puertas)


    data = {}
    if len(preData)>0:
        autosStr=""
        for auto in preData:
            if noArrendado(auto.arrendado_en):
                autosStr=autosStr+"##"+auto.modelo+"##"+auto.puertas+"##"+auto.diesel+"##"+\
                auto.tamano+"##"+str(auto.id)+"**"

        data = {
            'autos': autosStr
        }

    return JsonResponse(data)

def login(request):
    form = AuthenticationForm()
    error=''
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        data= request.POST
        rut = data['username']
        clave = data['password']
        if rut!='' and clave!='':
	
            user = Cliente.objects.filter(rut=rut, clave=clave)
		
            if len(user)>0:
                data_dict = {'nombre': user[0].nombre,\
                'rut':user[0].rut,\
                'autos_arredandos':user[0].autos_arredandos,\
                'flota':Auto.objects.all().count()}
                        
                return render(request, "welcome.html",data_dict)
            
            error="Usuario no registrado"   
    		

    return render(request, "login.html", {'form': form,'error':error})

def logout(request):
    return redirect('/')