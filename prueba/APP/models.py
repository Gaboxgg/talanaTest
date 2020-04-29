from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Auto(models.Model):
    modelo = models.CharField(max_length=100,default='')
    tamano = models.CharField(max_length=100)
    puertas = models.CharField(max_length=300)
    diesel = models.CharField(max_length=300)
    hoja_vida = models.CharField(max_length=300,blank=True,null=True)
    arrendado_en = models.DateTimeField(max_length=100,blank=True,null=True)
    entregado_en = models.DateTimeField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.modelo


class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    rut = models.CharField(max_length=300)
    clave = models.CharField(max_length=300)
    autos_arredandos = models.IntegerField()


    def __str__(self):
        return self.nombre

class HojaDeVida(models.Model):
    hoja_vida = models.CharField(max_length=300,blank=True,null=True)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(max_length=100)

    def __str__(self):
        return self.creado_en


class Reserva(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(max_length=100)

    def __str__(self):
        return self.creado_en