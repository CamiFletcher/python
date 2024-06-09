#SEMANA 1 /// EJERCICIO 7
"""
print("Hola Mundo")
"""

#SEMANA 1 /// EJERCICIO 8
"""
variable = "Hola Mundo"
print(variable)
"""

#SEMANA 1 /// EJERCICIO 9
"""
variable = 1
print(variable)
"""

#SEMANA 1 /// EJERCICIO 10
"""
SUMA
numeroUno = 1
numeroDos = 3
resultado = numeroUno + numeroDos
print(resultado)
"""

#SEMANA 1 /// EJERCICIO 11
"""
MULTIPLICACIÓN
numeroUno = 1
numeroDos = 3
resultado = numeroUno * numeroDos
print(resultado)

RESTA
numeroUno = 1
numeroDos = 3
resultado = numeroUno - numeroDos
print(resultado)

DIVISIÓN
numeroUno = 1
numeroDos = 3
resultado = numeroUno / numeroDos
print(resultado)
"""

#SEMANA 2 /// EJERCICIO 1
"""variable = int(input("Por favor, ingrese un número entero: "))
print(variable)"""

#SEMANA 2 /// EJERCICIO 2
"""
variableUno = int(input("Por favor, ingrese un número entero: "))
variableDos = int(input("Por favor, ingrese otro número entero: "))

suma = variableUno + variableDos
resta = variableUno - variableDos
multiplicacion = variableUno * variableDos
division = variableUno / variableDos
resto = variableUno % variableDos

print("La suma de ", variableUno ," y ", variableDos ," es ", suma)
print("La resta de ", variableUno ," y ", variableDos ," es ", resta)
print("El producto de ", variableUno ," y ", variableDos ," es ", multiplicacion)
print("La division de ", variableUno ," y ", variableDos ," da ", division)
print(f"El resto de {variableUno} por {variableDos} es {resto}")
"""

#SEMANA 2 /// EJERCICIO 3
"""
variable = int(input("Por favor, ingrese un número entero: "))

if variable % 2 == 0:
    print("Su número es par")
else:
    print("Su número es impar")
"""

#SEMANA 2 /// EJERCICIO 4
"""
añoNacimiento = int(input("Por favor, ingrese su año de nacimiento: "))
añoFuturo = int(input("Por favor, ingrese un año futuro: "))

solucion = añoFuturo - añoNacimiento
print("En ese año, usted tendrá", solucion)
"""

#SEMANA 2 /// EJERCICIO 5
"""
numeroUno = int(input("Por favor, ingrese un primer número: "))
numeroDos = int(input("Por favor, ingrese un segundo número: "))
numeroTres = int(input("Por favor, ingrese un tercer número: "))
numeroCuatro = int(input("Por favor, ingrese un cuarto número: "))
numeroCinco = int(input("Por favor, ingrese un quinto número: "))

promedio = (numeroUno + numeroDos + numeroTres + numeroCuatro + numeroCinco) / 5
print(f"El promedio entre todos los números es de {promedio}")
"""

#SEMANA 2 /// EJERCICIO 6
"""
def posicion_numero(numero):
    anterior = numero-1
    siguiente = numero+1
    print(f"El anterior de {numero} es {anterior} y el siguiente es {siguiente}")

num = int(input("Ingrese un número para mostrar el anterior y el siguiente: "))
posicion_numero(num)
"""

"""
def posicion_numero(numero):
    anterior = numero-1
    siguiente = numero+1
    mensaje = f"El anterior de {numero} es {anterior} y el siguiente es {siguiente}"
    return mensaje

num = int(input("Ingrese un número para mostrar el anterior y el siguiente: "))
print(posicion_numero(num))
"""

#SEMANA 2 /// EJERCICIO 7
"""
def str_int(texto, entero):
    concatenar = texto+str(entero)
    return concatenar

uno = "Hola, ¿qué tal? Soy el número "
dos = 15
print(str_int(uno, dos))
"""

#SEMANA 2 /// EJERCICIO 8
"""
def resto_y_cociente(num):
    cociente = num//2
    resto = num%2
    mensaje = f"El cociente del numero {num} es {cociente} y el resto es {resto}"
    return mensaje

numero = int(input("Ingrese un número para dividirlo por 2: "))
print(resto_y_cociente(numero))
"""

#SEMANA 2 /// EJERCICIO 9
"""
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
print(f"Usted es {apellido}, {nombre}")
"""

#SEMANA 2 /// EJERCICIO 10
"""
palabra = input("Ingrese una palabra para medir su longitud: ")
longitud = len(palabra)
print(longitud)
"""

