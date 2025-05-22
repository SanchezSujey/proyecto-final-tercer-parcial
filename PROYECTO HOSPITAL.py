import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def agregar_datos():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    IDN = entry_IDN.get()

    if not nombre or not edad or not correo:
        messagebox.showwarning("Campos Vacíos", "Por favor, completa todos los campos.")
        return

    if not edad.isdigit():
        messagebox.showerror("Edad Inválida", "La edad debe ser un número.")
        return

   
    tabla.insert("", "end", values=(nombre, edad, IDN))

   
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_correo.delete(0, tk.END)


ventana = tk.Tk()
ventana.title("Formulario de Personas con Historial")
ventana.geometry("500x400")

# Etiquetas y entradastk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_nombre = tk.Entry(ventana, width=30)
entry_nombre.grid(row=0, column=1)

tk.Label(ventana, text="Edad:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_edad = tk.Entry(ventana, width=30)
entry_edad.grid(row=1, column=1)

tk.Label(ventana, text= "IDN:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_correo = tk.Entry(ventana, width=30)
entry_correo.grid(row=2, column=1)


btn_agregar = tk.Button(ventana, text="Agregar al Historial", command=agregar_datos)
btn_agregar.grid(row=3, column=0, columnspan=2, pady=10)

tabla = ttk.Treeview(ventana, columns=("Nombre", "Edad", "IDN"), show="headings")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Edad", text="Edad")
tabla.heading("IDN", text="IDN")
tabla.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


ventana.mainloop()