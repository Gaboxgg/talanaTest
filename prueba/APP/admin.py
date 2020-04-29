from __future__ import unicode_literals

from django.contrib import admin

from models import Auto , Cliente , HojaDeVida , Reserva

# Register your models here.
admin.site.register(Auto)
admin.site.register(Cliente)
admin.site.register(HojaDeVida)
admin.site.register(Reserva)