# Título: Sistema de Registro de libros
# Estudiante: Walter Antonio Machaca Anze

import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox

# Creación, configuración de ventana
ventana = tb.Window(themename="darkly")
ventana.title("Sistema de Registro de Libros")
ventana.geometry("1200x750")
ventana.resizable(False, False)

# Creacion de notebook para las pestañas
notebook = tb.Notebook(ventana)

# Creación de pestañas
tab_registro = tb.Frame(notebook)
tab_catálogo = tb.Frame(notebook)

# Agregar pestañas al notebook
notebook.add(tab_registro, text="Registro de Libros")
notebook.add(tab_catálogo, text="Catálogo")

# Publicar el notebook en la ventana
notebook.pack(pady=10, padx=10, fill="both", expand=True)

# Creación de título
título_registro = tb.Label(tab_registro, text="Registro de Libros", font=("Calibri", 20, "bold"), bootstyle="warning")
título_registro.pack(pady=20)
título_catálogo = tb.Label(tab_catálogo, text="Catálogo de Libros", font=("Calibri", 20, "bold"), bootstyle="warning")
título_catálogo.pack(pady=20)

# Creación de frame para el formulario de ingreso de datos
frame_registro = tb.Frame(tab_registro)
frame_registro.pack(pady=10, padx=50, fill="x")
frame_catálogo = tb.Frame(tab_catálogo)
frame_catálogo.pack(pady=10, padx=50, fill="x")

# Creación de widgets (etiquetas, entradas, botones)
# Para pestaña Registro
etiqueta_título_libro = tb.Label(frame_registro, text="Título del Libro:", font=("Calibri", 12, "bold"), bootstyle="warning")
caja_título_libro = tb.Entry(frame_registro, font=("Calibri", 12), bootstyle="info")
etiqueta_autor_libro = tb.Label(frame_registro, text="Autor:", font=("Calibri", 12, "bold"), bootstyle="warning")
caja_autor_libro = tb.Entry(frame_registro, font=("Calibri", 12), bootstyle="info")
etiqueta_categoría_libro = tb.Label(frame_registro, text="Categoría:", font=("Calibri", 12, "bold"), bootstyle="warning")
combo_categoría_libro = tb.Combobox(frame_registro, font=("Calibri", 12), state="readonly")
combo_categoría_libro['values'] = ("Programación", "Base de Datos", "Redes", "Inteligencia Artificial")
combo_categoría_libro.current(0)  # Establecer valor predeterminado

# Creación de la variable para el Checkbutton
var_préstamo = tb.BooleanVar()

etiqueta_préstamo = tb.Label(frame_registro, text="Disponible para préstamo:", font=("Calibri", 12, "bold"), bootstyle="warning")
check_préstamo = tb.Checkbutton(frame_registro, bootstyle="round-toggle", variable=var_préstamo)

# Creación de botones
botón_agregar_libro = tb.Button(frame_registro, text="Agregar Libro", bootstyle="warning", width=12)
botón_limpiar_tabla = tb.Button(frame_registro, text="Limpiar", bootstyle="warning", width=12)

# Creación de grilla para organizar los widgets del formulario
# Para pestaña Registro
etiqueta_título_libro.grid(row=0, column=1, padx=10, pady=5, sticky="e")
caja_título_libro.grid(row=0, column=2, padx=10, pady=5, sticky="w")
etiqueta_autor_libro.grid(row=1, column=1, padx=10, pady=5, sticky="e")
caja_autor_libro.grid(row=1, column=2, padx=10, pady=5, sticky="w")
etiqueta_categoría_libro.grid(row=2, column=1, padx=10, pady=5, sticky="e")
combo_categoría_libro.grid(row=2, column=2, padx=10, pady=5, sticky="w")
etiqueta_préstamo.grid(row=3, column=1, padx=10, pady=5, sticky="e")
check_préstamo.grid(row=3, column=2, padx=10, pady=5, sticky="w")
botón_agregar_libro.grid(row=4, column=0, padx=10, pady=15)
botón_limpiar_tabla.grid(row=4, column=3, padx=10, pady=15)

# Creación de frames para las tablas
frame_tabla_catálogo= tb.Frame(tab_catálogo)
frame_tabla_catálogo.pack(pady=15, padx=50, fill="both", expand=True)

# Configuración del grid para que la tabla se expanda correctamente
frame_tabla_catálogo.grid_rowconfigure(0, weight=1)
frame_tabla_catálogo.grid_columnconfigure(0, weight=1)

# Creación de tablas para mostrar el catálogo de libros
columnas_catálogo = ["Título", "Autor", "Categoría", "Disponible"]
tabla_catálogo = tb.Treeview(frame_tabla_catálogo, columns=columnas_catálogo, show="headings", selectmode="browse", bootstyle="success")

# Configuración de anchos de columnas ajustados a la pantalla
tabla_catálogo.column("Título", width=300, anchor=CENTER)
tabla_catálogo.column("Autor", width=200, anchor=CENTER)
tabla_catálogo.column("Categoría", width=200, anchor=CENTER)
tabla_catálogo.column("Disponible", width=150, anchor=CENTER)

# Encabezados de columnas
tabla_catálogo.heading("Título", text="Título")
tabla_catálogo.heading("Autor", text="Autor")
tabla_catálogo.heading("Categoría", text="Categoría")
tabla_catálogo.heading("Disponible", text="Disponible")

# Creación de barra de desplazamiento 
scrollbar_catálogo = tb.Scrollbar(frame_tabla_catálogo, orient="vertical", command=tabla_catálogo.yview, bootstyle="success")  
tabla_catálogo.configure(yscrollcommand=scrollbar_catálogo.set)
tabla_catálogo.grid(row=0, column=0, sticky="nsew")
scrollbar_catálogo.grid(row=0, column=1, sticky="ns")

# Listas para almacenar los datos de los libros registrados
libros_registrados = []

# Funciones

# Función para agregar un libro al catálogo y actualizar la lista de libros en la pestaña de catálogo
def agregar_libro():
    título = caja_título_libro.get()
    autor = caja_autor_libro.get()
    categoría = combo_categoría_libro.get()
    disponible = "Sí" if var_préstamo.get() else "No"

    if título and autor:
        libro = (título, autor, categoría, disponible)
        libros_registrados.append(libro)
        tabla_catálogo.insert("", tb.END, values=libro)
        
        caja_título_libro.delete(0, tb.END)
        caja_autor_libro.delete(0, tb.END)
        combo_categoría_libro.current(0)
        var_préstamo.set(False)
    else:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
        
# Función para limpiar los campos del formulario      
def limpiar():
    # Limpiar los campos del formulario
    caja_título_libro.delete(0, tb.END)
    caja_autor_libro.delete(0, tb.END)
    combo_categoría_libro.current(0)
    var_préstamo.set(False)
    # Vaciar la lista de libros registrados
    libros_registrados.clear()
    # Eliminar todos los registros visuales del Treeview
    for elemento in tabla_catálogo.get_children():
        tabla_catálogo.delete(elemento)

# Asociación de eventos a los botones
botón_agregar_libro.config(command=agregar_libro)
botón_limpiar_tabla.config(command=limpiar)

ventana.mainloop()