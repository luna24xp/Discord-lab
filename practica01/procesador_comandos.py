def obtener_saludo(nombre_bot):
    

def procesar_comando_recordar(argumento):
    

def calcular_uptime(hora_inicio):
    

def mostrar_ayuda():
    
    
def iniciar_agente():



import datatime

def main():
    nombre_bot = "AgenteBot"
    hora_inicio = datetime.datetime.now()
    
    print(obtener_saludo(nombre_bot))
    
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