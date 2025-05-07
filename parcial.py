# Ejercicio 1

suma = 0 # Se crea la variable suma = 0 para que la suma de los números empiece desde 0 
for x in range(5): # x toma los valores del 1 al 5, es decir que las líneas siguientes dentro de este bloque se ejecutarán 5 veces
    número = int(input("Ingrese un número: ")) # Se crea la variable número que es igual al número ingresado por el usuario (se repite 5 veces). Como son números enteros se usa el int antes del input
    if número %2 == 0 and número >= 0: # Se crean 2 condicionales separados por and, uno identifica si el cociente de un número dividido 2 es = a 0 (lo que significa que es par) y el otro verifica que el número sea mayor o igual a 0 (lo que significa que es positivo)
        suma += número # A la variable "suma = 0" se le suman sucesivamente los números que cumplieron la condición. El += hace que la variable suma se actualice para hacer la suma con el nuevo valor
print(f"La suma de los positivos y pares es: {suma}") # Se imprime un mensaje al usuario seguido de la variable suma, que es el resultado


# Ejercicio 2 

edad = int(input("Ingrese su edad ")) # Se crea la variable edad, que es igual al número de edad ingresado por el usuario. En el ejercicio anterior se explica el uso del int antes del input
if edad < 0: # Esta condición verifica si el número ingresado es positivo o negativo
    print("Error") # Si se cumple la condición se muestra en pantalla error, porque signifiaría que la edad es negativa
    edad = int(input("Su edad debe ser un número positivo, ingresela de nuevo: ")) # Se le pide al usuario que vuelva a ingresar la edad, aclarando que debe ser un número positivo
if edad >= 0 and edad < 13: # Se crea la condición de "si la edad es mayor o igual a 0 y menor que 13"
    print("Usted es un niño") # Si se cumple con la condición significa que el usuario es un niño, así que se imprime ese mensaje
if edad >= 13 and edad <= 17: # En las demás líneas se crean las otras condiciones de edad para adolescente, adulto y adulto mayor, todas siguen una estructura similar a la anterior así que no las explico detalladamente
    print("Usted es un adolescente") # No se usa elif para que después del error, si se ingresa una nueva edad también se muestre el mensaje
if edad >= 18 and edad <= 59:
    print("Usted es un adulto")
if edad >= 60:
    print("Usted es un adulto mayor")

# Ejercicio 3 

palabra = input("Ingrese una palabra (sin espacios): ") # Se crea la variable palabra, que es igual a la palabra que ingresa el usuario
a = 0 # Se crean las variables para cada una de las vocales, todas deben ser igual a 0 para que al hacer la suma de cada una de ellas esta empiece desde 0
e = 0 
i = 0 
o = 0
u = 0 
for x in palabra: # x va a recorrer cada uno de los valores (letras) de la palabra ingresada por el usuario y verificará las condiciones
    if x == "a" or x == "A": # Si la letra que toma x es igual a "a" o a "A"
        a += 1 # Se sumará 1 a la variable a si se cumple con la condición, se actualizará la variable y se hará la suma de nuevo si se vuelve a cumplir con la condición
    elif x == "e" or x == "E": # Se crea la misma condición, pero para las demás vocales
        e += 1
    elif x == "i" or x == "I":
        i += 1
    elif x == "o" or x == "O":
        o += 1
    elif x == "u" or x == "U":
        u += 1 
print("La palabra tiene:") # Se muestra un mensaje con el número de vocales que tiene la palabra, una por una, como las variables pasaron por las condiciones, se muestra su valor actualizado
print(f"a: {a}")
print(f"e: {e}")
print(f"i: {i}")
print(f"o: {o}")
print(f"u: {u}")



