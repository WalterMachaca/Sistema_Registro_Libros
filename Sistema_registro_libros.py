# Título: Sistema de Registro de libros
# Estudiante: Walter Antonio Machaca Anze

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Creación, configuración de ventana
ventana = tk.Tk()
ventana.title("Sistema de Registro de Libros")
ventana.geometry("900x650")
ventana.resizable(False, False)
ventana.configure(bg="#4A4E69")  

# Creacion de notebook para las pestañas
notebook = ttk.Notebook(ventana)

# Creación de pestañas
tab_registro = tk.Frame(notebook, bg="#4A4E69")
tab_catálogo = tk.Frame(notebook, bg="#4A4E69")

# Agregar pestañas al notebook
notebook.add(tab_registro, text="Registro de Libros")
notebook.add(tab_catálogo, text="Catálogo")

# Publicar el notebook en la ventana
notebook.pack(pady=10, padx=10, fill="both", expand=True)

# Creación de título
título_registro = tk.Label(tab_registro, text="Registro de Libros", font=("Calibri", 20, "bold"), fg="#D4A373", bg="#4A4E69")
título_registro.pack(pady=20)
título_catálogo = tk.Label(tab_catálogo, text="Catálogo de Libros", font=("Calibri", 20, "bold"), fg="#D4A373", bg="#4A4E69")
título_catálogo.pack(pady=20)

# Creación de frame para el formulario de ingreso de datos
frame_registro = tk.Frame(tab_registro, bg="#4A4E69", padx=20, pady=20)
frame_registro.pack(pady=10, padx=50, fill="x")
frame_catálogo = tk.Frame(tab_catálogo, bg="#4A4E69", padx=20, pady=20)
frame_catálogo.pack(pady=10, padx=50, fill="x")

# Creación de widgets (etiquetas, entradas, botones)
# Para pestaña Registro
etiqueta_título_libro = tk.Label(frame_registro, text="Título del Libro:", font=("Calibri", 12, "bold"), bg="#4A4E69", fg="#D4A373")
caja_título_libro = tk.Entry(frame_registro, font=("Calibri", 12), bg="white", fg="black", insertbackground="black")
etiqueta_autor_libro = tk.Label(frame_registro, text="Autor:", font=("Calibri", 12, "bold"), bg="#4A4E69", fg="#D4A373")
caja_autor_libro = tk.Entry(frame_registro, font=("Calibri", 12), bg="white", fg="black", insertbackground="black")
etiqueta_categoría_libro = tk.Label(frame_registro, text="Categoría:", font=("Calibri", 12, "bold"), bg="#4A4E69", fg="#D4A373")
combo_categoría_libro = ttk.Combobox(frame_registro, font=("Calibri", 12), state="readonly")
combo_categoría_libro['values'] = ("Programación", "Base de Datos", "Redes", "Inteligencia Artificial")
combo_categoría_libro.current(0)  # Establecer valor predeterminado

# Creación de la variable para el Checkbutton
var_préstamo = tk.BooleanVar()

etiqueta_préstamo = tk.Label(frame_registro, text="Disponible para préstamo:", font=("Calibri", 12, "bold"), bg="#4A4E69", fg="#D4A373")
check_préstamo = tk.Checkbutton(frame_registro, bg="#4A4E69", activebackground="#4A4E69", selectcolor="#D4A373", variable=var_préstamo)

# Creación de botones
botón_agregar_libro = tk.Button(frame_registro, text="Agregar Libro", font=("Calibri", 11, "bold"), bg="#2E4A3F", fg="white", width=12)
botón_limpiar_tabla = tk.Button(frame_registro, text="Limpiar", font=("Calibri", 11, "bold"), bg="#D4A373", fg="white", width=12)

# Creación de grilla para organizar los widgets del formulario
# Para pestaña Registro
etiqueta_título_libro.grid(row=0, column=0, padx=10, pady=5, sticky="e")
caja_título_libro.grid(row=0, column=1, padx=10, pady=5, sticky="w")
etiqueta_autor_libro.grid(row=1, column=0, padx=10, pady=5, sticky="e")
caja_autor_libro.grid(row=1, column=1, padx=10, pady=5, sticky="w")
etiqueta_categoría_libro.grid(row=2, column=0, padx=10, pady=5, sticky="e")
combo_categoría_libro.grid(row=2, column=1, padx=10, pady=5, sticky="w")
etiqueta_préstamo.grid(row=3, column=0, padx=10, pady=5, sticky="e")
check_préstamo.grid(row=3, column=1, padx=10, pady=5, sticky="w")
botón_agregar_libro.grid(row=4, column=0, padx=10, pady=15)
botón_limpiar_tabla.grid(row=4, column=1, padx=10, pady=15)

# Creación de frames para las tablas
frame_tabla_catálogo= tk.Frame(tab_catálogo, bg="#4A4E69", padx=20, pady=20)
frame_tabla_catálogo.pack(pady=15, padx=50, fill="both", expand=True)

# Configuración del grid para que la tabla se expanda correctamente
frame_tabla_catálogo.grid_rowconfigure(0, weight=1)
frame_tabla_catálogo.grid_columnconfigure(0, weight=1)

# Configuración de estilo para la tabla
estilo = ttk.Style()
estilo.theme_use("default")
estilo.configure("Treeview", background="#2a3042", foreground="white", rowheight=30, fieldbackground="white", borderwidth=0)
estilo.configure("Treeview.Heading", background="#2E4A3F", foreground="#D4A373", font=("Calibri", 11, "bold"))
estilo.map("Treeview", background=[("selected", "#2E4A3F")], foreground=[("selected", "white")])

# Creación de tablas para mostrar el catálogo de libros
columnas_catálogo = ["Título", "Autor", "Categoría", "Disponible"]
tabla_catálogo = ttk.Treeview(frame_tabla_catálogo, columns=columnas_catálogo, show="headings", selectmode="browse")

# Configuración de anchos de columnas ajustados a la pantalla
tabla_catálogo.column("Título", width=300, anchor=tk.CENTER)
tabla_catálogo.column("Autor", width=200, anchor=tk.CENTER)
tabla_catálogo.column("Categoría", width=200, anchor=tk.CENTER)
tabla_catálogo.column("Disponible", width=150, anchor=tk.CENTER)

# Encabezados de columnas
tabla_catálogo.heading("Título", text="Título")
tabla_catálogo.heading("Autor", text="Autor")
tabla_catálogo.heading("Categoría", text="Categoría")
tabla_catálogo.heading("Disponible", text="Disponible")

# Creación de barra de desplazamiento 
scrollbar_catálogo = ttk.Scrollbar(frame_tabla_catálogo, orient="vertical", command=tabla_catálogo.yview)  
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
        tabla_catálogo.insert("", tk.END, values=libro)
    else:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
        
# Función para limpiar los campos del formulario      
def limpiar():
    # Limpiar los campos del formulario
    caja_título_libro.delete(0, tk.END)
    caja_autor_libro.delete(0, tk.END)
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