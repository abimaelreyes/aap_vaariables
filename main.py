'''
Abimael Reyes
video 13 - funciones pt2
'''

# *Args y **Kwargs, estos nos dan como resultado una tupla y un diccionario, respectivamente

def argumentos(*patitos):
	print(patitos)

def kwargunmentos(**kwpatitos):
	print(kwpatitos)

# argumentos("Hola", 2, "Chao")

# kwargunmentos(nombre="Hola", edad=2, despedida="Chao")

def suma(a,b):
	return a+b

def res(a,b):
	return a-b

def mul(a,b):
	return a*b

def div(a,b):
	return a/b

op= {
	"suma": suma,
	"resta": res,
	"multi": mul,
	"divi": div
}

print(op["suma"](1,2))