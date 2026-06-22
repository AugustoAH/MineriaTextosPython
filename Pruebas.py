"""
# Crear una listad
Lista = [1, 2, 3, 4, 5]

#Crear un Tupla
Tupla = (1, 2, 3, 4, 5)

#Crear un Diccionario
Diccionario = {"Nombre": "Juan", "Edad": 30, "Ciudad": "Madrid"}    


print("Lista:", Lista)
print("Mínimo de la lista:", min(Lista))
print("Máximo de la lista:", max(Lista))
print("Suma de la lista:", sum(Lista))

print(3 in Lista)  # Verificar si el número 3 está en la lista
print(Lista.count(2))  # Contar cuántas veces aparece el número 2 en la lista 
print(Lista.index(4))  # Obtener el índice del número 4 en la lista 

# Notación a[ ini : fin : paso ]
print("Lista original:", Lista)
print("Elementos desde el índice 1 hasta el 3:", Lista[1:4])  # Elementos desde el índice 1 hasta el 3 (excluyendo el índice 4)
print("Elementos desde el inicio hasta el índice 2:", Lista[:3])  # Elementos desde el inicio hasta el índice 2 (excluyendo el índice 3)
print("Elementos desde el índice 2 hasta el final:", Lista[2:])  # Elementos desde el índice 2 hasta el final
print("Todos los Elementos:", Lista[:])  # Todos los elementos de la lista
print("Elementos con paso 2:", Lista[::2])  # Elementos con paso 2 (todos los elementos en posiciones pares)        

s = "el ser que puede ser comprendido es lenguaje (Gadamer)"
print(s.startswith("el"), s.endswith("el"))  # Verificar si la cadena comienza con "el" y termina con "el"

p1 = s.find("ser")  # Encontrar la posición de la primera aparición de "ser"
p2 = s.find("ser", p1 + 1)  # Encontrar la posición de la segunda aparición de "ser"
p3 = s.find("ser", p2 + 1)  # Intentar encontrar una tercera aparición de "ser" (no existe)
pf = s.rfind("ser")  # Encontrar la posición de la última aparición de "ser"
print(p1, p2, p3, pf)  # Imprimir las posiciones encontradas

caja = [['tornillo','turcas','arandelas'],['martillo','sierra']]
caja[0].append('clavos')
print(caja)

"""
x = input("Ingrese un número: ")
y = input("Ingrese otro número: ")
if x > y:
    print(f"{x} es mayor que {y}")
elif x < y:
    print(f"{y} es mayor que {x}")
else:
    print("Ambos números son iguales")

for i in range(int(y)):
    print(i)

