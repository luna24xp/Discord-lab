import datetime

def analizar_comando(entrada_usuario):
    """
    Segunda fase del agente: Procesamiento de comandos y lógica dinamica.
    Aquí el alumno aprende a separar la 'accion' de los 'datos'.
    """
    mensaje = entrada_usuario.lower().strip()
    
    # Simulacion de comandos prefijados
    if mensaje.startswith("!"):
        partes = mensaje.split(" ", 1)
        comando = partes[0]
        argumento = partes[1] if len(partes) > 1 else ""
        
        # Logica de comando
        if comando == "!definir":
            return buscar_en_diccionario(argumento)
        elif comando == "!validar":
            return validar_variable(argumento)
        elif comando == "!hora":
            ahora = datetime.datetime.now().strftime("%H:%M:%S")
            return f"La hora actual del servidro es: {ahora}"
        elif comando == "!ayuda":
            return (" **Comandos disponibles:**\n"
                    "1. !definir [termino] - Busca la definición de una palabra.\n"
                    "2. !validar [nombre] - Valida el valor de una variable.\n"
                    "3. !hora - Muestra la hora actual del servidor.\n")
        else:
            return f" El comando '{comando}' no es reconocido. Escribe '!ayuda' para ver los comandos disponibles."
    
    return " Recuerda usar el prefijo '!' para los comandos. Escribe '!ayuda' para ver los comandos disponibles."

def buscar_en_diccionario(termino):
    if not termino:
        return "Debes escribir qué termino quieres definir. Ejemplo: '!definir list'"
    
    # Base de datos simplificada (puedes reutilizar la de la practica anterior)
    conocimientos = {
        "variable": "Una variable es un espacio en memoria que puede contener un valor.",
        "lista": "Una lista es una colección ordenada y mutable de elementos.",
        "tupla": "Una tupla es una colección ordenada e inmutable de elementos.",
    }
    return conocimientos.get(termino, f"No tengo la definición de '{termino}'.")

def validar_variable(nombre):
    """
    Lógica pedagogica: Enseña a los alumnos las reglas de nombrado en Python.
    """
    
    if not nombre:
        return " Indica el nombre a validar. Ejemplo: '!validar mi_variable'"
    
    # Reglas basicas de python
    if nombre [0].isdigit():
        return f" '{nombre}' no es un nombre válido: no puede comenzar con un número!."
    if " " in nombre:
        return f" '{nombre}' no es un nombre válido: no puede contener espacios!."
    if not nombre.isidentifier():
        return f" '{nombre}' contiene caracteeres no permitidos (solo letras, numeros y guion bajo)."
    
    return f" '{nombre}' es un nombre de variable válido!"

# Simulacion de ejecucion
if __name__ == "__main__":
    print("--- Agente de Lógica: Fase de Comandos ---")
    print("Prueba comandos como: !validar 123hola o !definir lista\n")

    while True:
        user_input = input("Alumno >> ")
        if user_input.lower() in ["salir", "exit"]: break

        respuesta = analizar_comando(user_input)
        print(f"Bot >> {respuesta}\n")

