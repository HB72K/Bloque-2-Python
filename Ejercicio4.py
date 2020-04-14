# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 23:37:15 2020

@author: 52971
"""

'''
El dueño de un estacionamiento requiere un programa en Python 
que le permita determinar cuánto debe cobrar por el uso del
estacionamiento a sus clientes. Las tarifas que se tienen son 
las siguientes: Las dos primeras horas a $5.00 c/u. o Las siguientes 
tres a $4.00 c/u. o Las cinco siguientes a $3.00 c/u. o 
Después de diez horas el costo por cada una es de dos pesos
'''
horas = int(input("ingrese las  horas que se uso el estacionamiento:"))
if(horas>10):
    costo = horas * 2
elif(horas>5) and (horas<=10):
    costo = horas * 3
elif(horas>3) and (horas<=5):
    costo = horas * 4
else:
    costo = horas * 5
print("El costo total, por las horas de estacionamiento es:",costo)
