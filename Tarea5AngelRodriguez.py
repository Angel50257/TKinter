import os
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox
from tkinter import ttk, filedialog

DATA_FILE = "tareas.txt"

def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return "break"

def agregar_tareas():
    def agregar():
        try:
            vtarea = tarea.get()
            vopcion = var.get()

            with open(DATA_FILE, "a") as file:
                file.write(f"{vtarea},{vopcion}\n")
                messagebox.showinfo("Tarea agregada", "La tarea fue agregada exitosamente.")
        except FileNotFoundError:
            print(f"Error: El archivo {file} no fue encontrado.")

    # Genera una nueva ventana emergente o secundaria en la aplicacion de tkinter
    window_agregar_tareas = tk.Toplevel(root)
    window_agregar_tareas.title("Agregar tarea")
    window_agregar_tareas.geometry("400x300")
    window_agregar_tareas.configure(background="#be9341")
    # crear etiquetas
    label = tk.Label(window_agregar_tareas, text="Introduce la tarea: ")
    label.grid(row=0, column=0, padx=10, pady=10)
    label.configure(background="#d1a453")

    # crear un cuadro de texto
    tarea = tk.Entry(window_agregar_tareas)
    tarea.grid(row=0, column=1, padx=10, pady=10)
    tarea.bind("<Return>", focus_next_widget)

    button = tk.Button(window_agregar_tareas, text="Agregar", command=agregar)
    button.grid(row=4, column=0, columnspan=1, pady=10)
    button.configure(background="#d1a453")

    # seleccionar estado
    var = tk.StringVar(window_agregar_tareas)
    var.set("Pendiente")
    opciones = ["Completada", "Pendiente"]

    opcion = tk.OptionMenu(window_agregar_tareas, var, *opciones)
    opcion.grid(row=4, column=1, padx=10, pady=10)
    # opcion.configure(activebackground="#d1a453")
    opcion.configure(activeforeground="#845f0c")  # activeforeground


def ver_tareas():
    def load_list():
        tareas = leer_tareas()

        # limpiar datos en el Treeview
        for row in tree.get_children():
            tree.delete(row)
        # insertar datos en el Treeview
        for item in tareas:
            tree.insert("", "end", values=item)

    window_ver_tareas = tk.Toplevel(root)
    window_ver_tareas.title("Ver tareas")
    window_ver_tareas.geometry("600x300")
    (window_ver_tareas.configure(background="#be9341"))

    # crear el treeview
    columns = ("#", "Tarea", "Estado")
    tree = ttk.Treeview(window_ver_tareas, columns=columns, show="headings")
    tree.heading("#", text="#")
    tree.heading("Tarea", text="Tarea")
    tree.heading("Estado", text="Estado")
    tree.grid(row=0, column=0, sticky="nsew")

    # anadir una barra de desplazamiento vertical
    scrollbar = ttk.Scrollbar(window_ver_tareas, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky="ns")

    # configurar el grid
    window_ver_tareas.grid_rowconfigure(0, weight=0)
    window_ver_tareas.grid_columnconfigure(0, weight=1)

    # botonpara cargar la lista
    button2 = tk.Button(window_ver_tareas, text="Cargar lista", command=load_list)
    button2.grid(row=2, column=1, pady=10)
    button2.configure(background="#97701e")


def leer_tareas():
    if not os.path.exists(DATA_FILE):
        return []
    tareas = []

    with open(DATA_FILE, "r") as file:
        for i, line in enumerate(file, start=1):
            datos = line.strip().split(",")
            if len(datos) == 2:
                tarea, estado = datos
                tareas.append((i, tarea, estado))
            else:
                tareas.append((i, datos[0], "Pendiente"))
    return tareas


