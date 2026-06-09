import discord
import os
import re
from dotenv import load_dotenv

from practica01.gestor_comandos import analizar_comando, buscar_en_diccionario, validar_variable
tareas = []  # Nuestra "base de datos" en memoria (lista)

def agregar_tarea(lista_tareas, descripcion):
    """
    Agrega una tarea a la lista si cumple con los requisitos.
    Recibe la lista (paso por referencia) y la cadena de descripción.
    """
    if len(descripcion) < 3:
        return " Error: La descripción es muy corta (mínimo 3 caracteres)."
    
    # Creamos un formato de cadena simple para la tarea
    lista_tareas.append(descripcion)
    return f" Tarea añadida con éxito."
def mostrar_bienvenida():
    """Retorna la lista de comandos disponibles."""
    return (
        "📜 Bot gestor (Modo Estructurado):\n"
        "📜 Primeros pasos Agente Discord UX:\n"
        "📜 Escriba !Exit para salir del Agente:"
        "📜 Escriba !buscar para buscar tareas:\n"
        "📜 Escriba !validar para validar tareas:\n"
        
    )

def main(entrada):
        tareas = []  # Nuestra "base de datos" en memoria (lista)

    
        PREFIJO = "!"
        
        if not entrada.startswith(PREFIJO):
            if entrada: print("Recuerda usar '!' para comandos.")
            
        # Procesamiento de la entrada
        cuerpo = entrada[len(PREFIJO):].split(maxsplit=1)
        comando = cuerpo[0].lower()
        argumento = cuerpo[1] if len(cuerpo) > 1 else ""
        
        # Selección de acción (Estructura de control)
        if comando == "exit":
            print("Saliendo del gestor...")
            return "Saliendo del gestor..."
                        
        elif comando == "inicio":
            print(mostrar_bienvenida())
            return mostrar_bienvenida()
        
        elif comando == "buscar":
            return buscar_en_diccionario(argumento)
        
        elif comando == "validar":
            return validar_variable(argumento)
        
        elif comando == "add":
            resultado = agregar_tarea(tareas, argumento)
            print(resultado)
            return resultado
            
            
        else:
            print(f" Error: Comando '!{comando}' no reconocido.")
            return f" Error: Comando '!{comando}' no reconocido."
        
        print("-" * 20)


# --- CONFIGURACIÓN DE DISCORD ---

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Definir los "intents" (permisos) necesarios
intents = discord.Intents.default()
intents.message_content = True  # Necesario para leer el contenido de los mensajes

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Sincronizado como {client.user} (ID: {client.user.id})')
    print('------')

@client.event
async def on_message(message):
    # Evitar que el bot se responda a sí mismo
    if message.author == client.user:
        return
    
    # 3. Procesamiento: Pasamos el contenido del mensaje a nuestra lógica
    print(f"Mensaje recibido de {message.author}: {message.content}")

    # Solo procesamos si el mensaje empieza con un prefijo (opcional, pero recomendado)
    if message.content.startswith('!'):
        resultado = main(message.content)

        print(f"Resultado del procesamiento: {resultado}")
        
        # 4. Respuesta: El bot escribe el resultado en el mismo canal
        await message.channel.send(f" **Bot Procesador:** {resultado}")
    
# Ejecutar el bot
if __name__ == "__main__":
    if TOKEN:
        client.run(TOKEN)
    else:
        print("ERROR: No se encontró el TOKEN en el archivo .env")