#SEMANA 2 /// EJERCICIO 11
""" DIFICIL
palabra = input("Ingrese una palabra para recortar: ")
longitud = len(palabra)
recorte = int(input("Ingrese el número de la cantidad de caracteres a cortar"))

if recorte>longitud:
    print("La palabra que usted ingresó no puede ser recortada en esa cantidad de caracteres, vuelva a iniciar el programa")
else:
    print(f"La palabra recortada es {palabra[0:recorte]}")
"""

""" FACIL
name = input("Ingrese su nombre: ")
name_slicer = name[0:5]
print(name_slicer)
"""

#SEMANA 2 /// EJERCICIO 12
"""
palabra = input("Escriba una palabra para quitarle las a: ")
nueva_palabra = palabra.replace("a","")
print(nueva_palabra)
"""

#SEMANA 3 /// EJERCICIO 1: Escribir la expresión para saber si un número es más grande que otro. Guardarla en una variable de tipo
#bool e imprimirla por pantalla para ver su valor.
"""
num1 = 15
num2 = 12

if num1>num2:
    print(f"El número más grande es {num1}")
else:
    print(f"El número más grande es {num2}")
"""

#SEMANA 3 /// EJERCICIO 2: Repetir el punto anterior pero con la expresión que determina que una letra NO es vocal.
"""
letra = input("Ingrese una letra: ")
letra = letra.lower()

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("Su letra es una vocal")
else:
    print("Su letra no es vocal")
"""

#SEMANA 3 /// EJERCICIO 3: Repetir pero para la expresión que permite saber si un número es par y menor a 10.
"""
numero = int(input("Ingrese un número"))

if numero%2==0 and numero<10:
    print("Su número es par y menor a 10")
elif numero%2==0 or numero<10:
    print("Su número es par o menor a 10")
else:
    print("Su número no es par ni menor a 10")
"""

#SEMANA 3 /// EJERCICIO 4: Crear una función que dado un número, devuelva su valor absoluto. El valor absoluto de un número es
#el mismo número sin considerar el signo.
"""
def valor_absoluto(numero):
    if numero>0:
        return numero
    else:
        numero=numero*-1
        return numero

num1 = int(input("Ingrese un número: "))
print(valor_absoluto(num1))
"""

#SEMANA 3 /// EJERCICIO 5: Crear el programa al que sea imposible ganarle en el juego de “Piedra, papel o tijera”. Cada elemento va
#a ser representado con una letra: R para piedra, P para papel y T para tijera.
"""
print("¡Juguemos al Piedra, Papel o Tijera!")
letra = input("R es para hacer piedra, P para papel y T para tijera, ¡ingresa una letra para poder jugar! ")
letra = letra.lower()

if letra == "r":
    print("P")
    print("¡Te gané!")
elif letra == "p":
    print("T")
    print("¡Te gané!")
elif letra == "t":
    print("R")
    print("¡Te gané!")
else:
    print("¡No vale! Volvé a ingresar para jugar")
"""

#SEMANA 3 /// EJERCICIO 6: Escribir código que dado dos enteros, determine si la suma de ambos da menos que 100. Si la suma de
#ambos es menor a 100, calcular cuánto falta para llegar a 100 y mostrar por pantalla un mensaje con
#ese valor. Si la suma es mayor a 100, mostrar un mensaje diciendo “Llega a 100”.
"""
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un número: "))

if num1+num2>=100:
    print("La suma de ambos números es mayor o igual a 100")
else:
    resultado = 100-(num1+num2)
    print(f"La suma de ambos números no da 100: Le faltan {resultado} para llegar.")
"""
#Extra: ¿Cómo harían para que el programa quede generalizado para cualquier límite, a elección del
#usuario, y no solo para 100?.
"""
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un número: "))
resultado = int(input("Ingrese el resultado para comparar"))

if num1+num2>=resultado:
    print(f"La suma de ambos números es mayor o igual a {resultado}")
else:
    solucion = resultado-(num1+num2)
    print(f"La suma de ambos números no da {resultado}: Le faltan {solucion} para llegar.")
"""

#SEMANA 3 /// EJERCICIO 7: Se tienen letras para representar las estaciones del año. Crear una función que dada una letra, imprima por pantalla la estación del año que representa (es
#decir, si se ingresa V se mostrará por pantalla el mensaje “Verano”). En caso de no representar a
#ninguna estación mostrar un mensaje que diga “error”.
"""
estacion = input("Ingrese la primera letra de una estacion del año: ")
estacion=estacion.lower()

if estacion == "v":
    print("Verano")
elif estacion == "o":
    print("Otoño")
elif estacion == "i":
    print("Invierno")
elif estacion == "p":
    print("Primavera")
else:
    print("ERROR")
"""

