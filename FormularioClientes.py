import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class FormularioClientes:
    def __init__(self):
        self.base = None
        self.texBoxCC = None
        self.texBoxNombres = None
        self.texBoxApellidos = None
        self.comboSexo = None
        self.tree = None

    def formulario(self):
        try:
            self.base = Tk()
            self.base.geometry("1200x300")
            self.base.title("Formulario de Clientes")

            # Grupo de datos personales
            groupBox = LabelFrame(self.base, text="Datos del Cliente", padx=5, pady=5)
            groupBox.grid(row=0, column=0, padx=10, pady=10)

            # Declaramnos los campos del formulario para los clientes 
            Label(groupBox, text="Cédula de Ciudadanía:", width=20, font=("arial", 12)).grid(row=0, column=0)
            self.texBoxCC = Entry(groupBox)
            self.texBoxCC.grid(row=0, column=1)

            Label(groupBox, text="Nombres:", width=20, font=("arial", 12)).grid(row=1, column=0)
            self.texBoxNombres = Entry(groupBox)
            self.texBoxNombres.grid(row=1, column=1)

            Label(groupBox, text="Apellidos:", width=20, font=("arial", 12)).grid(row=2, column=0)
            self.texBoxApellidos = Entry(groupBox)
            self.texBoxApellidos.grid(row=2, column=1)

            Label(groupBox, text="Sexo:", width=20, font=("arial", 12)).grid(row=3, column=0)
            self.comboSexo = ttk.Combobox(groupBox, values=["Masculino", "Femenino", "Otro"])
            self.comboSexo.grid(row=3, column=1)
            self.comboSexo.current(0)

            # Botones para guardar, editar y eliminar registros
            Button(groupBox, text="Guardar", width=10, command=self.guardarRegistro).grid(row=4, column=0)
            Button(groupBox, text="Editar", width=10, command=self.actualizarRegistro).grid(row=4, column=1)
            Button(groupBox, text="Eliminar", width=10, command=self.eliminarRegistro).grid(row=4, column=2)

            # Tabla que muestra los registros
            groupBox2 = LabelFrame(self.base, text="Lista de Clientes", padx=5, pady=5)
            groupBox2.grid(row=0, column=1, padx=10, pady=10)

            self.tree = ttk.Treeview(groupBox2, columns=("CC", "Nombres", "Apellidos", "Sexo"), show="headings", height=5)
            self.tree.column("#1", anchor=CENTER)
            self.tree.heading("#1", text="Cédula")
            self.tree.column("#2", anchor=CENTER)
            self.tree.heading("#2", text="Nombres")
            self.tree.column("#3", anchor=CENTER)
            self.tree.heading("#3", text="Apellidos")
            self.tree.column("#4", anchor=CENTER)
            self.tree.heading("#4", text="Sexo")
            self.tree.pack()

            # Mostar los registros en la tabla
            self.mostrarRegistros()

            # Evento que nos permite seleccionar un registro de la tabla
            self.tree.bind("<<TreeviewSelect>>", self.seleccionarRegistro)

            self.base.mainloop()
        except ValueError as error:
            print(f"Error al abrir formulario: {error}")

    def guardarRegistro(self):
        try:
            cc = self.texBoxCC.get()
            nombres = self.texBoxNombres.get()
            apellidos = self.texBoxApellidos.get()
            sexo = self.comboSexo.get()
            
            #Mensaje de error si no se ingresan los datos
            if not cc or not nombres or not apellidos:
                messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
                return

            # Agregamos una tabla
            self.tree.insert("", "end", values=(cc, nombres, apellidos, sexo))
            messagebox.showinfo("Éxito", "Registro guardado correctamente")

            # Limpiar campos después de guardar
            self.texBoxCC.delete(0, END)
            self.texBoxNombres.delete(0, END)
            self.texBoxApellidos.delete(0, END)
            self.comboSexo.current(0)
        except Exception as error:
            print(f"Error al guardar registro: {error}")

    def actualizarRegistro(self):
        try:
            seleccionado = self.tree.selection()
            if not seleccionado:
                messagebox.showwarning("Advertencia", "Seleccione un registro para editar.")
                return

            cc = self.texBoxCC.get()
            nombres = self.texBoxNombres.get()
            apellidos = self.texBoxApellidos.get()
            sexo = self.comboSexo.get()

            if not cc or not nombres or not apellidos:
                messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
                return

            # Actualizar datos de la tabla 
            self.tree.item(seleccionado, values=(cc, nombres, apellidos, sexo))
            messagebox.showinfo("Éxito", "Registro actualizado correctamente")

            # Limpiar campos después de actualizar
            self.texBoxCC.delete(0, END)
            self.texBoxNombres.delete(0, END)
            self.texBoxApellidos.delete(0, END)
            self.comboSexo.current(0)
        except Exception as error:
            print(f"Error al actualizar registro: {error}")

    def eliminarRegistro(self):
        try:
            seleccionado = self.tree.selection()
            if not seleccionado:
                messagebox.showwarning("Advertencia", "Seleccione un registro para eliminar.")
                return

            # Eliminar el registro de la tabla
            self.tree.delete(seleccionado)
            messagebox.showinfo("Éxito", "Registro eliminado correctamente")

            # Limpiar campos después de eliminar
            self.texBoxCC.delete(0, END)
            self.texBoxNombres.delete(0, END)
            self.texBoxApellidos.delete(0, END)
            self.comboSexo.current(0)
        except Exception as error:
            print(f"Error al eliminar registro: {error}")

    def mostrarRegistros(self):
        # Aquí iría la lógica para cargar registros desde la base de datos
        # Por ahora, agregamos algunos datos de ejemplo
        registros = [
            ("123456789", "Juan", "Pérez", "Masculino"),
            ("987654321", "María", "Gómez", "Femenino"),
        ]

        for registro in registros:
            self.tree.insert("", "end", values=registro)

    def seleccionarRegistro(self, event):
        try:
            seleccionado = self.tree.selection()
            if seleccionado:
                valores = self.tree.item(seleccionado, "values")
                self.texBoxCC.delete(0, END)
                self.texBoxCC.insert(0, valores[0])
                self.texBoxNombres.delete(0, END)
                self.texBoxNombres.insert(0, valores[1])
                self.texBoxApellidos.delete(0, END)
                self.texBoxApellidos.insert(0, valores[2])
                self.comboSexo.set(valores[3])
        except Exception as error:
            print(f"Error al seleccionar registro: {error}")


# Crear una instancia del formulario y mostrarlo
app = FormularioClientes()
app.formulario()