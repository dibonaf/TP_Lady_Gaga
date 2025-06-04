from playlist_lady_gaga import *
from funciones_TP import *
from validaciones import *

datos_cargados = False

while True:
    opcion = mostrar_menu( "\nMENÚ DE OPCIONES" "\n1 – Normalización de Datos" "\n2 – Mostrar Lista de Temas" "\n3 – Ordenar Temas por Duración" "\n4 – Promedio de Vistas" "\n5 – Máxima Reproducción" "\n6 – Mínima Reproducción" "\n7 – Búsqueda por Código" "\n8 – Listar por Colaborador" "\n9 – Listar por Mes de Lanzamiento" "\n10 – Salir")

    match opcion:
        case 1:
            playlist_lady_gaga = normalizar_toda_playlist(playlist_lady_gaga)
            datos_cargados = True
            print("Datos normalizados y cargados exitosamente.")

        case 2:
            if datos_cargados:
                mostrar_lista_temas(playlist_lady_gaga)
            else:
                print("Debe normalizar y cargar los datos primero (opción 1).")

        case 3:
            if datos_cargados:
                ordenar_temas_por_duracion(playlist_lady_gaga)
                mostrar_lista_temas(playlist_lady_gaga)
            else:
                print("Debe normalizar y cargar los datos primero (opción 1).")

        case 4:
            if datos_cargados:
                promedio = promedio_vistas_millones(playlist_lady_gaga)
                print(f"Promedio de vistas: {promedio:.2f} millones")
            else:
                print("Debe normalizar y cargar los datos primero (opción 1).")

        case 5:
            if datos_cargados:
                max_videos = videos_maxima_reproduccion(playlist_lady_gaga)
                print("Video(s) con máxima reproducción:")
                for v in max_videos:
                    print(f"{v['Título']} - {v['Vistas']} vistas")
            else:
                print("Debe normalizar y cargar los datos primero (opción 1).")

        case 6:
            if datos_cargados:
                min_videos = videos_minima_reprduccion(playlist_lady_gaga)
                print("Video(s) con mínima reproducción:")
                for v in min_videos:
                    print(f"{v['Título']} - {v['Vistas']} vistas")
            else:
                print("Debe normalizar y cargar los datos primero (opción 1).")

        case 7:
            if datos_cargados:
                codigo = input("Ingrese código de video: ").strip()
                resultado = buscar_por_codigo(playlist_lady_gaga, codigo)
                if resultado:
                    print("Detalles del video encontrado:")
                    for clave, valor in resultado.items():
                        print(f"{clave}: {valor}")
                else:
                    print("No se encontró ningún video con ese código.")
            else:
                print("Debe normalizar y cargar los datos primero (opción 1).")

        case 8:
            if datos_cargados:
                colaborador = input("Ingrese nombre del colaborador: ").strip()
                encontrados = []
                for video in playlist_lady_gaga:
                    if colaborador in video["Colaboradores"]:
                        encontrados.append(video)
                if encontrados:
                    mostrar_lista_temas(encontrados)
                else:
                    print("No se encontraron videos con ese colaborador.")
            else:
                print("Debe normalizar y cargar los datos primero (opción 1).")

        case 9:
            if datos_cargados:
                entrada = input("Ingrese número de mes (1-12): ").strip()
                meses_validos = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
                if entrada in meses_validos:
                    mes = int(entrada)
                    resultados = listar_por_mes(playlist_lady_gaga, mes)
                    if resultados:
                        mostrar_lista_temas(resultados)
                    else:
                        print("No hay videos para ese mes.")
                else:
                    print("Entrada inválida. Ingrese un número entre 1 y 12.")
            else:
                print("Debe normalizar y cargar los datos primero (opción 1).")

        case 10:
            print("Fin del programa.")
            break

        case _:
            print("Opción no válida.")