#SEMANA 3 /// EJERCICIO 8: Se quiere hacer un programa para enseñar a unos niños a contar. Crear una función que reciba un
#número entero e imprima por pantalla los números del 1 hasta ese número con la estructura de control
#iterativa for.
"""
def contar(num : int):
    for i in range(1,num+1):
        print(i)

numero = int(input("Ingrese un número"))
contar(numero)
"""

#SEMANA 3 /// EJERCICIO 9: Crear una función que reciba un número entero e imprima por pantalla la tabla de ese número del 1 al 10.
"""
def tabla(numero):
    for i in range(1,11):
        solucion = numero * i
        print(f"{i}*{numero}={solucion}")

num = int(input("Ingrese un número entero: "))
tabla(num)
"""

#SEMANA 3 /// EJERCICIO 10: Crear una función que simule un cumpleaños: que dado un entero imprima “Que los cumplas feliz” esa cantidad de veces.
"""
def cumple(numero):
    for i in range(1,numero):
        print("Que los cumplas feliz")

num = int(input("¿Cuántos años cumplís? "))
cumple(num)
"""

#SEMANA 3 /// EJERCICIO 11: Crear una función que reciba un número entero que representa lo que hay que cobrar, le pida al
#usuario ingresar un monto, y se vaya mostrando por pantalla cuánto falta para completar el pago. Repetir este proceso hasta que la deuda sea 0 
#o menor
"""
def pago(numero):
    while numero>0:
        ingresa = int(input(f"El importe a pagar es de {numero} pesos. Por favor, ingrese lo que desea pagar: "))
        numero = numero-ingresa

monto = int(input("Ingrese el monto de su compra: "))
pago(monto)
print("Muchas gracias por su compra")
"""

#SEMANA 3 /// EJERCICIO 12: Escribir código que recorra los números del 1 al 20 y determine para cada uno si es par o impar,
#imprimiendo un mensaje por pantalla en cada caso.
"""
for numero in range (0,21):
    if numero%2 == 0:
        print(f"El número {numero} es par")
    else:
        print(f"El número {numero} es impar")
"""

#SEMANA 3 /// EJERCICIO 13: Hacer una función que reciba un número que represente el precio de la máquina, e imprima
#por pantalla “Ingresá x fichas para comenzar” hasta que se hayan ingresado esa cantidad de letras F (que representan una ficha), 
#y luego “¡A jugar!” cuando se hayan ingresado todas las fichas necesarias. Ahora se quiere que se vaya mostrando por pantalla, cuántas fichas FALTAN 
#ingresar para empezar a jugar. Agregar a la función el mensaje de error “Por favor solamente ingrese fichas reales (F)” cuando se recibe una letra distinta de F.
"""
def pago(numero):
    while numero>0:
        fichas = input(f"Ingresa {numero} fichas para comenzar: ")
        fichas = fichas.lower()

        if fichas == "f":
            fichas = len(fichas)
            numero = numero-fichas
        else:
            print("Por favor solamente ingrese fichas reales (F)")

num = 3
pago(num)
print("¡A jugar!")
"""

#SEMANA 3 /// EJERCICIO 14: Crear una función que reciba un número entero e imprima los números primos entre 0 y el número ingresado.
"""
def primo(num):
    posible_divisor = 1
    divisores = 0
    while posible_divisor <= num:
        if num % posible_divisor == 0:
            divisores += 1
        posible_divisor += 1
    if divisores == 2:
        return True
    else:
        return False

numero = int(input("Ingrese un número: "))

for i in range(1, numero+1):
    if primo(i) == True:
        print(i)
"""

#SEMANA 4 /// EJERCICIO 1: Crear una lista con los números del 1 al 10. Acceder con el índice a la posición que contiene el número
#5, e imprimirlo por pantalla. Recordar que el índice de las listas empiezan con 0.
"""
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista.index(5))
"""

#SEMANA 4 /// EJERCICIO 2: Con la lista del punto anterior, usar la función len() para averiguar su longitud, e imprimirla.
"""
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
largo_lista = len(lista)
print(largo_lista)
"""

"""
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(lista))
"""

#SEMANA 4 /// EJERCICIO 3: Crear una secuencia con números distintos, y luego devolver el elemento máximo y el mínimo.
"""
lista = [5,2,13,7,15]
maximo = max(lista)
minimo = min(lista)
print(f"El máximo de la lista {lista} es {maximo} y el mínimo es {minimo}.")
"""

#SEMANA 4 /// EJERCICIO 4: Ordenar la secuencia del ejercicio anterior, e imprimirla por pantalla.
"""
lista = [5,2,13,7,15]
lista.sort(reverse = True)
print(lista)
"""
"""
lista = [5,2,13,7,15]
lista = sorted(lista,reverse = False)
print(lista)
"""