def marcar_completada():
    window_marcar_completado = tk.Toplevel(root)
    window_marcar_completado.title("Marcar completado")
    window_marcar_completado.geometry("500x300")
    window_marcar_completado.configure(background="#be9341")

    tareas = leer_tareas()

    def load_list():
        for row in tree.get_children():
            tree.delete(row)
        for i, tarea, estado in tareas:
            tree.insert("", "end", values=(i, tarea, estado))

    def actualizar_estado():
        selected_item = tree.selection()
        if not selected_item:
            return

        index = int(tree.item(selected_item)["values"][0]) - 1
        nuevo_estado = var.get()

        tareas[index] = (tareas[index][0], tareas[index][1], nuevo_estado)
        guardar_tareas(tareas)
        load_list()

    # Crear Treeview
    columns = ("#", "Tarea", "Estado")
    tree = ttk.Treeview(window_marcar_completado, columns=columns, show="headings")
    tree.heading("#", text="#")
    tree.heading("Tarea", text="Tarea")
    tree.heading("Estado", text="Estado")
    tree.grid(row=0, column=0, sticky="nsew")

    # Scrollbar vertical
    scrollbar = ttk.Scrollbar(window_marcar_completado, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky="ns")

    # Configurar grid
    window_marcar_completado.grid_rowconfigure(0, weight=1)
    window_marcar_completado.grid_columnconfigure(0, weight=1)

    load_list()

    # Selector de estado
    var = tk.StringVar(window_marcar_completado)
    opciones = ["Completada", "Pendiente"]
    opcion_menu = tk.OptionMenu(window_marcar_completado, var, *opciones)
    opcion_menu.grid(row=1, column=0, padx=10, pady=10)

    # Botón para actualizar estado
    btn_actualizar = tk.Button(window_marcar_completado, text="Actualizar Estado", command=actualizar_estado)
    btn_actualizar.grid(row=2, column=0, padx=10, pady=10)


# opcion.configure(activeforeground="#845f0c")  # activeforeground


def eliminar_tareas():
    def eliminar():
        try:
            vtarea = int(numero.get()) - 1

            if 0 <= vtarea < len(tareas):
                del tareas[vtarea]
                guardar_tareas(tareas)
                messagebox.showinfo("Tarea Eliminada", "La tarea fue eliminada exitosamente.")
                load_list()  # Recargar lista
            else:
                messagebox.showerror("Error", "Número de tarea inválido.")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido.")

    def load_list():
        for row in tree.get_children():
            tree.delete(row)

        for i, item in enumerate(tareas, start=1):
            tree.insert("", "end", values=item)

    window_eliminar_tareas = tk.Toplevel(root)
    window_eliminar_tareas.title("Eliminar tareas")
    window_eliminar_tareas.geometry("700x350")
    window_eliminar_tareas.configure(background="#be9341")
    tareas = leer_tareas()

    label = tk.Label(window_eliminar_tareas, text="Introduce el número: ")
    label.grid(row=1, column=0, padx=10, pady=10)
    label.configure(background="#d1a453")

    # crear un cuadro de texto
    numero = tk.Entry(window_eliminar_tareas)
    numero.grid(row=2, column=0, padx=10, pady=10)
    numero.bind("<Return>", focus_next_widget)

    # crear el treeview
    columns = ("#", "Tarea", "Estado")
    tree = ttk.Treeview(window_eliminar_tareas, columns=columns, show="headings")
    tree.heading("#", text="#")
    tree.heading("Tarea", text="Tarea")
    tree.heading("Estado", text="Estado")
    tree.grid(row=0, column=0, sticky="nsew")

    # anadir una barra de desplazamiento vertical
    scrollbar = ttk.Scrollbar(window_eliminar_tareas, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky="ns")

    # configurar el grid
    window_eliminar_tareas.grid_rowconfigure(0, weight=0)
    window_eliminar_tareas.grid_columnconfigure(0, weight=1)

    # boton eliminar
    button = tk.Button(window_eliminar_tareas, text="Eliminar", command=eliminar)
    button.grid(row=3, column=0, pady=10)
    button.configure(background="#97701e")

    load_list()


def guardar_tareas(tareas):
    with open(DATA_FILE, "w") as file:
        for item in tareas:
            if len(item) == 3:
                _, tarea, estado = item
            elif len(item) == 2:
                tarea, estado = item
            else:
                continue
            file.write(f"{tarea},{estado}\n")



# Menu principal
root = tk.Tk()
root.title("TAREAS")
root.geometry("800x500")
root.configure(background='#d1a453')

# crear la barra del menu
menu_bar = Menu(root)
root.config(menu=menu_bar)

# agregar un menu desplegable
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Archivo", menu=file_menu)
file_menu.configure(background="#be9341")

# agregar
file_menu.add_command(label="Agregar Tareas", command=agregar_tareas)
file_menu.add_command(label="Ver Tareas", command=ver_tareas)
file_menu.add_command(label="Marcar Tareas", command=marcar_completada)
file_menu.add_command(label="Eliminar Tareas", command=eliminar_tareas)
file_menu.add_separator()
file_menu.add_command(label="Salir", command=root.quit)

root.mainloop()
