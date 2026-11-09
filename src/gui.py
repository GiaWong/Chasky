import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox

# Arreglo para que Python encuentre stego.py cuando ejecutamos desde la raíz
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from gui_operations import embed_message_from_file, extract_message
from gui_views import GuiWidgets, create_widgets

class StegoApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Chasky - Esteganografía LSB")
        self.root.geometry("500x450")
        self.root.resizable(False, False)

        self.widgets: GuiWidgets = create_widgets(
            self.root,
            load_image=self.load_image,
            load_text=self.load_txt,
            embed_message=self.do_embed,
            load_stego_image=self.load_stego_image,
            extract_message=self.do_extract,
        )

        self.image_path = self.widgets.image_path
        self.txt_path = self.widgets.txt_path
        self.stego_image_path = self.widgets.stego_image_path
        self.result_text = self.widgets.result_text

    # --- FUNCIONES DE LOS BOTONES ---

    @staticmethod
    def _select_file(filetypes: list[tuple[str, str]]) -> str:
        return filedialog.askopenfilename(filetypes=filetypes)

    def load_image(self) -> None:
        filepath = self._select_file([("Imágenes PNG", "*.png")])
        if filepath:
            self.image_path.set(filepath)

    def load_txt(self) -> None:
        filepath = self._select_file([("Archivos de texto", "*.txt")])
        if filepath:
            self.txt_path.set(filepath)

    def do_embed(self) -> None:
        if not self.image_path.get() or not self.txt_path.get():
            messagebox.showwarning("Faltan datos", "Por favor, selecciona una imagen y un archivo .txt")
            return

        # Pedir dónde guardar la imagen resultante
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Imágenes PNG", "*.png")])
        if not save_path:
            return

        try:
            embed_message_from_file(self.image_path.get(), self.txt_path.get(), save_path)
            messagebox.showinfo("Éxito", f"Imagen guardada en:\n{save_path}")
        except Exception as error:
            messagebox.showerror("Error", f"Ocurrió un error: {str(error)}")

    def load_stego_image(self) -> None:
        filepath = self._select_file([("Imágenes PNG", "*.png")])
        if filepath:
            self.stego_image_path.set(filepath)

    def do_extract(self) -> None:
        if not self.stego_image_path.get():
            messagebox.showwarning("Faltan datos", "Por favor, selecciona una imagen para extraer el mensaje")
            return

        try:
            mensaje = extract_message(self.stego_image_path.get())
            
            # Mostrar en el área de texto
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, mensaje)
        except Exception as error:
            messagebox.showerror("Error", f"No se pudo extraer el mensaje.\n¿Seguro que la imagen tiene un mensaje oculto?\n\nDetalle: {str(error)}")


def main() -> None:
    root = tk.Tk()
    StegoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