#SEMANA 4 /// EJERCICIO 5: Crear una tupla que guarde tu nombre y tu edad. Luego, imprimir por pantalla tu edad, accediendo al
#elemento de la tupla que corresponda.
"""
tupla = ("Camila", "18")
print(tupla[1])
"""

#SEMANA 4 /// EJERCICIO 6: Hacer una lista con 5 nombres.
#A) Cambiar el último elemento de la lista y cambiar el último nombre por “Juan”. ¿Cómo podría saber cuál es el último elemento si no sé la longitud?
"""
lista = ["Ivan","Lautaro","Teo","Carlos","Tobias"]
longitud = len(lista)
lista[longitud-1] = "Juan"
print(lista)
"""
#B) Devolver el nombre que esté a dos posiciones del final. ¿Cómo hacemos para que nos funcione para cualquier lista y no solo para la que 
#tenga 5 elementos?
"""
lista = ["Ivan","Lautaro","Teo","Carlos","Tobias"]
print(lista[-3])
"""
#C) Recorrer la lista e imprimir cada nombre por pantalla.
"""
lista = ["Ivan","Lautaro","Teo","Carlos","Tobias"]
for i in lista:
    print(i)
"""
#D) Imprimir por pantalla la lista con 3 repeticiones, usar el operador repetición (*).
"""
lista = ["Ivan","Lautaro","Teo","Carlos","Tobias"]
print(lista*3)
"""

#SEMANA 4 /// EJERCICIO 7: Se pide ahora crear 3 tuplas como las del ejercicio 5, con un nombre y una edad. A continuación,
#guardarlas en una lista. Pensar, ¿De que nos servirá guardar las tuplas en una lista en vez de tenerlas por separado?
"""
tupla_1 = ("Pepe","45")
tupla_2 = ("Ivan","2")                  #Porque es fácil y rápido de acceder
tupla_3 = ("Camila","18")
lista = [tupla_1,tupla_2,tupla_3]
"""

#SEMANA 4 /// EJERCICIO 8: Se quiere guardar información de los siguientes países: Francia, Argentina, Japón, Alemania, Perú.
#A) Crear una tupla para cada país que contenga su nombre, su capital y el continente donde se encuentra.
#B) Guardar las tuplas en una lista.
#C) Hacer una función que reciba por parámetros la lista, e imprima la información de cada país
"""
def info(lista_paises : list):
    for pais in lista_paises:
        print(f"Pais: {pais[0]}\nCapital: {pais[1]}\nContinente: {pais[2]}\n ")

francia = ("Francia","Paris","Europa")
argentina = ("Argentina","CABA","América del Sur")
japon = ("Japón","Tokyo","Asia")
alemania = ("Alemania","Berlín","Europa")
peru = ("Perú","Lima","América del Sur")
paises = [argentina,francia,japon,alemania,peru]

info(paises)
"""

#SEMANA 4 /// EJERCICIO 9: Una librería tiene un sistema que guarda los nombres de todos los libros que tienen en una lista de la
#siguiente forma: [“El principito”, “It”, “Sherlock Holmes”...]. Se quiere saber cuántos libros repetidos
#tienen. Hacer código que imprima para cada título, cuántos ejemplares hay.
"""
libros = ["El principito","It","Sherlock Holmes","El principito","El principito","It"]
bandera_1 = True
bandera_2 = True
bandera_3 = True

for libro in libros:
    cantidad = libros.count(libro)
    if bandera_1 == True and cantidad == 1:
        print(f"{libro}: {cantidad} ejemplares")
        bandera_1 = False
    elif bandera_2 == True and cantidad == 2:
        print(f"{libro}: {cantidad} ejemplares")
        bandera_2 = False
    elif bandera_3 == True and cantidad == 3:
        print(f"{libro}: {cantidad} ejemplares")
        bandera_3 = False
"""

#SEMANA 4 /// EJERCICIO 10: Crear una lista que contenga los números del 1 al 10, luego recorrerla y guardar en otra lista esos
#números elevados al cuadrado.
"""
nuevalista = []
lista = [1,2,3,4,5,6,7,8,9,10]
for numero in lista:
    numero = numero*numero
    nuevalista.append(numero)
print(nuevalista)
"""

#SEMANA 4 /// EJERCICIO 11: Hacer una función que reciba una lista, y devuelva un string uniendolas palabras desde el final de
#la lista hasta el principio con un “ ” (espacio) entre cada una, para formar la frase. 
"""
frase = ["entender","pueden","humanos","los","que","código","escriben","programadores","buenos","Los","entiende.","computadora","una","que","código","escribe","tonto","Cualquier"]
frase_ordenada = []
mensaje = ""
for i in reversed(frase):
    frase_ordenada.append(i)
for i in frase_ordenada:
    mensaje = mensaje + f"{i} " 

print(mensaje)
"""

