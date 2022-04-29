'''
Abimael Reyes
video 10 - for the people by the people
'''

'''

numeros = [6,5,3,8,4,2,5,4,11]

# for num in numeros:
# 	print(num)

# for i in range(10):
# 	print(i)
# else:
# 	print("no hay mas numeros")

# tabla2=[(i+1)*2 for i in range(10)]

# print(tabla2)

'''
curso tiene 30 alumnxs
cada alumnx tiene 3 notas
'''
import random

cant_alum=int(input("Ingrese la cant de alumnos: "))
cant_notas= int(input("Ingrese la cant. de notas: "))

notas= [random.randint(1,10) for i in range(cant_notas)]

alum=[(i+1) for i in range(cant_alum)]

for num in alum:
	notas= [random.randint(1,10) for i in range(cant_notas)]
	prom=0
	prom=sum(notas)/cant_notas
	print("El promedio del alumno %i es: %.2f"%(num,prom))
else:
	print("Gracias")