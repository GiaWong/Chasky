#  Chasky - Esteganografía LSB en Imágenes

**Chasky** es una herramienta educativa en Python que demuestra cómo ocultar un mensaje de texto dentro de una imagen usando **LSB** (*Least Significant Bit*, bit menos significativo). El programa incrusta el mensaje en los canales RGB y permite recuperarlo después.

El proyecto sirve para aprender sobre esteganografía y procesamiento de imágenes. Ocultar un mensaje no lo cifra: no uses esta herramienta para proteger información sensible ni para fines no autorizados.

##  Características

- Interfaz gráfica con Tkinter para ocultar y extraer mensajes.
- Interfaz de línea de comandos (CLI).
- Lee archivos de texto UTF-8 e incrusta su contenido en imágenes.
- Guarda la imagen resultante como PNG, un formato sin pérdida adecuado para conservar los bits modificados.

---

##  Instalación y configuración

Realiza estos pasos desde una terminal.

### 1. Requisitos previos

- Python **3.10 o superior**. El proyecto se ha desarrollado y verificado con Python 3.10.12; `requirements.txt` fija las versiones de las dependencias de Python.
- Git, para clonar el repositorio.
- Tkinter para usar la interfaz gráfica. Suele venir con Python; en algunas distribuciones de Linux se instala por separado (por ejemplo, el paquete `python3-tk`).

Comprueba que Python y Git estén disponibles:

```bash
python3 --version
git --version
```

En Windows, puede que debas usar `python` en lugar de `python3`.

### 2. Clonar el repositorio

```bash
git clone https://github.com/GiaWong/Chasky.git
cd Chasky
```

### 3. Crear y activar el entorno virtual

**Linux / macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (CMD o PowerShell):**

```powershell
python -m venv venv
venv\Scripts\activate
```

Cuando el entorno esté activo, el prompt de la terminal normalmente mostrará `(venv)`.

### 4. Instalar dependencias

Con el entorno virtual activo, instala las versiones indicadas en `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

No se recomienda sustituir este paso por instalaciones manuales: el archivo de requisitos fija las versiones para que las instalaciones sean consistentes. El directorio `venv/` es local y no se sube a GitHub.

---

##  Cómo usar Chasky

Ejecuta los comandos desde la raíz del repositorio, con el entorno virtual activado.

### Modo gráfico (GUI)

```bash
python3 src/gui.py
```

En Windows:

```powershell
python src\gui.py
```

Se abrirá una ventana con dos secciones:

1. **Ocultar Mensaje en Imagen:** selecciona una imagen PNG original, selecciona el archivo `.txt` con el mensaje y pulsa **“Ocultar y Guardar como...”**. Elige la ruta de salida y guarda el resultado como PNG.
2. **Extraer Mensaje de Imagen:** selecciona la imagen PNG resultante (la que contiene el mensaje oculto) y pulsa **“Extraer Mensaje”**. El mensaje aparecerá en el área **“Mensaje Extraído”**.

#### Prueba con los archivos de ejemplo

En la primera sección, selecciona:

- Imagen: `example/mascota.png`.
- Texto: `example/textoDePrueba.txt`.

Guarda el resultado, por ejemplo, como `salida.png`. Para comprobarlo, selecciona `salida.png` en la sección de extracción y pulsa **“Extraer Mensaje”**. No selecciones la imagen original para extraer: debes usar el PNG que generó Chasky.

### Modo terminal (CLI)

**Ocultar un mensaje escrito directamente en la terminal:**

```bash
python3 src/stego.py embed example/mascota.png "Tu mensaje secreto aquí" salida.png
```

**Extraer el mensaje:**

```bash
python3 src/stego.py extract salida.png
```

La ruta de salida puede cambiarse. Para conservar el mensaje, debe seguir siendo un PNG sin recomprimir.

---

##  Cómo funciona

1. El texto se codifica como UTF-8 y se antepone una cabecera de 4 bytes que indica su longitud.
2. Los bits de la cabecera y del texto se escriben, en orden, en el bit menos significativo de los canales rojo, verde y azul de los píxeles.
3. La extracción lee la cabecera y recupera la cantidad de bytes indicada.

Se utilizan hasta 3 bits por píxel y 32 bits se reservan para la cabecera. Si el mensaje no cabe en la imagen, el programa devuelve un error.

##  Estructura del proyecto

```text
Chasky/
├── example/
│   ├── mascota.png          # Imagen original de ejemplo
│   └── textoDePrueba.txt    # Mensaje de ejemplo
├── src/
│   ├── stego.py             # Funciones LSB y comandos CLI
│   ├── gui.py               # Aplicación y eventos de la interfaz
│   ├── gui_views.py         # Construcción de widgets
│   └── gui_operations.py    # Operaciones de archivos y esteganografía
├── requirements.txt         # Dependencias con versiones fijadas
├── .gitignore               # Archivos locales excluidos de Git
├── LICENSE
└── README.md
```

##  Advertencias

- Usa imágenes PNG al guardar el resultado. JPEG y otros formatos con pérdida pueden alterar los bits y destruir el mensaje.
- La esteganografía **no es cifrado**: el contenido oculto no queda protegido criptográficamente.
- `salida.png` es un archivo generado y se puede volver a crear con los pasos anteriores; no hace falta subirlo al repositorio.
- Usa la herramienta únicamente con imágenes y mensajes que tengas autorización para procesar.

##  Fuentes

- [Pillow](https://python-pillow.org/): procesamiento de imágenes.
- [Tkinter](https://docs.python.org/3/library/tkinter.html): interfaz gráfica incluida con Python en muchas distribuciones.
