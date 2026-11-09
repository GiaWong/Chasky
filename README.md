# Chasky

Proyecto de esteganografía que oculta un mensaje de texto dentro de una imagen mediante **LSB** (*least significant bit*, bit menos significativo) en los canales RGB. El programa permite incrustar un mensaje y luego extraerlo.

## Requisitos

- Python **3.10.12** (versión del entorno local del proyecto).
- `pip`.

Las dependencias, incluidas sus versiones, están fijadas en `requirements.txt`. Desde la raíz del repositorio, crea un entorno virtual e instala esas versiones:

```bash
python3.10 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

En Windows, activa el entorno con `venv\Scripts\activate` en lugar de `source venv/bin/activate`. No se debe subir el directorio `venv/`: cada persona lo crea localmente a partir de `requirements.txt`.

## Uso

Ejecuta los comandos desde la raíz del repositorio.

### Interfaz gráfica

```bash
python src/gui.py
```

La interfaz permite seleccionar una imagen PNG y un archivo `.txt` para ocultar el texto, o seleccionar una imagen con un mensaje para extraerlo. Tkinter viene con Python en la mayoría de las instalaciones; en Linux puede ser necesario instalar el paquete del sistema `python3-tk`.

### Ocultar un mensaje

```bash
python src/stego.py embed example/mascota.png "Mensaje de prueba" salida.png
```

El programa guarda la imagen resultante en `salida.png` y muestra su ruta.

### Extraer el mensaje

```bash
python src/stego.py extract salida.png
```

El texto extraído se imprime en la terminal. También se puede reemplazar `salida.png` por la ruta de otra imagen que contenga un mensaje.

## Cómo funciona

- El texto se convierte a UTF-8 y se antepone una cabecera de 4 bytes con su longitud.
- Los bits de la cabecera y el texto se escriben, en orden, en el bit menos significativo de los canales rojo, verde y azul de cada píxel.
- La imagen resultante se guarda como PNG; la extracción lee primero la cabecera para conocer cuántos bytes recuperar.

La capacidad depende de la imagen: se usan 3 bits por píxel y 32 bits se reservan para la cabecera. Los mensajes demasiado grandes producen un error.

## Estructura

```text
.
├── example/
│   └── mascota.png    # Imagen de entrada para probar el programa
├── src/
│   ├── stego.py       # Implementación y comandos embed/extract
│   ├── gui.py         # Aplicación y control de eventos de la interfaz
│   ├── gui_views.py   # Construcción de widgets
│   └── gui_operations.py  # Operaciones de lectura, ocultación y extracción
├── requirements.txt   # Dependencias con versiones fijadas
├── LICENSE
├── .gitignore
└── README.md
```

## Notas

- Usa PNG u otro formato sin pérdida para conservar los bits; recomprimir o convertir la imagen a JPEG puede corromper el mensaje.
- Este mecanismo oculta datos, pero **no los cifra**. No debe usarse como sustituto de cifrado ni para proteger información sensible.
- `salida.png` es un archivo generado por el ejemplo y se puede volver a crear siguiendo los comandos anteriores.
