# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 00:01:41 2020

@author: 52971
"""

'''
Un profesor tiene un salario inicial de $1500, y recibe un incremento de 10 % anual durante 6 años. ¿Cuál es su salario al cabo de 6 años? 
¿Qué salario ha recibido en cada uno de los 6 años? 
'''
base = 1500
año = 1
print("El sueldo base de cada año es: ")
while año <= 6:
	print ("El sueldo: ", año, " fue de", float(base))
	base = base + base * (10/100)
	año = año + 1
print("sueldo despues de 6 años: ", float(base))

