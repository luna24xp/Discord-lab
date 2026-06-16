import datetime

def analizar_comando(entrada_usuario):
    """
    segunda fase del Agente: procesamiento de comandos y lógica dinamica.
    Aquí el alumno aprednde a separar la 'acción' de los datos."""

    mensaje = entrada_usuario.lower().strip()

    #Simulación de comandos prefijos(como se usan en Discord !Ayuda, !Ejemlo)
    
    if mensaje.startswith("!"):
        partes = mensaje.split(" ", 1)  # Dividir en comando y argumento
        comando = partes[0]
        argumento = partes[1] if len(partes) > 1 else None

        #Logica de comandos
        if comando == "!definir":
            return buscar_en_diccionario(argumento)
        
        elif comando == "!validar":
            return validar_variable(argumento)
        
        elif comando == "!hora":
            ahora = datetime.datetime.now().strftime("%H:%M:%S")
            return f"La hora actual del servidor es: {ahora}"
        
        elif comando == "!ayuda":
            return ("Comandos disponibles:\n"
                    "!definir [termino] - Busca la definición de un término en el diccionario.\n"
                    "!validar [nombre] - Valida si un nombre de variable es correcto.\n"
                    "!hora - Muestra la hora actual del servidor.\n"
                    "!ayuda - Muestra esta ayuda.")

        else:
            return f" El comando '{comando}' no existe. Usa '!ayuda' para ver los comandos disponibles."
        
    return " Recuerda usar el prefijo '!' para darme órdenes, o pregunta algo directamente."



def buscar_en_diccionario(termino):
    if not termino:
        return "Debes escribir qué término quieres definir. Ejemplo: !definir list"

    # Base de datos simplificada (puedes reutilizar la de la practica anterior)
    conocimiento = {

        "variable": "Un espacio en memoria para almacener datos",
        "Lista": "Colección mutable de elementos",
        "Tupla": "Colección immutable de elementos (no se pueden cambiar)."

    }

    return conocimiento.get(termino, f"No encontré '{termino}' en mi base de datos.")



def validar_variable(nombre):
    """
    Lógica pedagogica: Enseña a los alumnos las reglas de nombres en python.
    """
    if not nombre:
        return "Debes escribir un nombre de variable para validar. Ejemplo: !validar mi_variable"


    #Reglas básicas de python.
    if nombre[0].isdigit():
        return f" '{nombre}' no es válido: ¡!No puede comenzar con un número!"
    if " " in nombre:
        return f" '{nombre}' no es válido: ¡!No puede contener espacios!"
    if not nombre.isidentifier():
        return f" '{nombre}' contiene caracteres no permitidos (solo letras ,números y _)"
    
    return f" '{nombre}' es un nombre de variable válido en python."

if __name__ == "__main__":
    print("--- Agente de Lógica: Fase de Comandos ---")
    print("Prueba comandos como: !validar 123hola o !definir lista\n")

    while True:
        user_input = input("Alumno >> ")
        if user_input.lower() in ["salir", "exit"]: break

        respuesta = analizar_comando(user_input)
        print(f"Bot >> {respuesta}\n")