#SEMANA 4 /// EJERCICIO 12: Crear una función que le pregunte al usuario la materia que quiere almacenar, e ir guardando la información en una 
#lista hasta que ingrese una ‘X’. ¿Qué funciones de listas no permiten insertar en una lista?
"""
lista_materias = []
materia=input('Ingrese una materia, * para salir: ')
while materia!='*':
    lista_materias.append(materia)
    materia=input('Ingrese una materia, * para salir: ')
print('Lista de Materias')
print(lista_materias)
"""

#SEMANA 4 /// EJERCICIO 13: Se tiene un ticket de supermercado que se puede representar como una lista de tuplas (producto, precio).
#a. Hacer una función que reciba la lista, calcule y devuelva el total que hay que pagar.
#b. Ahora se tienen dos tickets. Juntar ambos y volver a calcular el total.
"""
producto1 = ("pollo", 600)
producto2 = ("carne", 500)
producto3 = ("queso", 200)
producto4 = ("pan", 300)
lista_productos = [producto1, producto2, producto3, producto4]

def tomar_pedido(lista : list) -> list:
    on = True
    lista_compra = []
    while on:
        eleccion = int(input("¿Qué desea comprar? (1 para detergente, 2 para jabon, 3 para esponja y 4 para trapo); 5 para salir "))
        if eleccion == 5:
            on = False
        elif eleccion == 1:
            var1 = lista_productos[0]
            var2 = var1[1]
            lista_compra.append(int(var2))
        elif eleccion == 2:
            var1 = lista_productos[1]
            var2 = var1[1]
            lista_compra.append(int(var2))
        elif eleccion == 3:
            var1 = lista_productos[2]
            var2 = var1[1]
            lista_compra.append(int(var2))
        elif eleccion == 4:
            var1 = lista_productos[3]
            var2 = var1[1]
            lista_compra.append(int(var2))
    return lista_compra

def calcular_precio(lista : list) -> int:
    acumulador_precio = 0
    for i in lista:
        acumulador_precio = acumulador_precio + i
    return acumulador_precio

print(f"El precio total es de {calcular_precio(tomar_pedido(lista_productos))}")
"""

#SEMANA 4 /// Parte dos: EJERCICIO 1: Hacer una función que reciba un string y que imprima solamente los caracteres que sean vocales.
"""
def muestra_vocales(palabra):
    palabra = palabra.lower()
    mensaje = "" 
    for letra in palabra:
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            mensaje = mensaje + f"{letra} "
    return mensaje

word = str(input("Ingrese una palabra para mostrar sus vocales: "))
print(muestra_vocales(word))
"""

#SEMANA 4 /// Parte dos: EJERCICIO 2: Hacer una función que reciba un string y que lo invierta.
"""
def invertir_palabra(palabra):
    nueva_palabra = ""
    longitud = len(palabra)
    for numero in range(1,longitud+1):
        nueva_palabra = nueva_palabra + palabra[-numero]
    return nueva_palabra

word = "padre"
print(invertir_palabra(word))
"""

#SEMANA 6 /// EJERCICIO 1: Se tiene un archivo con la pregunta “¿Cómo estás hoy?” llamado pregunta.txt. Se pide leerlo y mostrar
#la pregunta por pantalla para luego pedirle al usuario que ingrese una respuesta. Después, guardar la respuesta dada por el usuario en el archivo.
"""
archivo = open("python\\6_1.txt", "r+")
pregunta = archivo.readline()
print(pregunta)
respuesta = input()
archivo.write("\n" + respuesta + "\n")
archivo.close()
"""

#SEMANA 6 /// EJERCICIO 2: En un archivo llamado regalo.txt se tiene la lista de las personas que quieren participar en el regalo de
#cumpleaños de Sol. a) Mostrar por pantalla los nombres de las personas que quieren participar en el regalo. b) Se sabe que quieren 
#poner 1000 pesos por persona por regalo. c) Tomi sabe que si participa Santi, también participa Tomi. Se pide que si Santi está en el archivo
#de los nombres, se agregue también a Tomi.
"""
def cantidad_plata(dinero : int):
    plata = dinero*1000
    mensaje = f"La cantidad de dinero es {plata}"
    return mensaje

archivo = open("python\\6_2.txt", "r+")
contador = 0
lista = archivo.readlines()
for persona in lista:
    contador += 1
    persona = persona.strip("\n")
    if (persona.lower()) == "santi":
        archivo.write("\nTomi\n")
        print("Tomi")
        contador += 1
    print(persona.strip("\n"))
print(cantidad_plata(contador))
archivo.close()
"""

