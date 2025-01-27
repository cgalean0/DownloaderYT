import os
from yt_dlp import YoutubeDL

def download_audio(url, output_path="musics"):
    try:
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        options = {
            'format': 'bestaudio/best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with YoutubeDL(options) as ydl:
            print("Descargando...")
            ydl.download([url])
            print(f"Descarga completa. Archivos guardados en {output_path}")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

def process_list(file_path, output_path="musics"):
    #Procesa un archivo con multiples urls
    try:
        with open(file_path, "r") as file:
            urls = file.readlines()
            for url in urls:
                url = url.strip()
                if url:
                    download_audio(url, output_path)
    except FileNotFoundError:
        print(f"El archivo '{file_path}' no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


if __name__ == "__main__":
    print("=== Youtube to mp3 Downloader ===")
    resp = input("1. Descargar una canción\n2. Descargar lista\nInserta tu respuesta: ")
    if resp == "1":
        video_url = input("Inserta la url del video: ")
        download_audio(video_url)
    elif resp == "2":
        file_path = input("Inserta la ruta del archivo con la lista de urls: ")
        process_list(file_path)
    else:
        print("Inserta una opción válida")
