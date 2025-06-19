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
         empleados.append(datos)
    messagebox.showinfo("Registro exitoso", f"Empleado {datos['nombre']} registrado correctamente.")
    limpiar_campos()
    mostrar_historial()

def limpiar_campos():
    for var in [nombre_var, control_var, nacimiento_var, puesto_var, grado_var, cedula_var,
                domicilio_var, telefono_var, correo_var, ingreso_var,
                llegada_var, salida_var]:
        var.set("")
    for cb in [contratacion_cb, sexo_cb, jornada_cb, dias_cb, vacaciones_cb]:
        cb.set("")

def tomar_asistencia():
    if not empleados:
        messagebox.showwarning("Sin empleados", "No hay empleados registrados para tomar asistencia.")
        return

    for idx, check in enumerate(check_vars):
        if idx < len(empleados):
            if check.get():
                empleados[idx]["asistencias"].append("✔")
            else:
                empleados[idx]["asistencias"].append("✘")

    messagebox.showinfo("Asistencia registrada", "La asistencia fue registrada correctamente.")
    mostrar_resumen()
    limpiar_checks()

def limpiar_checks():
    for var in check_vars:
        var.set(False)
