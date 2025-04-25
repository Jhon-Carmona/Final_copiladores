from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox


class Inventario(tk.Frame):
    def __init__(self, padre):
        super().__init__(padre)
        # self.pack() # No es necesario si usas place en el Toplevel
        self.widgets()

    def widgets(self):
        frame1 = tk.Frame(self, bg="#dddddd",
                          highlightbackground="gray", highlightthickness=1)
        frame1.place(x=0, y=0, width=1100, height=100)

        titulo = tk.Label(self, text="INVENTARIOS", bg="#dddddd",
                          font=("sans", 30, "bold"), anchor="center")
        titulo.place(x=5, y=0, width=1090, height=90)

        frame2 = tk.Frame(self, bg="#C6D9E3",
                          highlightbackground="gray", highlightthickness=1)
        frame2.place(x=0, y=100, width=1100, height=550)

        labelframe = LabelFrame(frame2, text="Productos",
                                font=("sans", 22, "bold"), bg="#C6D9E3")
        labelframe.place(x=20, y=30, width=400, height=500)

        lblbnombre = Label(labelframe, text="Nombre",
                           font=("sans", 14, "bold"), bg="#C6D9E3")
        lblbnombre.place(x=10, y=20)
        self.nombre = ttk.Entry(labelframe, font=("sans", 14))
        self.nombre.place(x=140, y=20, width=240, height=40)

        lblproveedor = Label(labelframe, text="Proveedor",
                             font=("sans", 14, "bold"), bg="#C6D9E3")
        lblproveedor.place(x=10, y=80)
        self.proveedor = ttk.Entry(labelframe, font=("sans", 14))
        self.proveedor.place(x=140, y=80, width=240, height=40)

        lblprecio = Label(labelframe, text="Precio",
                          font=("sans", 14, "bold"), bg="#C6D9E3")
        lblprecio.place(x=10, y=140)
        self.precio = ttk.Entry(labelframe, font=("sans", 14))
        self.precio.place(x=140, y=140, width=240, height=40)

        lblcosto = Label(labelframe, text="Costo",
                         font=("sans", 14, "bold"), bg="#C6D9E3")
        lblcosto.place(x=10, y=200)
        self.costo = ttk.Entry(labelframe, font=("sans", 14))
        self.costo.place(x=140, y=200, width=240, height=40)

        lblstock = Label(labelframe, text="Stock",
                         font=("sans", 14, "bold"), bg="#C6D9E3")
        lblstock.place(x=10, y=260)
        self.stock = ttk.Entry(labelframe, font=("sans", 14))
        self.stock.place(x=140, y=260, width=240, height=40)

        boton_agregar = tk.Button(
            labelframe, text="Ingresar", font=("sans", 14, "bold"), bg="#dddddd")
        boton_agregar.place(x=80, y=340, width=240, height=40)

        boton_editar = tk.Button(
            labelframe, text="Editar", font=("sans", 14, "bold"), bg="#dddddd")
        boton_editar.place(x=80, y=400, width=240, height=40)

        # tabla
        treFrame = Frame(frame2, bg="white")
        treFrame.place(x=440, y=50, width=620, height=400)

        scrol_y = ttk.Scrollbar(treFrame)
        scrol_y.pack(side=RIGHT, fill=Y)

        scrol_x = ttk.Scrollbar(treFrame, orient=HORIZONTAL)
        scrol_x.pack(side=BOTTOM, fill=X)

        self.tree = ttk.Treeview(treFrame, yscrollcommand=scrol_y.set, xscrollcommand=scrol_x.set, height=40,
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
