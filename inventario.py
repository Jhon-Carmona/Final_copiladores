# Importa módulos de tkinter para crear interfaces gráficas
from tkinter import ttk, messagebox
import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox


class Inventario(tk.Frame):
    db_name = "database.db"  # Nombre de la base de datos

    def __init__(self, padre):
        super().__init__(padre)
        # self.pack() # No es necesario si usas place en el Toplevel
        self.conn = sqlite3.connect(self.db_name)  # Conecta a la base de datos
        self.cursor = self.conn.cursor()  # Crea un cursor para ejecutar comandos SQL

        self.widgets()

    def widgets(self):
        """
        Método que configura todos los widgets (componentes visuales) en el contenedor de inventario.
        Incluye etiquetas, campos de entrada, botones, y una tabla para mostrar los productos.
        """
        # Crea un frame para la cabecera de la interfaz
        frame1 = tk.Frame(self, bg="#dddddd",
                            highlightbackground="gray", highlightthickness=1)
        frame1.place(x=0, y=0, width=1100, height=100)

        # Título del formulario
        titulo = tk.Label(self, text="INVENTARIOS", bg="#dddddd",
                            font=("sans", 30, "bold"), anchor="center")
        titulo.place(x=5, y=0, width=1090, height=90)

        # Crea un segundo frame para contener el formulario y la tabla
        frame2 = tk.Frame(self, bg="#C6D9E3",
                            highlightbackground="gray", highlightthickness=1)
        frame2.place(x=0, y=100, width=1100, height=550)

        # Crea un LabelFrame para agrupar los campos de entrada de los productos
        labelframe = LabelFrame(frame2, text="Productos",
                                    font=("sans", 22, "bold"), bg="#C6D9E3")
        labelframe.place(x=20, y=30, width=400, height=500)

        # Campo de entrada para el nombre del producto
        lblbnombre = Label(labelframe, text="Nombre",
                                    font=("sans", 14, "bold"), bg="#C6D9E3")
        lblbnombre.place(x=10, y=20)
        self.nombre = ttk.Entry(labelframe, font=("sans", 14))
        self.nombre.place(x=140, y=20, width=240, height=40)

        # Campo de entrada para el proveedor del producto
        lblproveedor = Label(labelframe, text="Proveedor",
                                        font=("sans", 14, "bold"), bg="#C6D9E3")
        lblproveedor.place(x=10, y=80)
        self.proveedor = ttk.Entry(labelframe, font=("sans", 14))
        self.proveedor.place(x=140, y=80, width=240, height=40)

        # Campo de entrada para el precio del producto
        lblprecio = Label(labelframe, text="Precio",
                                    font=("sans", 14, "bold"), bg="#C6D9E3")
        lblprecio.place(x=10, y=140)
        self.precio = ttk.Entry(labelframe, font=("sans", 14))
        self.precio.place(x=140, y=140, width=240, height=40)

        # Campo de entrada para el costo del producto
        lblcosto = Label(labelframe, text="Costo",
                                    font=("sans", 14, "bold"), bg="#C6D9E3")
        lblcosto.place(x=10, y=200)
        self.costo = ttk.Entry(labelframe, font=("sans", 14))
        self.costo.place(x=140, y=200, width=240, height=40)

        # Campo de entrada para el stock del producto
        lblstock = Label(labelframe, text="Stock",
                                    font=("sans", 14, "bold"), bg="#C6D9E3")
        lblstock.place(x=10, y=260)
        self.stock = ttk.Entry(labelframe, font=("sans", 14))
        self.stock.place(x=140, y=260, width=240, height=40)

        # Botón para agregar un nuevo producto al inventario
        boton_agregar = tk.Button(labelframe, text="Ingresar", font=(
            "sans", 14, "bold"), bg="#dddddd", command=self.registrar)
        boton_agregar.place(x=80, y=340, width=240, height=40)

        # Botón para editar un producto ya existente en el inventario
        boton_editar = tk.Button(
            labelframe, text="Editar", font=("sans", 14, "bold"), bg="#dddddd", command=self.editar_producto)
        boton_editar.place(x=80, y=400, width=240, height=40)

        # Sección de tabla para mostrar los productos en el inventario
        treFrame = Frame(frame2, bg="white")
        treFrame.place(x=440, y=50, width=620, height=400)

        # Scroll vertical de la tabla
        scrol_y = ttk.Scrollbar(treFrame)
        scrol_y.pack(side=RIGHT, fill=Y)

        # Scroll horizontal de la tabla
        scrol_x = ttk.Scrollbar(treFrame, orient=HORIZONTAL)
        scrol_x.pack(side=BOTTOM, fill=X)

        # Tabla donde se mostrarán los productos registrados
        self.tree = ttk.Treeview(treFrame, yscrollcommand=scrol_y.set, xscrollcommand=scrol_x.set, height=40,
                                    columns=("ID", "PRODUCTO", "PROVEEDOR", "PRECIO", "COSTO", "STOCK"), show="headings")
        self.tree.pack(expand=True, fill=BOTH)

        # Vincula los scrollbars a la tabla para permitir desplazamiento
        scrol_y.config(command=self.tree.yview)
        scrol_x.config(command=self.tree.xview)

        # Define los encabezados de la tabla
        self.tree.heading("ID", text="Id")
        self.tree.heading("PRODUCTO", text="Producto")
        self.tree.heading("PROVEEDOR", text="Proveedor")
        self.tree.heading("PRECIO", text="Precio")
        self.tree.heading("COSTO", text="Costo")
        self.tree.heading("STOCK", text="Stock")

        # Define las características de las columnas (anchura y alineación)
        self.tree.column("ID", width=70, anchor="center")
        self.tree.column("PRODUCTO", width=100, anchor="center")
        self.tree.column("PROVEEDOR", width=100, anchor="center")
        self.tree.column("PRECIO", width=100, anchor="center")
        self.tree.column("COSTO", width=100, anchor="center")
        self.tree.column("STOCK", width=70, anchor="center")

        self.mostrar()

        btn_actualizar = Button(frame2, text="Actualizar", font=("sans", 14, "bold"), bg="#dddddd", command=self.actualizar_inventario)
        btn_actualizar.place(x=440, y=480, width=260, height=50)

    def eje_consulta(self, consulta, parametros=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(consulta, parametros)
            conn.commit()
        return result

    def validacion(self, nombre, pro, precio, costo, stock):
        if not (nombre and pro and precio and costo and stock):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return False
        try:
            float(precio)
            float(costo)
            int(stock)
        except ValueError:
            return False
        return True

    def mostrar(self):
        consulta = "SELECT * FROM inventario ORDER by id DESC"
        result = self.eje_consulta(consulta)
        for element in result:
            try:
                precio_cop = "{:,.0f}".format(element[3]) if element[3] else ""
                costo_cop = "{:,.0f}".format(element[4]) if element[4] else ""
            except ValueError:
                precio_cop = element[3]
                costo_cop = element[4]
            self.tree.insert("", 0, text=element[0], values=(
                element[0], element[1], element[2], precio_cop, costo_cop, element[5]))

    def actualizar_inventario(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.mostrar()

        messagebox.showinfo(
            "Actualización", "Inventario actualizado correctamente")

    def registrar(self):
        result = self.tree.get_children()
        for i in result:
            self.tree.delete(i)
            nombre = self.nombre.get()
            prov = self.proveedor.get()
            precio = self.precio.get()
            costo = self.costo.get()
            stock = self.stock.get()
            if self.validacion(nombre, prov, precio, costo, stock):
                try:
                    consulta = "INSERT INTO inventario VALUES (?, ?, ?, ?, ?, ?)"
                    parametros = (None, nombre, prov, precio, costo, stock)
                    self.eje_consulta(consulta, parametros)
                    self.mostrar()
                    self.nombre.delete(0, END)
                    self.proveedor.delete(0, END)
                    self.precio.delete(0, END)
                    self.costo.delete(0, END)
                    self.stock.delete(0, END)
                except Exception as e:
                    messagebox.showerror(
                        title="Error", message=f"Error al registrar el producto: {e}")
            else:
                messagebox.showwarning(
                    title="Error", message="Error en la validación de datos")
                self.mostrar()

    def editar_producto(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning(
                "Advertencia", "Seleccione un producto para editar")
            return
        item_id = self.tree.item(seleccion)["text"]
        item_values = self.tree.item(seleccion)["values"]

        ventana_editar = Toplevel(self)
        ventana_editar.title("Editar Producto")
        ventana_editar.geometry("400x400")
        ventana_editar.config(bg="#C6D9E3")

        lbl_nombre = Label(ventana_editar, text="Nombre", bg="#C6D9E3")
        lbl_nombre.grid(row=0, column=0, padx=10, pady=10)
        entry_nombre = Entry(ventana_editar, width=30)
        entry_nombre.grid(row=0, column=1, padx=10, pady=10)
        entry_nombre.insert(0, item_values[1])

        lbl_proveedor = Label(ventana_editar, text="proveedor", bg="#C6D9E3")
        lbl_proveedor.grid(row=1, column=0, padx=10, pady=10)
        entry_proveedor = Entry(ventana_editar, width=30)
        entry_proveedor.grid(row=1, column=1, padx=10, pady=10)
        entry_proveedor.insert(0, item_values[2])

        lbl_precio = Label(ventana_editar, text="Precio", bg="#C6D9E3")
        lbl_precio.grid(row=2, column=0, padx=10, pady=10)
        entry_precio = Entry(ventana_editar, width=30)
        entry_precio.grid(row=2, column=1, padx=10, pady=10)
        entry_precio.insert(0, item_values[3].split()[0].replace(",", ""))

        lbl_costo = Label(ventana_editar, text="Costo", bg="#C6D9E3")
        lbl_costo.grid(row=3, column=0, padx=10, pady=10)
        entry_costo = Entry(ventana_editar, width=30)
        entry_costo.grid(row=3, column=1, padx=10, pady=10)
        entry_costo.insert(0, item_values[4].split()[0].replace(",", ""))

        lbl_stock = Label(ventana_editar, text="Stock", bg="#C6D9E3")
        lbl_stock.grid(row=4, column=0, padx=10, pady=10)
        entry_stock = Entry(ventana_editar, width=30)
        entry_stock.grid(row=4, column=1, padx=10, pady=10)
        entry_stock.insert(0, item_values[5])

        def guardar_cambios():
            nombre = entry_nombre.get()
            proveedor = entry_proveedor.get()
            precio = entry_precio.get()
            costo = entry_costo.get()
            stock = entry_stock.get()

            if not (nombre and proveedor and precio and costo and stock):
                messagebox.showwarning(
                    "Guardar cambios", "Rellene todos los campos.")
                return

            try:
                precio = float(precio.replace(",", "."))
                costo = float(costo.replace(",", ""))
            except ValueError:
                messagebox.showwarning(
                    "Guardar cambios", "Ingrese valores numéricos válidos para precio y costo.")
                return
            consulta = "UPDATE inventario SET nombre=?, proveedor=?, precio=?, costo=?, stock=? WHERE id=?"
            parametros = (nombre, proveedor, precio, costo, stock, item_id)
            self.eje_consulta(consulta, parametros)

            self.actualizar_inventario()

            ventana_editar.destroy()

        btn_guardar = Button(ventana_editar, text="Guardar cambios",
                                    font="sans 14 bold", command=guardar_cambios)
        btn_guardar.place(x=80, y=250, width=240, height=40)