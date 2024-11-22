# hackaton2024.py
def saludo():
    print("¡Hola! Bienvenido al bot de saludo.")
    nombre = input("¿Cuál es tu nombre? ")
    mensaje_bienvenida = f"¡Hola, {nombre}! Encantado de conocerte."
    color_favorito = input("¿Te gustaría decirme tu color favorito? (sí/no) ").strip().lower()
    if color_favorito == 'sí':
        color = input("¿Cuál es tu color favorito? ")
        mensaje_bienvenida += f" Me gusta el color {color} también."
    print(mensaje_bienvenida)
if _name_ == "_main_":
    saludo()



#2
def contar_palabras(texto, excluir=None):
    texto = texto.lower()
    for caracter in [",", ".", "!", "?", ";", ":", "-", "_", "(", ")", "[", "]", "{", "}", "\"", "'"]:
        texto = texto.replace(caracter, " ")
    palabras = texto.split()
    contador = {}
    for palabra in palabras:
        if excluir and palabra in excluir:
            continue
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
    return contador
def main():
    texto = input("Por favor, ingresa un bloque de texto:\n")
    excluir_opcion = input("¿Deseas excluir palabras comunes? (sí/no): ").strip().lower()
    palabras_excluir = []
    if excluir_opcion == 'sí':
        palabras_excluir = ["el", "la", "y", "de", "que", "a", "en", "un", "ser", "con", "no", "por", "una", "su", "al", "lo", "como", "más", "o", "pero", "para", "está", "esto", "si", "me", "te", "se", "es", "del", "las", "los", "todo", "toda", "entre", "ya", "muy", "también", "cuando", "todo", "cual", "donde"]
    resultado = contar_palabras(texto, excluir=palabras_excluir)
    print("\nContador de palabras:")
    for palabra, cantidad in resultado.items():
        print(f"{palabra}: {cantidad}")
if _name_ == "_main_":
    main()



#3
import random
def lanzar_dados(cantidad_dados):
    resultados = []
    for _ in range(cantidad_dados):
        resultado = random.randint(1, 6)
        resultados.append(resultado)
        print(f"Lanzamiento: {resultado}")
    return resultados
def main():
    while True:
        try:
            cantidad_dados = int(input("¿Cuántos dados quieres lanzar? (1-10): "))
            if cantidad_dados < 1 or cantidad_dados > 10:
                print("Por favor, elige un número entre 1 y 10.")
                continue
            break
        except ValueError:
            print("Por favor, introduce un número válido.")
    resultados = lanzar_dados(cantidad_dados)
    suma_total = sum(resultados)
    print(f"\nResultados de los lanzamientos: {resultados}")
    print(f"Suma total: {suma_total}")
if _name_ == "_main_":
    main()




#4
import random
import string
def generar_contrasena(longitud):
    letras = string.ascii_letters  
    numeros = string.digits  
    simbolos = string.punctuation  
    todos_los_caracteres = letras + numeros + simbolos
    contrasena = ''.join(random.choice(todos_los_caracteres) for _ in range(longitud))
    return contrasena
def main():
    while True:
        try:
            longitud = int(input("Introduce la longitud de la contraseña (mínimo 8): "))
            if longitud < 8:
                print("La contraseña debe tener al menos 8 caracteres.")
                continue
            break
        except ValueError:
            print("Por favor, introduce un número válido.")
    contrasena = generar_contrasena(longitud)
    print(f"\nContraseña generada: {contrasena}")
if _name_ == "_main_":
    main()



#5
import random
def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False
    print("¡Bienvenido al juego 'Adivina el número'!")
    print("He elegido un número entre 1 y 100. ¡Intenta adivinarlo!")
    while not adivinado:
        try:
            guess = int(input("Introduce tu número: "))
            intentos += 1
            if guess < 1 or guess > 100:
                print("Por favor, elige un número entre 1 y 100.")
            elif guess < numero_secreto:
                print("Demasiado bajo. Intenta de nuevo.")
            elif guess > numero_secreto:
                print("Demasiado alto. Intenta de nuevo.")
            else:
                adivinado = True
                print(f"¡Felicidades! Has adivinado el número {numero_secreto} en {intentos} intentos.")
        except ValueError:
            print("Por favor, introduce un número válido.")
def main():
    while True:
        adivina_el_numero()
        reiniciar = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if reiniciar != 's':
            print("Gracias por jugar. ¡Hasta luego!")
            break
if _name_ == "_main_":
    main()



#6
def obtener_lista_compras():
    lista_compras = []
    while True:
        producto = input("Introduce el nombre del producto (o 'fin' para terminar): ")
        if producto.lower() == 'fin':
            break
        try:
            precio = float(input(f"Introduce el precio de {producto}: "))
            lista_compras.append({'nombre': producto, 'precio': precio})
        except ValueError:
            print("Por favor, introduce un precio válido.")
    return lista_compras
def calcular_total(lista_compras):
    total = sum(item['precio'] for item in lista_compras)
    return total
def aplicar_descuento(total, umbral, descuento):
    if total > umbral:
        total -= descuento
        print(f"Se ha aplicado un descuento de {descuento}.")
    return total
def mostrar_lista(lista_compras):
    print("\nLista de Compras:")
    for item in lista_compras:
        print(f"{item['nombre']}: ${item['precio']:.2f}")
