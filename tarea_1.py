def download_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        return f"Video descargado: {yt.title}"
    except Exception as e:
        return f"Error al descargar: {str(e)}"

# Ejemplo de uso
url = input("Ingresa la URL del video de YouTube: ")
result = download_video(url)
print(result)