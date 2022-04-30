'''
Abimael Reyes
video 11 - diccionarios
'''

# mi_dic={"nombre":"Abi", "edad":28 , "verdad": True}

## Obtener una key
# print(mi_dic.get("ape", "Key no valida"))

## Solo muestra las key del dicionario
# for value in mi_dic:
# 	print(value)

## cambiar el value de una key
# mi_dic["verdad"]=False

## Consultar por key y value de un disccionario
# for key, value in mi_dic.items():
# 	print(key)
# 	print(value)

## Consultar si existe una key en el diccionario
# if "edad" in mi_dic:
# 	print("Hay edad")

# if "apellido" in mi_dic:
# 	print("Hay apellido")
# else:
# 	print("No hay apellido") 

# # Agregar elementos a un dic

# mi_dic["apellido"]="reyes"
# print(mi_dic)

import random
import nombres

# noms=nombres.get_nombres(2)

# alumnos = {}

# for nombre in noms:
# 	notas = [random.randint(1,10) for i in range(3)]
# 	alumnos[nombre]= notas


# promedios = {}
# for nom in alumnos:
# 	notas=alumnos[nom]
# 	suma = 0
# 	for nota in notas:
# 		suma = nota + suma
# 	promedios[nom] = suma/3

# print(promedios)



cant_alum=int(input("Ingrese la cant de alumnos: "))

cant_notas= int(input("Ingrese la cant. de notas: "))

alum=nombres.get_nombres(cant_alum)

alumnos = {}

# alum=[(i+1) for i in range(cant_alum)]

for nombre in alum:
	notas= [random.randint(1,10) for i in range(cant_notas)]
	alumnos[nombre]=notas

promedios ={}

for nom in alumnos:
	notas=alumnos[nom]
	suma=0
	for nota in notas:
		suma=nota+suma
	promedios[nom]=int(round(suma/cant_notas,0))
else:
	print("Este es el resultado: ")

print(promedios)

aprobados={}

for nom in promedios:
	prom=promedios[nom]
	if prom >=6:
		aprobado="aprobado"
	else:
		aprobado="reprobado"
	aprobados[nom]=aprobado
else:
	print("listado de alumnos aprobados: ")

print(aprobados)