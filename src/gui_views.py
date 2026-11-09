"""Construcción de los widgets de la interfaz gráfica de Chasky."""

import tkinter as tk
from dataclasses import dataclass
from typing import Callable


@dataclass
class GuiWidgets:
    image_path: tk.StringVar
    txt_path: tk.StringVar
    stego_image_path: tk.StringVar
    result_text: tk.Text


def create_widgets(
    root: tk.Tk,
    *,
    load_image: Callable[[], None],
    load_text: Callable[[], None],
    embed_message: Callable[[], None],
    load_stego_image: Callable[[], None],
    extract_message: Callable[[], None],
) -> GuiWidgets:
    # Variables para guardar las rutas de los archivos
    image_path = tk.StringVar(master=root)
    txt_path = tk.StringVar(master=root)
    stego_image_path = tk.StringVar(master=root)

    # --- SECCIÓN: OCULTAR MENSAJE ---
    frame_embed = tk.LabelFrame(root, text="1. Ocultar Mensaje en Imagen", padx=10, pady=10)
    frame_embed.pack(padx=10, pady=10, fill="x")

    # Seleccionar Imagen Original
    tk.Button(frame_embed, text="Cargar Imagen (.png)", command=load_image).grid(row=0, column=0, pady=5, sticky="w")
    tk.Label(frame_embed, textvariable=image_path, fg="blue", wraplength=300).grid(row=0, column=1, padx=5)

    # Seleccionar Archivo de Texto
    tk.Button(frame_embed, text="Cargar Mensaje (.txt)", command=load_text).grid(row=1, column=0, pady=5, sticky="w")
    tk.Label(frame_embed, textvariable=txt_path, fg="blue", wraplength=300).grid(row=1, column=1, padx=5)

    # Botón para ejecutar la ocultación
    tk.Button(
        frame_embed,
        text="Ocultar y Guardar como...",
        bg="#4CAF50",
        fg="white",
        command=embed_message,
    ).grid(row=2, column=0, columnspan=2, pady=15)

    # --- SECCIÓN: EXTRAER MENSAJE ---
    frame_extract = tk.LabelFrame(root, text="2. Extraer Mensaje de Imagen", padx=10, pady=10)
    frame_extract.pack(padx=10, pady=10, fill="x")

    # Seleccionar Imagen Modificada
    tk.Button(frame_extract, text="Cargar Imagen con Secreto", command=load_stego_image).grid(row=0, column=0, pady=5, sticky="w")
    tk.Label(frame_extract, textvariable=stego_image_path, fg="blue", wraplength=300).grid(row=0, column=1, padx=5)

    # Botón para extraer
    tk.Button(
        frame_extract,
        text="Extraer Mensaje",
        bg="#2196F3",
        fg="white",
        command=extract_message,
    ).grid(row=1, column=0, columnspan=2, pady=15)

    # --- ÁREA DE TEXTO PARA MOSTRAR EL MENSAJE ---
    tk.Label(root, text="Mensaje Extraído:").pack(anchor="w", padx=10)
    result_text = tk.Text(root, height=5, width=60)
    result_text.pack(padx=10, pady=5)

    return GuiWidgets(
        image_path=image_path,
        txt_path=txt_path,
        stego_image_path=stego_image_path,
        result_text=result_text,
    )