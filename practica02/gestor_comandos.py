import datetime

def analizar_comando(entrada_usuario):
    """
    Segunda fase del agente: Procesamiento de comandos y lógica dinamica.
    Aquí el alumno aprende a separar la 'accion' de los 'datos'.
    """
    mensaje = entrada_usuario.lower().strip()
    
    # Simulacion de comandos prefijados
    if mensaje.startswith("!recordar"):
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


def buscar_en_diccionario():


def validar_variable():
    