def main():
    print("Bienvenido al ordenador de lista de compras.")
    lista_compras = obtener_lista_compras()
    lista_compras.sort(key=lambda x: x['precio'])
    mostrar_lista(lista_compras)
    total = calcular_total(lista_compras)
    print(f"\nTotal de la compra: ${total:.2f}")
    umbral_descuento = 100  
    descuento = 10
    total_final = aplicar_descuento(total, umbral_descuento, descuento)
    print(f"Total final después de aplicar descuentos (si corresponde): ${total_final:.2f}")
if _name_ == "_main_":
    main()



#7
import random
def obtener_palabras_clave():
    nombre = input("Introduce un nombre: ")
    lugar = input("Introduce un lugar: ")
    actividad = input("Introduce una actividad: ")
    return nombre, lugar, actividad
def generar_historia_aventura(nombre, lugar, actividad):
    return f"Un día, {nombre} decidió ir a {lugar} para {actividad}. En el camino, se encontró con un dragón que custodiaba un tesoro. {nombre} tuvo que usar su ingenio para superar el desafío y finalmente se convirtió en un héroe."
def generar_historia_misterio(nombre, lugar, actividad):
    return f"{nombre} estaba en {lugar} cuando escuchó un extraño sonido mientras {actividad}. Decidió investigar y descubrió un secreto oscuro que cambiaría su vida para siempre."
def generar_historia_ciencia_ficcion(nombre, lugar, actividad):
    return f"En un futuro distante, {nombre} vivía en {lugar} y pasaba su tiempo {actividad}. Un día, encontró una máquina del tiempo que lo llevó a una aventura intergaláctica."
def main():
    print("¡Bienvenido al generador de historias aleatorias!")
    nombre, lugar, actividad = obtener_palabras_clave()
    tipo_historia = random.choice(["aventura", "misterio", "ciencia ficción"])
    if tipo_historia == "aventura":
        historia = generar_historia_aventura(nombre, lugar, actividad)
    elif tipo_historia == "misterio":
        historia = generar_historia_misterio(nombre, lugar, actividad)
    else:
        historia = generar_historia_ciencia_ficcion(nombre, lugar, actividad)
    print("\nAquí está tu historia:")
    print(historia)
if _name_ == "_main_":
    main()



#8
import random
def obtener_eleccion_usuario():
    while True:
        eleccion = input("Elige 'piedra', 'papel' o 'tijeras' (o 'salir' para terminar): ").lower()
        if eleccion in ['piedra', 'papel', 'tijeras', 'salir']:
            return eleccion
        else:
            print("Opción no válida. Por favor, elige 'piedra', 'papel' o 'tijeras'.")
def obtener_eleccion_computadora():
    return random.choice(['piedra', 'papel', 'tijeras'])
def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "empate"
    elif (usuario == 'piedra' and computadora == 'tijeras') or \
         (usuario == 'papel' and computadora == 'piedra') or \
         (usuario == 'tijeras' and computadora == 'papel'):
        return "victoria"
    else:
        return "derrota"
def main():
    print("¡Bienvenido al juego de 'Piedra, Papel o Tijeras'!")
    victorias = 0
    empates = 0
    derrotas = 0
    while True:
        eleccion_usuario = obtener_eleccion_usuario()
        if eleccion_usuario == 'salir':
            break
        eleccion_computadora = obtener_eleccion_computadora()
        print(f"La computadora eligió: {eleccion_computadora}")
        resultado = determinar_ganador(eleccion_usuario, eleccion_computadora)
        if resultado == "victoria":
            print("¡Ganaste!")
            victorias += 1
        elif resultado == "empate":
            print("Es un empate.")
            empates += 1
        else:
            print("Perdiste.")
            derrotas += 1
    print("\nEstadísticas finales:")
    print(f"Victorias: {victorias}")
    print(f"Empates: {empates}")
    print(f"Derrotas: {derrotas}")
if _name_ == "_main_":
    main()



#9
def convertir_metros_a_kilometros(metros):
    return metros / 1000
def convertir_kilometros_a_metros(kilometros):
    return kilometros * 1000
def convertir_celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def convertir_fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def mostrar_menu():
    print("\n--- Conversor de Unidades ---")
    print("1. Metros a Kilómetros")
    print("2. Kilómetros a Metros")
    print("3. Celsius a Fahrenheit")
    print("4. Fahrenheit a Celsius")
    print("5. Salir")
def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")
        if opcion == '1':
            metros = float(input("Introduce la cantidad en metros: "))
            resultado = convertir_metros_a_kilometros(metros)
            print(f"{metros} metros son {resultado:.6f} kilómetros.")
        elif opcion == '2':
            kilometros = float(input("Introduce la cantidad en kilómetros: "))
            resultado = convertir_kilometros_a_metros(kilometros)
            print(f"{kilometros} kilómetros son {resultado:.6f} metros.")
        elif opcion == '3':
            celsius = float(input("Introduce la temperatura en Celsius: "))
            resultado = convertir_celsius_a_fahrenheit(celsius)
            print(f"{celsius}°C son {resultado:.2f}°F.")
        elif opcion == '4':
            fahrenheit = float(input("Introduce la temperatura en Fahrenheit: "))
            resultado = convertir_fahrenheit_a_celsius(fahrenheit)
            print(f"{fahrenheit}°F son {resultado:.2f}°C.")
        elif opcion == '5':
            print("Saliendo del conversor. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 5.")
if _name_ == "_main_":
    main()

