# Importa módulos de tkinter y sqlite3
import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

class Inventario(tk.Frame):
    db_name = "database.db"  # Nombre de la base de datos

    def __init__(self, padre):
        super().__init__(padre)
        self.conn = sqlite3.connect(self.db_name)  # Conexión a la base de datos
        self.cursor = self.conn.cursor()
        self.widgets()

    def widgets(self):
        """Crea la interfaz gráfica de inventario"""

        frame1 = tk.Frame(self, bg="#dddddd", highlightbackground="gray", highlightthickness=1)
        frame1.place(x=0, y=0, width=1100, height=100)

        titulo = tk.Label(self, text="INVENTARIOS", bg="#dddddd",
                          font=("sans", 30, "bold"), anchor="center")
        titulo.place(x=5, y=0, width=1090, height=90)

        frame2 = tk.Frame(self, bg="#C6D9E3", highlightbackground="gray", highlightthickness=1)
        frame2.place(x=0, y=100, width=1100, height=550)

        labelframe = LabelFrame(frame2, text="Productos", font=("sans", 22, "bold"), bg="#C6D9E3")
        labelframe.place(x=20, y=30, width=400, height=500)

        # Entradas de producto
        lblbnombre = Label(labelframe, text="Nombre", font=("sans", 14, "bold"), bg="#C6D9E3")
        lblbnombre.place(x=10, y=20)
        self.nombre = ttk.Entry(labelframe, font=("sans", 14))
        self.nombre.place(x=140, y=20, width=240, height=40)

        lblproveedor = Label(labelframe, text="Proveedor", font=("sans", 14, "bold"), bg="#C6D9E3")
        lblproveedor.place(x=10, y=80)
        self.proveedor = ttk.Entry(labelframe, font=("sans", 14))
        self.proveedor.place(x=140, y=80, width=240, height=40)

        lblprecio = Label(labelframe, text="Precio", font=("sans", 14, "bold"), bg="#C6D9E3")
        lblprecio.place(x=10, y=140)
        self.precio = ttk.Entry(labelframe, font=("sans", 14))
        self.precio.place(x=140, y=140, width=240, height=40)

        lblcosto = Label(labelframe, text="Costo", font=("sans", 14, "bold"), bg="#C6D9E3")
        lblcosto.place(x=10, y=200)
        self.costo = ttk.Entry(labelframe, font=("sans", 14))
        self.costo.place(x=140, y=200, width=240, height=40)

        lblstock = Label(labelframe, text="Stock", font=("sans", 14, "bold"), bg="#C6D9E3")
        lblstock.place(x=10, y=260)
        self.stock = ttk.Entry(labelframe, font=("sans", 14))
        self.stock.place(x=140, y=260, width=240, height=40)

        # Botones
        boton_agregar = tk.Button(labelframe, text="Ingresar", font=("sans", 14, "bold"),
                                  bg="#dddddd", command=self.registrar)
        boton_agregar.place(x=80, y=340, width=240, height=40)

        boton_editar = tk.Button(labelframe, text="Editar", font=("sans", 14, "bold"),
                                 bg="#dddddd", command=self.editar_producto)
        boton_editar.place(x=80, y=400, width=240, height=40)

        # Tabla
        treFrame = Frame(frame2, bg="white")
        treFrame.place(x=440, y=50, width=620, height=400)

        scrol_y = ttk.Scrollbar(treFrame)
        scrol_y.pack(side=RIGHT, fill=Y)

        scrol_x = ttk.Scrollbar(treFrame, orient=HORIZONTAL)
        scrol_x.pack(side=BOTTOM, fill=X)

        self.tree = ttk.Treeview(treFrame, yscrollcommand=scrol_y.set, xscrollcommand=scrol_x.set,
                                 columns=("ID", "PRODUCTO", "PROVEEDOR", "PRECIO", "COSTO", "STOCK"), show="headings")
        self.tree.pack(expand=True, fill=BOTH)

        scrol_y.config(command=self.tree.yview)
        scrol_x.config(command=self.tree.xview)

        self.tree.heading("ID", text="Id")
        self.tree.heading("PRODUCTO", text="Producto")
        self.tree.heading("PROVEEDOR", text="Proveedor")
        self.tree.heading("PRECIO", text="Precio")
        self.tree.heading("COSTO", text="Costo")
        self.tree.heading("STOCK", text="Stock")

        self.tree.column("ID", width=70, anchor="center")
        self.tree.column("PRODUCTO", width=100, anchor="center")
        self.tree.column("PROVEEDOR", width=100, anchor="center")
        self.tree.column("PRECIO", width=100, anchor="center")
        self.tree.column("COSTO", width=100, anchor="center")
        self.tree.column("STOCK", width=70, anchor="center")

        self.mostrar()

        btn_actualizar = Button(frame2, text="Actualizar", font=("sans", 14, "bold"),
                                bg="#dddddd", command=self.actualizar_inventario)
        btn_actualizar.place(x=440, y=480, width=260, height=50)

    def eje_consulta(self, consulta, parametros=()):
        """Ejecuta una consulta SQL"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(consulta, parametros)
            conn.commit()
        return result

    def validacion(self, nombre, pro, precio, costo, stock):
        """Valida los campos de entrada"""
        if not (nombre.strip() and pro.strip() and precio.strip() and costo.strip() and stock.strip()):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return False
        try:
            float(precio)
            float(costo)
            int(stock)
        except ValueError:
            messagebox.showerror("Error", "Precio, costo o stock inválido")
            return False
        return True

    def mostrar(self):
        """Carga productos en la tabla"""
        for item in self.tree.get_children():
            self.tree.delete(item)

        consulta = "SELECT * FROM inventario ORDER BY id DESC"
        result = self.eje_consulta(consulta)
        for element in result:
            try:
                precio = float(element[3])
                costo = float(element[4])
                precio_formateado = "{:,.0f}".format(precio)
                costo_formateado = "{:,.0f}".format(costo)
            except (ValueError, TypeError):
                precio_formateado = element[3]
                costo_formateado = element[4]

            self.tree.insert("", 0, text=element[0], values=(
                element[0], element[1], element[2], precio_formateado, costo_formateado, element[5]))

    def actualizar_inventario(self):
        """Actualiza la tabla"""
        self.mostrar()
        messagebox.showinfo("Actualización", "Inventario actualizado correctamente")

    def registrar(self):
        """Registra un nuevo producto"""
        nombre = self.nombre.get()
        prov = self.proveedor.get()
        precio = self.precio.get()
        costo = self.costo.get()
        stock = self.stock.get()

        if self.validacion(nombre, prov, precio, costo, stock):
            try:
                consulta = "INSERT INTO inventario (nombre, proveedor, precio, costo, stock) VALUES (?, ?, ?, ?, ?)"
                parametros = (nombre, prov, float(precio), float(costo), int(stock))
                self.eje_consulta(consulta, parametros)
                self.actualizar_inventario()
                self.nombre.delete(0, END)
                self.proveedor.delete(0, END)
                self.precio.delete(0, END)
                self.costo.delete(0, END)
                self.stock.delete(0, END)
            except Exception as e:
                messagebox.showerror("Error", f"Error al registrar: {e}")

    def editar_producto(self):
        """Edita el producto seleccionado"""
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un producto para editar")
            return
        item = self.tree.item(seleccion)
        valores = item['values']

        ventana_editar = Toplevel(self)
        ventana_editar.title("Editar Producto")
        ventana_editar.geometry("400x400")
        ventana_editar.config(bg="#C6D9E3")

        labels = ["Nombre", "Proveedor", "Precio", "Costo", "Stock"]
        entradas = []

        for i, texto in enumerate(labels):
            Label(ventana_editar, text=texto, bg="#C6D9E3").grid(row=i, column=0, padx=10, pady=10)
            entry = Entry(ventana_editar, width=30)
            entry.grid(row=i, column=1, padx=10, pady=10)
            entry.insert(0, valores[i+1])
            entradas.append(entry)

        def guardar_cambios():
            nuevos = [e.get() for e in entradas]
            if not all(nuevos):
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return
            try:
                consulta = "UPDATE inventario SET nombre=?, proveedor=?, precio=?, costo=?, stock=? WHERE id=?"
                parametros = (nuevos[0], nuevos[1], float(nuevos[2].replace(",", "")), float(nuevos[3].replace(",", "")), int(nuevos[4]), valores[0])
                self.eje_consulta(consulta, parametros)
                self.actualizar_inventario()
                ventana_editar.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Error al actualizar: {e}")

        Button(ventana_editar, text="Guardar cambios", command=guardar_cambios, font=("sans", 14, "bold")).place(x=80, y=320, width=240, height=40)
