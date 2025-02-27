import os
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox
from tkinter import ttk,filedialog

DATA_FILE = "tareas.txt"
def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return "break"

def agregar_tareas():
    def agregar():
        try:
            vtarea = tarea.get()

            with open(DATA_FILE, "a") as file:
                file.write(f"{vtarea}\n")
                messagebox.showinfo("Tarea agregada","La tarea fue agregada exitosamente.")
        except FileNotFoundError:
            print(f"Error: El archivo {file} no fue encontrado.")

    #Genera una nueva ventana emergente o secundaria en la palicacion de tkinter
    window_agregar_tareas = tk.Toplevel(root)
    window_agregar_tareas.title("Agregar tarea")
    window_agregar_tareas.geometry("400x300")
    #crear etiquetas
    label = tk.Label(window_agregar_tareas, text="Introduce la tarea: ")
    label.grid(row=0,column=0,padx=10,pady=10)

    #crear un cuadro de texto
    tarea = tk.Entry(window_agregar_tareas)
    tarea.grid(row=0,column=1,padx=10,pady=10)
    tarea.bind("<Return>",focus_next_widget)

    button = tk.Button(window_agregar_tareas,text="Agregar",command=agregar)
    button.grid(row=3,column=0,columnspan=2,pady=10)

def ver_tareas():
    def load_list():
        data =tareas

        #limpiar datos en el Treeview
        for row in tree.get_children():
            tree.delete(row)
        #insertar datos en el Treeview
        for item in data:
            tree.insert("","end",values=item)

    window_marcar_completado = tk.Toplevel(root)
    window_marcar_completado.title("Ver tareas")
    window_marcar_completado.geometry("600x300")
    tareas = leer_tareas()

    #crear el treeview
    columns = ("","Tarea")
    tree = ttk.Treeview(window_marcar_completado,columns=columns,show="headings")
    tree.heading("Tarea",text="Tarea")
    tree.heading("", text="")

    tree.grid(row=0,column=0,sticky="nsew")

    #anadir una barra de desplazamiento vertical
    scrollbar = ttk.Scrollbar(window_marcar_completado,orient="vertical",command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0,column=1,sticky="ns")

    #configurar el grid
    window_marcar_completado.grid_rowconfigure(0,weight=0)
    window_marcar_completado.grid_columnconfigure(0,weight=1)

    #botonpara cargar la lista
    button2 = tk.Button(window_marcar_completado,text="Cargar lista",command=load_list)
    button2.grid(row=2,column=1,pady=10)

def leer_tareas():
    if not os.path.exists(DATA_FILE):
        return []
    tareas = []

    with open(DATA_FILE, "r") as file:
        for i, line in enumerate(file,start=1):
            tarea = line.strip()
            tareas.append((i,tarea))
    return tareas

def marcar_completada():
    window_marcar_completado = tk.Toplevel(root)
    window_marcar_completado.title("Marcar completado")
    window_marcar_completado.geometry("400x400")

    frame_tareas = tk.Frame(window_marcar_completado)
    frame_tareas.pack(pady=10)

    tareas = leer_tareas()
    check_vars = []  # Lista para almacenar los estados de los checkboxes

    def marcar_como_completada():
        tareas_completadas = [tareas[i][0] for i, var in enumerate(check_vars) if var.get()]
        messagebox.showinfo("Tareas Completadas",
                            "\n".join(tareas_completadas) if tareas_completadas else "Ninguna tarea marcada.")

    for tarea in tareas:
        var = tk.BooleanVar()
        check_vars.append(var)
        chk = tk.Checkbutton(frame_tareas, text=tarea[1], variable=var)
        chk.pack(anchor="w")

    btn_completar = tk.Button(window_marcar_completado, text="Marcar Completadas", command=marcar_como_completada)
    btn_completar.pack(pady=10)

def eliminar_tareas():
    def eliminar():
        try:
            vtarea = int(numero.get())

            # Buscar la tarea por índice
            tarea_encontrada = next((t for t in tareas if t[0] == vtarea), None)

            if tarea_encontrada:
                tareas.remove(tarea_encontrada)  # Eliminar la tarea de la lista
                guardar_tareas(tareas)  # Guardar sin índices en el archivo
                messagebox.showinfo("Tarea Eliminada", "La tarea fue eliminada exitosamente.")
                load_list()  # Recargar lista
            else:
                messagebox.showerror("Error", "Número de tarea inválido.")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido.")

    def load_list():
        for row in tree.get_children():
            tree.delete(row)

        for item in tareas:
            tree.insert("", "end", values=item)

    window_eliminar_tareas = tk.Toplevel(root)
    window_eliminar_tareas.title("Eliminar tareas")
    window_eliminar_tareas.geometry("600x300")
    tareas = leer_tareas()

    label = tk.Label(window_eliminar_tareas,text="Introduce el numero: ")
    label.grid(row=1,column=0,padx=10,pady=10)

    #crear un cuadro de texto
    numero = tk.Entry(window_eliminar_tareas)
    numero.grid(row=1,column=1,padx=10,pady=10)
    numero.bind("<Return>",focus_next_widget)

    # crear el treeview
    columns = ("","Tarea")
    tree = ttk.Treeview(window_eliminar_tareas, columns=columns, show="headings")
    tree.heading("", text="")
    tree.heading("Tarea", text="Tarea")

    tree.grid(row=0, column=0, sticky="nsew")

    # anadir una barra de desplazamiento vertical
    scrollbar = ttk.Scrollbar(window_eliminar_tareas, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky="ns")

    # configurar el grid
    window_eliminar_tareas.grid_rowconfigure(0, weight=0)
    window_eliminar_tareas.grid_columnconfigure(0, weight=1)

    #boton eliminar
    button = tk.Button(window_eliminar_tareas, text="Eliminar", command=eliminar)
    button.grid(row=2, column=0, pady=10)

    # botonpara cargar la lista
    button2 = tk.Button(window_eliminar_tareas, text="Cargar lista", command=load_list)
    button2.grid(row=2, column=1, pady=10)

def guardar_tareas(tareas):
    with open(DATA_FILE,"w") as file:
        for _, tarea in tareas:
            file.write(f"{tarea}\n")

#Menu principal
root = tk.Tk()
root.title("TAREAS")
root.geometry("800x500")

#crear la barra del menu
menu_bar = Menu(root)
root.config(menu=menu_bar)

#agregar un menu desplegable
file_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Archivo", menu=file_menu)

#agregar
file_menu.add_command(label="Agregar Tareas",command=agregar_tareas)
file_menu.add_command(label="Ver Tareas",command=ver_tareas)
file_menu.add_command(label="Modificar Contactos",command=marcar_completada)
file_menu.add_command(label="Eliminar Tareas",command=eliminar_tareas)
file_menu.add_separator()
file_menu.add_command(label="Salir",command=root.quit)

root.mainloop()