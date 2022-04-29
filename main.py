'''
Abimael Reyes
video 10 - for the people by the people
'''

'''

tirar 4 dados y quedarnos con la suma de los 3 mejores
'''
# import random

# dado1 = int(random.randint(1,6))
# dado2 = int(random.randint(1,6))
# dado3 = int(random.randint(1,6))
# dado4 = int(random.randint(1,6))
# suma=0

# # if(dado1<dado2 and dado1 < dado3 and dado1<dado4): 
# # 	suma= dado2+dado3+dado4
# # if(dado2<dado1 and dado2 < dado3 and dado2<dado4): 
# # 	suma= dado1+dado3+dado4 
# # if(dado3<dado2 and dado3 < dado and dado3<dado4): 
# # 	suma= dado2+dado1+dado4
# # if(dado4<dado2 and dado4 < dado3 and dado4<dado1): 
# # 	suma= dado2+dado3+dado1

# # print("dado1 %i dado2 %i dado3 %i dado4 %i"%(dado1,dado2,dado3,dado4))

# suma = dado1+dado2+dado3+dado4
# menor= min(dado1,dado2,dado3,dado4)
# result=suma-menor
# print("Fuerza: %i"%result)

# dado1 = int(random.randint(1,6))
# dado2 = int(random.randint(1,6))
# dado3 = int(random.randint(1,6))
# dado4 = int(random.randint(1,6))

# suma = dado1+dado2+dado3+dado4
# menor= min(dado1,dado2,dado3,dado4)
# result=suma-menor
# print("Destreza: %i"%result)

# dado1 = int(random.randint(1,6))
# dado2 = int(random.randint(1,6))
# dado3 = int(random.randint(1,6))
# dado4 = int(random.randint(1,6))

# suma = dado1+dado2+dado3+dado4
# menor= min(dado1,dado2,dado3,dado4)
# result=suma-menor
# print("Constitucion: %i"%result)

# dado1 = int(random.randint(1,6))
# dado2 = int(random.randint(1,6))
# dado3 = int(random.randint(1,6))
# dado4 = int(random.randint(1,6))

# suma = dado1+dado2+dado3+dado4
# menor= min(dado1,dado2,dado3,dado4)
# result=suma-menor
# print("Inteligencia: %i"%result)

# dado1 = int(random.randint(1,6))
# dado2 = int(random.randint(1,6))
# dado3 = int(random.randint(1,6))
# dado4 = int(random.randint(1,6))

# suma = dado1+dado2+dado3+dado4
# menor= min(dado1,dado2,dado3,dado4)
# result=suma-menor
# print("Sabiduria: %i"%result)

# dado1 = int(random.randint(1,6))
# dado2 = int(random.randint(1,6))
# dado3 = int(random.randint(1,6))
# dado4 = int(random.randint(1,6))

# suma = dado1+dado2+dado3+dado4
# menor= min(dado1,dado2,dado3,dado4)
# result=suma-menor
# print("Carisma: %i"%result)

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