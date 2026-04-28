import datetime

def obtener_saludo(nombre_bot):
    """
    Retorna un saludo formateado
    """
    return f"¡Hola! Soy {nombre_bot} y estoy listo para ayudarte."
    
def procesar_comando_recordar(comando):
    """
    Valida y procesa la accion de recirdar un dato
    """
    if not comando:
        return"Error: falta el nombre. Uso !recordar [nombre]"
    return f"¡He recordado el nombre '{comando}'"

def calcular_uptime(hora_inicio):
    """
    Calcula la diferencia de tiempo entre el inicio
    y el actual (mostrar actividad del bot)
    """
    ahora = datetime.datetime.now()
    diferencia = ahora - hora_inicio
    segundos = int(diferencia.total_seconds())
    return f"Tiempo de actividad: {diferencia}"

def mostrar_ayuda():
    
    
def iniciar_agente():



def main():
    obtener_saludo("AgenteBot")
    
    
    hora_inicio = datetime.datetime.now()
    
    while True:
        comando = input("Ingrese un comando: ")
        
        if comando.startswith("recordar "):
            argumento = comando[len("recordar "):]
            print(procesar_comando_recordar(argumento))
        elif comando == "uptime":
            print(calcular_uptime(hora_inicio))
        elif comando == "ayuda":
            mostrar_ayuda()
        elif comando == "salir":
            print("¡Hasta luego!")
            break
        else:
            print("Comando no reconocido. Escriba 'ayuda' para ver los comandos disponibles.")

if __name__ == "__main__":
    main()