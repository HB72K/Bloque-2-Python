# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 23:13:26 2020

@author: 52971
"""

'''
 Realice un programa que determine el promedio que obtendrá un alumno 
 considerando que realiza tres exámenes, de los cuales el primero
 y el segundo tienen una ponderación de 25%, mientras que el tercero de 50%. 
 '''
 
exa1 =float(input("Ingresa calificación del examen 1\n"))
exa2 =float(input("Ingresa calificación del examen 1:\n"))
exa3 =float(input("Ingresa calificación del examen 1:\n"))



a= (exa1) * 25 /100
b= (exa2) * 25 /100
c= (exa3) * 50 /100


promedio = (a+ b+ c) 

if exa1 >= 10 or exa2 > 10 or exa3 >= 10:
	print ("Calificación erronea (la calificación debe ser entre 0 y 10)")
elif exa1 >= 10 or exa2 >= 10 or exa3 >= 10:
	print ("Calificación erronea (la calificación debe ser entre 0 y 10)")
else: 
	print ("El promedio general del alumno es: ", promedio)