#SEMANA 6 /// EJERCICIO 3: Se pide hacer un programa que cree un archivo de compras.txt (Ayuda: abrir el archivo en modo w) y le
#pregunte al usuario qué necesita comprar hasta que ingrese una X
"""
with open("python\\6_3.txt", "w") as archivo:
    respuesta = input("Que agrego a la lista de compras? ")
    while (respuesta.lower()) != "x":
        archivo.writelines(respuesta + "\n")
        respuesta = input("Que agrego a la lista de compras? ")
"""

#SEMANA 6 /// EJERCICIO 4: Se pide hacer un programa que pida dos palabras: una que se quiera reemplazar y la palabra por la que
#se quiera reemplazar, cambie el texto y lo guarde en el archivo otra vez.
"""
mensaje = ""
palabra_cambiar = input("Nombre la palabra que desee cambiar: ").lower()
reemplazo = input("Palabra con la que quiere reemplazarla: ").lower()

archivo = open("python\\6_4.txt", "r")
lista_lineas = archivo.readlines()
for linea in lista_lineas:
    linea = linea.strip("\n")
    linea = linea.lower()
    linea = linea.replace(palabra_cambiar, reemplazo)
    mensaje = mensaje + linea + "\n"
archivo.close()

archivo2 = open("python\\6_4.txt", "w")
archivo2.write(mensaje)
archivo2.close()
"""

#SEMANA 6 /// EJERCICIO 5: Se tiene un archivo csv que contiene información sobre el stock de una librería. Se guarda por cadalínea, el 
#nombre del producto, el código, el precio por unidad y el stock actual, es decir: nombre;código;precio;stock
#a) Leer el archivo y mostrarlo por pantalla.
#b) Hacer una función que reciba un diccionario que describa una línea del archivo y lo agregue.

#A)
"""archivo = open("python\\6_5.csv", "r")
stock = archivo.readlines()
archivo.close()
for linea in stock:
    linea = linea.strip("\n")
    linea = linea.split(",")
    linea[0] = linea[0].capitalize()
    print("Nombre completo: ", linea[0])
    print("Codigo producto: ", linea[1])
    print("Precio por unidad: ", linea[2])
    print("Stock: ",linea[3])
    print("")"""

#B)
"""def agregar_producto(texto):
    texto.write(f"\n{diccionario["Nombre"],{diccionario["Codigo"]},{diccionario['Precio']},{diccionario['Stock']}}")

archivo = open("python\\6_5.csv", "r+")
diccionario = {
    "Nombre" : "Hoja A4",
    "Codigo" : "35662",
    "Precio" : "600",
    "Stock" : "45"
    }
agregar_producto(archivo)
archivo.close()"""

#SEMANA 6 /// EJERCICIO 6: Una profesora tiene una lista de diccionarios para guardar las notas que sacaron sus alumnos en el
#último parcial que tomó. Cada uno de esos diccionarios tiene el nombre del alumno, su apellido, su dni y la nota que sacó.
#a. Hacer una función que reciba este diccionario, y guarde las notas en un archivo csv, llamados notas.csv
#b. Tiempo después de guardar las notas, la profesora quiso saber la cantidad de alumnos que aprobaron. Hacer una función que lea el 
#archivo creado en el ejercicio anterior, y devolver lacantidad de alumnos aprobados (su nota es mayor a 4).
"""
alumnos = [
    {
        "Nombre" : "Juan",
        "Apellido" : "Perez",
        "DNI" : "12345678",
        "Nota" : "7"
    },
    {
        "Nombre" : "Pedro",
        "Apellido" : "Gomez",
        "DNI" : "87654321",
        "Nota" : "4"
    },
    {
        "Nombre" : "Maria",
        "Apellido" : "Lopez",
        "DNI" : "98765432",
        "Nota" : "9"
    },
    {
        "Nombre" : "Ana",
        "Apellido" : "Garcia",
        "DNI" : "76543218",
        "Nota" : "3"
    }
]

def leer_dicc_alumno(dicc : dict) -> str:
    mensaje = f"{dicc['Nombre']},{dicc['Apellido']},{dicc['DNI']},{dicc['Nota']}"
    return mensaje

csv_packet = ""

for alumno in alumnos:
    csv_packet = csv_packet + leer_dicc_alumno(alumno) + "\n"

archivo = open("notas.csv", "w")
archivo.write(csv_packet)
archivo.close()

archivo2 = open("notas.csv", "r")
lista_alumnos_csv = archivo2.readlines()
archivo2.close()

lista_notas = []
contador_desaprobados = 0

for alumno in lista_alumnos_csv:
    alumno = alumno.strip("\n")
    alumno = alumno.split(",")
    lista_notas.append(alumno[3])

for nota in lista_notas:
    print(nota)
    if int(nota) < 4:
        contador_desaprobados += 1
print(f"Cantidad de alumnos desaprobados: {contador_desaprobados}")
"""

