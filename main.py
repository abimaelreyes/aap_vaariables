'''
Abimael Reyes
if y operadores de comparacion
'''

'''
print(5<10) #true
print(2>20) #false
print(6<=6) #true
print(0==0) #true
'''

'''
prom= input
Si prom > 6 entonces 
	probado
sino
	reprobado

'''
'''
prom = int(input("Escribir promedio: "))

if(prom>6):
	print("Aprobado")
else:
	print("Reprobado")
'''
'''
Ingresar 3 notas
guardar notas
suma de las notas y calculo de promedio
Si prom > 6 entonces 
	probado
sino
	reprobado
'''
'''
not1=int(input("Ingrese la nota 1: "))
not2=int(input("Ingrese la nota 2: "))
not3=int(input("Ingrese la nota 3: "))
prom=(not1+not2+not3)/3

print("Su promedio fue: %.2f"%prom )
if(prom>6):
	print("Usted ha sido Aprobado")
else:
	print("Usted ha sido Reprobado")
'''

num = int(input("Ingresar nota: "))

prom = 0
cant = 0
while(num !=0):
	if(num>=0 and num<=10):
	 	prom=num+prom
	 	cant = cant + 1
	 	num = int(input("Ingresar nota: "))
	else:
		num = int(input("Valor fuera del rango, por favor, ingrese nota entre 1 y 10 o 0 para salir: "))

# print("prom %.2f y cant %i"% (prom,cant))

prom_final= prom/cant

print("Promedio final %.2f" %prom_final)