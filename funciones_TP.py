from validaciones import *
from playlist_lady_gaga import *

def mostrar_menu(opciones) -> None:
    '''
    Es la funcion que me permite realizar un menu de opciones.
    '''
    print(opciones)
    opcion = int(input("Ingrese una opción: "))
    return opcion

def mostrar_lista_temas(playlist: list) -> list:
    lista_resultado = []

    # Calcular anchos máximos para alineación dinámica
    max_titulo = max(len(video["Título"]) for video in playlist)
    max_colab = max(len(", ".join(video["Colaboradores"])) if video["Colaboradores"] else 3 for video in playlist)

    print(f"{'Título':{max_titulo}} | {'Colaboradores':{max_colab}} | {'Duración':>8}")
    print("-" * (max_titulo + max_colab + 15))

    for video in playlist:
        titulo = video["Título"]
        colaboradores = ", ".join(video["Colaboradores"]) if video["Colaboradores"] else "—"
        duracion_segundos = video["Duración"]
        minutos = duracion_segundos // 60
        segundos = duracion_segundos % 60
        duracion_formateada = f"{minutos}:{segundos:02d}"

        print(f"{titulo:{max_titulo}} | {colaboradores:{max_colab}} | {duracion_formateada:>8}")
        lista_resultado.append((titulo, colaboradores, duracion_formateada))

    return lista_resultado

def obtener_duracion(video):
    '''
    Recibe un video (diccionario) y devuelve su duración en segundos.
    '''
    return video["Duración"]

def ordenar_temas_por_duracion(playlist):
    '''
    Ordena la lista de videos por duración de mayor a menor.
    '''
    playlist.sort(key=obtener_duracion, reverse=True)
    return playlist

def promedio_vistas_millones(playlist):
    '''
    Calcula el promedio de vistas de todos los videos en millones.
    '''
    total_vistas = 0
    cantidad_videos = len(playlist)
    for video in playlist:
        total_vistas += video["Vistas"]
    promedio = total_vistas / cantidad_videos / 1_000_000
    return promedio

def videos_maxima_reproduccion(playlist):
    '''
Devuelve una lista con el o los videos que tienen la mayor cantidad de vistas.
Usa normalizar_vistas para comparar la cantidad de vistas de cada video.
    '''
    vistas_normalizadas = []
    
    for video in playlist:
        vistas_normalizadas.append(normalizar_vistas(video["Vistas"]))

    max_vistas = max(vistas_normalizadas)

    resultados = []
    for video in playlist:
        if normalizar_vistas(video["Vistas"]) == max_vistas:
            resultados.append(video)

    return resultados

def videos_minima_reprduccion (playlist):
    '''
Devuelve una lista con el o los videos que tienen la menor cantidad de vistas.
Usa normalizar_vistas para comparar la cantidad de vistas de cada video.
    '''
    vistas_normalizadas = []
    
    for video in playlist:
        vistas_normalizadas.append(normalizar_vistas(video["Vistas"]))

    min_vistas = min(vistas_normalizadas)

    resultados = []
    for video in playlist:
        if normalizar_vistas(video["Vistas"]) == min_vistas:
            resultados.append(video)

    return resultados

def buscar_por_codigo(playlist: list, codigo: str) -> dict:
    '''
    Busca un video en la playlist por su código de YouTube,
    imprime todos los datos del video encontrado de forma alineada,
    y devuelve el diccionario del video.
    '''
    resultado = None

    for video in playlist:
        enlace = video["Link"]      
        if codigo in enlace:
            colaboradores = video["Colaboradores"]            
            if len(colaboradores) == 0:
                video["Colaboradores"] = "-"            
            else:
                colaboradores_str = ""                
                for i in range(len(colaboradores)):
                    colaboradores_str += colaboradores[i]                    
                    if i < len(colaboradores) - 1:
                        colaboradores_str += ", "
                video["Colaboradores"] = colaboradores_str            
            resultado = video
            break
    return resultado


def listar_por_mes(playlist: list, mes: int) -> list:
    '''
    Devuelve una lista de videos lanzados en el mes ingresado (1 a 12).
    '''
    resultados = []
    for video in playlist:
        fecha = video["Fecha lanzamiento"].strip()
        partes = fecha.split("/")
        mes_video = int(partes[1])
        if mes_video == mes:
            resultados.append(video)
    return resultados