#SEMANA 6 /// EJERCICIO 7: En un cine tienen dos archivos .txt, uno con salas y otro con nombres de películas. Se sabe que en la
#sala de una fila del archivo se va a transmitir la película de la misma fila del archivo de películas. Se pide
#leer los dos archivos, y crear un nuevo archivo csv que tenga el nuevo formato sala;pelicula.

"""archivo_sala = open("python\\6_6(salas).txt", "r")
salas = archivo_sala.readlines()
archivo_sala.close()

archivo_pelicula = open("python\\6_6(peliculas).txt", "r")
peliculas = archivo_pelicula.readlines()
archivo_pelicula.close()

mensaje = ""

for i in range(len(salas)):
    mensaje = mensaje + f"{salas[i].strip("\n")},{peliculas[i].strip("\n")}" + "\n"

archivo_completo = open("python\\6_6(completo).csv", "w")
archivo_completo.write(mensaje)
archivo_completo.close()"""

#SEMANA 6 /// EJERCICIO 8: Hacer un programa que lea el archivo .csv y lo transforme en un archivo .txt. 
"""
def gustar_color(lista : list):
    mensaje = f"A {linea[0]} {linea[2]} le gusta el {linea[1]}"
    return mensaje

csv = open("6_8.csv", "r")
texto = csv.readlines()
csv.close()

escribir_txt = ""

for linea in texto:
    linea = linea.strip("\n")
    linea = linea.split(";")
    escribir_txt = escribir_txt + gustar_color(linea) + "\n"

txt = open("python\\6_8.txt", "w")
txt.write(escribir_txt)
txt.close()
"""

#SEMANA 6 /// Errores: EJERCICIO 1: Se quiere hacer un programa para pedirle al usuario que ingrese un número entero, y en caso de que el
#valor ingresado no sea un número entero, mostrarle un mensaje apropiado.
#a. Realizarlo utilizando isnumeric(). ¿Qué limitaciones encuentra? (No considera negativos)
#b. Realizarlo utilizando try/ except.
"""
numero = None
while type(numero) is not int:
    try:
        numero = input("Ingrese un mumero entero: ")
        numero = int(numero)
        print("El numero es ", numero)
    except ValueError:
        print("El valor ingresado no es valido")
"""

#SEMANA 6 /// Errores: EJERCICIO 2: Crear una función, utilizando el punto anterior, que le pida al usuario un número entero. Utilizarla para
#calcular el producto entre dos números enteros ingresados.
"""
def calcular_producto(entero, entero_2):
    solucion = entero * entero_2
    print(f"El producto de ambos numeros enteros es {solucion}")

numero = None
while type(numero) is not int:
    try:
        numero = input("Ingrese un mumero entero: ")
        numero = int(numero)
    except ValueError:
        print("El valor ingresado no es valido")

numero_2 = None
while type(numero_2) is not int:
    try:
        numero_2 = input("Ingrese un mumero entero: ")
        numero_2 = int(numero_2)
    except ValueError:
        print("El valor ingresado no es valido")
"""

#SEMANA 6 /// Errores: EJERCICIO 3: Se quiere hacer un programa que le solicite al usuario un número divisor y un dividendo, y calcule el
#cociente entre ellos.
"""
def calcular_cociente(divisor, dividendo):
    solucion = dividendo / divisor
    print(f"El cociente entre ambos numeros es {solucion}")

numero = None
while type(numero) is not float:
    try:
        numero = input("Ingrese un mumero entero: ")
        numero = float(numero)
    except ValueError:
        print("El valor ingresado no es valido")

numero_2 = None
while type(numero_2) is not float or numero_2 == 0:
    try:
        numero_2 = input("Ingrese un mumero entero: ")
        numero_2 = float(numero_2)
    except ValueError:
        print("El valor ingresado no es valido")
"""

#SEMANA 6 /// Errores: EJERCICIO 4: Crear un programa para abrir un archivo llamado “file.txt” en modo lectura y en caso de que este
#archivo no exista, mostrar el mensaje “No se pudo encontrar el archivo file.txt”.
"""
try:
    archivo = open("file.txt", "r")
    archivo.close()
except FileNotFoundError:
    print("No se pudo encontrar el archivo file.txt")
"""

