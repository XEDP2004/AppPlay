import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import messagebox
from reportlab.pdfgen import canvas
from datetime import datetime

class FormularioPDF:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de PDF")
        self.root.geometry("400x300")

        # Variables para almacenar los datos del formulario
        self.nombre_var = tk.StringVar()
        self.contenido_var = tk.StringVar()

        # Etiquetas y campos de entrada
        ttk.Label(root, text="Nombre:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        ttk.Entry(root, textvariable=self.nombre_var).grid(row=0, column=1, padx=10, pady=10, sticky="w")

        ttk.Label(root, text="Contenido:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        ttk.Entry(root, textvariable=self.contenido_var).grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Botón para generar y guardar el PDF
        ttk.Button(root, text="Guardar como PDF", command=self.guardar_como_pdf).grid(row=2, column=0, columnspan=2, pady=20)

    def guardar_como_pdf(self):
        nombre = self.nombre_var.get()
        contenido = self.contenido_var.get()

        if not nombre or not contenido:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        # Mostrar un cuadro de diálogo para seleccionar la ubicación de guardado
        ruta_guardado = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Archivos PDF", "*.pdf")])

        # Generar y guardar el PDF
        if ruta_guardado:
            self.generar_pdf(nombre, contenido, ruta_guardado)
            messagebox.showinfo("Éxito", f"PDF guardado en: {ruta_guardado}")

    def generar_pdf(self, nombre, contenido, ruta_guardado):
        pdf = canvas.Canvas(ruta_guardado)
        pdf.drawString(100, 800, f"Nombre: {nombre}")
        pdf.drawString(100, 780, "Contenido:")
        pdf.drawString(100, 760, contenido)
        pdf.drawString(100, 740, f"Fecha de creación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        pdf.save()

if __name__ == "__main__":
    root = tk.Tk()
    app = FormularioPDF(root)
    root.mainloop()