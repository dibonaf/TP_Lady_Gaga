from playlist_lady_gaga import *

def obtener_titulo(tema: str) -> str:
    if " - " in tema:
        titulo = tema.split(" - ", 1)[1]
    else:
        titulo = tema
    return titulo


def obtener_colaboradores(tema: str) -> list:
    if " - " in tema:
        parte_colab = tema.split(" - ", 1)[0]
        lista = parte_colab.split("|")
        colaboradores = []
        for colab in lista:
            colaboradores.append(colab.strip())
    else:
        colaboradores = []
    return colaboradores


def normalizar_vistas(vistas: str) -> int:
    '''
Convertimos el texto a un numero entero.
    '''    
    texto = str(vistas).lower()  # Convertimos a string para evitar errores
    texto = texto.replace("millones", "")
    texto = texto.strip()
    cantidad = int(float(texto) * 1_000_000)
    return cantidad

def normalizar_duracion(duracion: str) -> int:
    partes = duracion.split(":")
    minutos = int(partes[0])
    segundos = int(partes[1])
    total_segundos = minutos * 60 + segundos
    return total_segundos


def obtener_link(link: str) -> str:
    '''
Elimina espacios innecesarios al inicio o final del link.
    '''
    enlace = link.strip()
    return enlace


def normalizar_fecha(fecha: str) -> str:
    '''
Cambia de formato la fecha, por la tradicional que utilizamos en Argentina
    '''
    partes = fecha.strip().split("-")  
    año = partes[0]
    mes = partes[1]
    dia = partes[2]
    fecha_formateada = f"{dia}/{mes}/{año}"
    return fecha_formateada

def normalizar_toda_playlist(playlist):
    playlist_normalizada = []

    for video in playlist:
        titulo = obtener_titulo(video["Tema"])
        colaboradores = obtener_colaboradores(video["Tema"])
        vistas = normalizar_vistas(video["Vistas"])
        duracion = normalizar_duracion(video["Duracion"])
        link = obtener_link(video["Link Youtube"])
        fecha = normalizar_fecha(video["Fecha lanzamiento"])

        video_normalizado = {
            "Título": titulo,
            "Colaboradores": colaboradores,
            "Vistas": vistas,
            "Duración": duracion,
            "Link": link,
            "Fecha lanzamiento": fecha  
        }
        playlist_normalizada.append(video_normalizado)
        
    return playlist_normalizada