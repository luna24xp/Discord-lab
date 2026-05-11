import datetime

def agregar_tarea(lista_tareas, descripcion):
    """
    Agregar una tarea a las lista si cumpole con los requisitos
    """
    if len(descripcion) < 3:
        return "Error: La descripción de la tarea debe tener al menos 3 caracteres."
    
    # Crear formato para tarea
    fecha = datetime.datetime.now().strftime("%H:%M")
    nueva_tarea = f"{descripcion} - {fecha})"
    lista_tareas.append(nueva_tarea)
    return f"Tarea agregada con exito"

def listar_tareas(lista_tareas):
    """
    Formatea la lista de tareas para su visualizacion
    """
    if not lista_tareas:
        return "No hay tareas pendientes."
    
    #Agregar una variable llamada resultado
    resultado = "Listado de tareas: \n"
    
    #Iterar la lista de tareas y formatear la salida
    for i, tarea in enumerate(lista_tareas, start=1):
        resultado += f"{i}. {tarea}\n"

    return resultado

def eliminar_tarea(lista_tareas, indice):
    """
    Elimina una tarea de la lista segun su numero de indice
    """
    if not indice.isdigit():
        return "Error: El índice debe ser un número."
    
    indice = int(indice)-1
    
    #agregamos la logica al preguntar
    #si el elemento esta en la lista
    if 0 <= indice < len(lista_tareas):
        tarea_eliminada = lista_tareas.pop(indice)
    else: 
        return "Error: No existe la tarea."
    return f"Tarea eliminada: {tarea_eliminada}"

def main():
    tareas = []
    PREFIJO = "!"
    
    print("¡Bienvenido al gestor de tareas")
    activa = True
    while activa:
        entrada = input(">>>").strip()
        
        if not entrada.startswith(PREFIJO):
            print("Comando no reconocido.")
            continue
    
    #procesamiento de entrada
    cuerpo = entrada[len(PREFIJO):].split(maxsplit=1)
    comando = cuerpo[0].lower()
    argumento = cuerpo[1] if len(cuerpo) > 1 else ""
    
    #seleccion de accion
    if comando == "add":
        resultado = agregar_tarea(tareas, argumento)
        print