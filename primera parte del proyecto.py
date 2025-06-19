import tkinter as tk
from tkinter import ttk, messagebox

empleados = []

def registrar_empleado():
    datos = {
        "nombre": nombre_var.get(),
        "numero_control": control_var.get(),
        "nacimiento": nacimiento_var.get(),
        "puesto": puesto_var.get(),
        "contratacion": contratacion_cb.get(),
        "sexo": sexo_cb.get(),
        "grado": grado_var.get(),
        "cedula": cedula_var.get(),
        "domicilio": domicilio_var.get(),
        "telefono": telefono_var.get(),
        "correo": correo_var.get(),
        "ingreso": ingreso_var.get(),
        "jornada": jornada_cb.get(),
        "dias": dias_cb.get(),
        "vacaciones": vacaciones_cb.get(),
        "hora_llegada": llegada_var.get(),
        "hora_salida": salida_var.get(),
        "asistencias": []
    }
    
    if not datos["nombre"] or not datos["numero_control"]:
        messagebox.showwarning("Datos incompletos", "Por favor, ingresa al menos el nombre y número de control.")
        return
