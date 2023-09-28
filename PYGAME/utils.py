def formatear_puntaje(puntaje: str) -> str:
    return str(puntaje.zfill(5))

def formatear_nombre_jugador(nombre: str) -> str:
    return nombre.strip().split(' ')[0].upper()

def ordenar_puntajes(lista_puntajes: list[dict]):
    lista_puntajes_ordenada = sorted(lista_puntajes, key = lambda puntaje: puntaje['puntaje'], reverse = True)
    lista_puntajes.sort(key = lambda puntaje: puntaje['puntaje'], reverse = True)
    return lista_puntajes_ordenada 



# def formatear_puntaje(puntaje: str) -> str:
#     puntaje = puntaje.zfill(5)
#     return puntaje

# def formatear_nombre_jugador(nombre: str) -> str:
#     nombre = nombre.strip().upper()
#     return nombre