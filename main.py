'''
Abimael Reyes
video 12 - funciones
'''

def my_func(nombre):
	print(f"soy {nombre}")

# my_func("Abi")

def sumar(a,b):
	res= a + b
	return "soy una suma", res

tipo, resultado = sumar(3,4)
# print(tipo)
# print(resultado)

import random

def get_stats():
	dados = [random.randint(1,6) for i in range(4)]
	dados.sort()
	max_dados=dados[-3:]
	return sum(max_dados)

stats={
	"str": get_stats(),
	"des": get_stats(),
	"int": get_stats(),
	"wis": get_stats(),
	"cons": get_stats()
}

print(stats)