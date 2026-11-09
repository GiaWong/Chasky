"""Operaciones de lectura y esteganografía usadas por la interfaz gráfica."""

# Importamos nuestras funciones desde stego.py
# Como gui_operations.py está en la misma carpeta (src), podemos importarlo directo
from stego import embed, extract


def embed_message_from_file(image_path: str, text_path: str, output_path: str) -> None:
    # Leer el mensaje del txt
    with open(text_path, "r", encoding="utf-8") as text_file:
        mensaje = text_file.read()

    # Llamar a nuestra función embed
    embed(image_path, mensaje, output_path)


def extract_message(image_path: str) -> str:
    # Llamar a nuestra función extract
    return extract(image_path)