#SEMANA 6 /// Errores: EJERCICIO 5: Crear una función cuyos parámetros sean una lista y un índice de posición para mostrar el valor de la lista en esa ubicación.
#a. ¿Qué ocurre si ingreso un índice que se encuentra fuera del rango? (Sale error) IndexError
#b. Si el valor del índice ingresado se encuentra dentro del rango, mostrar el valor. En caso contrario, mostrar un mensaje apropiado para dicho error.
"""
def mostrar_posicion (lista : list, indice : int):
    return lista[indice]

lista_1 = ["Camila", "Tobias", "Ivan"]
indice_1 = int(input("Ingrese la posicion seleccionada: "))
try:
    print(mostrar_posicion(lista_1,indice_1))
except IndexError:
    print("Fuera de rango")
"""

#SEMANA 6 /// Errores: EJERCICIO 6: Para jugar al chinchón con un único mazo de cartas españolas, el número de jugadores puede ser: dos,
#tres o cuatro. Crear una función que pida al usuario informar el número de jugadores.
"""
def pedir_numero():
    num_jugadores = int(input("Ingrese el numero de jugadores: "))
    return num_jugadores

try:
    num_pj = pedir_numero()
    if num_pj != 2 and num_pj != 3 and num_pj != 4:
        if num_pj > 4:
            print("Se puede jugar con un maximo de cuatro jugadores")
        else:
            print("Debe haber al menos dos jugadores")
    else:
        print("Inicio del juego")
except ValueError:
    print("El valor ingresado no es valido")
"""

#SEMANA 6 /// Errores: Ejercicio 7: Para jugar al truco con un único mazo de cartas españolas, el número de jugadores puede ser: dos,
#cuatro o seis. Crear una función que pida al usuario informar el número de jugadores.
"""
def pedir_numero():
    num_jugadores = int(input("Ingrese el numero de jugadores: "))
    return num_jugadores

try:
    num_pj = pedir_numero()
    if num_pj != 2 and num_pj != 6 and num_pj != 4:
        if num_pj > 6:
            print("Se puede jugar con un maximo de cuatro jugadores")
        elif num_pj < 2:
            print("Debe haber al menos dos jugadores")
        else:
            print("Debe haber un numero par de jugadores")
    else:
        print("Inicio del juego")
except ValueError:
    print("El valor ingresado no es valido")
"""

#SEMANA 6 /// Errores: EJERCICIO 8: Se tienen dos diccionarios, uno con un código y el producto, y otro con el código y el precio de cada producto.
#Y le pida al usuario una opción y una cantidad. Luego, debe imprimir el total a pagar. Se debe considerar que el usuario podría ingresar una opción que no está en el diccionario, o ingresar
#una opción que no sea un número. El usuario debe en esos casos imprimir un mensaje de error que sea descriptivo y volver a pedirle al usuario que ingrese una opción
"""
opciones = {
    1: "hamburguesas",
    2: "milanesas",
    3: "gaseosa",
    4: "alfajor",
    5: "papas fritas",
    6: "agua"
}

valores = {
    1: 1000,
    2: 1500,
    3: 500,
    4: 300,
    5: 600,
    6: 350
}

mensaje = ""

for i in range(1,7):
    mensaje = mensaje + f"{i}: {opciones[i]} -> {valores[i]}" + "\n"

print(mensaje)

total = 0
while True:
    try:
        compra = int(input("Que desea comprar? (0 para cerrar la compra): "))
        if compra == 0:
            break
        total += valores[compra]
    except KeyError:
        print("No existe esa opcion")
    except ValueError:
        print("Debe ingresar un numero")
print(f"Total a pagar: {total}")
"""

#SEMANA 7: SE HACEN EN GOOGLE COLLAB (Esta en carpeta semana 7)
import pandas as pd
peliculas = {'nombre': ['Titanic', 'Kil Bill', 'Matrix', 'El padrino', 'Avatar',
                        'Casablanca', 'El exorcista',  'Soy leyenda',
                        'El club de la pelea', 'Mujercitas'],
            'director': ['James Cameron', 'Quentin Tarantino', 'Hermanas Wachowski',
                        'Francis Ford Coppola', 'James Cameron', 'Michael Curtiz',
                        'William Friedkin', 'Francis Lawrence','David Fincher',
                        'Greta Gerwig'],
            'año': [1997, 2003, 1999, 1972, 2009, 1942, 1973, 2007, 1999, 2019],
            'género': ['romance', 'acción', 'ciencia ficción', 'drama', 'ciencia ficción', 'drama', 'terror',
                        'ciencia ficción', 'drama', 'drama'],
            'puntaje': [8.6, None, 6.9, 7.5, 9.1, 6.0, None, None, 9.4, 8.0]}

#SEMANA 8: