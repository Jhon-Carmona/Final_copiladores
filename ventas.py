from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox


class Ventas(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)  # 1100, 650
        self.widgets()  # Llama al método widgets aquí

    def widgets(self):

        frame1 = tk.Frame(self, bg="#dddddd")
        # Corrección: Usar solo place
        frame1.place(x=0, y=0, width=1100, height=100)

        titulo = tk.Label(self, text="VENTAS", bg="#dddddd",
                          font=("sans", 30, "bold"), anchor="center")  # Corrección: Sintaxis de font y usar solo place
        titulo.place(x=5, y=0, width=1090, height=90)

        frame2 = tk.Frame(self, bg="#C6D9E3")
        frame2.place(x=0, y=100, width=1100, height=550)

        lblframe = LabelFrame(
            frame2, text="Infromacion de la venta", bg="#C6D9E3", font="sans 16 bold")
        lblframe.place(x=10, y=10, width=1060, height=80)

        label_numero_factura = tk.Label(
            lblframe, text="Numero de \nfactura", bg="#C6D9E3", font="sans 12 bold")
        label_numero_factura.place(x=10, y=5)
        self.numero_factura = tk.StringVar()

        self.entry_numero_factura = ttk.Entry(
            lblframe, textvariable=self.numero_factura, state="readonly", font="sans 12 bold")
        self.entry_numero_factura.place(x=100, y=5, width=80)

        label_nombre = tk.Label(
            lblframe, text="Producto: ", bg="#C6D9E3", font="sans 12 bold")
        label_nombre.place(x=200, y=12)

        self.entry_nombre = ttk.Entry(lblframe, font="sans 12 bold")
        self.entry_nombre.place(x=280, y=10, width=180)

        label_valor = tk.Label(lblframe, text="precio: ",
                               bg="#C6D9E3", font="sans 12 bold")
        label_valor.place(x=470, y=12)

        self.entry_valor = ttk.Entry(lblframe, font="sans 12 bold")
        self.entry_valor.place(x=540, y=10, width=180)

        label_cantidad = tk.Label(
            lblframe, text="Cantidad: ", bg="#C6D9E3", font="sans 12 bold")
        label_cantidad.place(x=730, y=12)

        self.entry_cantidad = ttk.Entry(lblframe, font="sans 12 bold")
        self.entry_cantidad.place(x=820, y=10)

        treFrame = tk.Frame(frame2, bg="#C6D9E3")
        treFrame.place(x=150, y=120, width=800, height=200)

        scrol_y = ttk.Scrollbar(treFrame, orient=VERTICAL)
        scrol_y.pack(side=RIGHT, fill=Y)  # Corrección: Usar la constante Y

        scrol_x = ttk.Scrollbar(treFrame, orient=HORIZONTAL)
        scrol_x.pack(side=BOTTOM, fill=X)  # Corrección: Usar la constante X

        self.tree = ttk.Treeview(treFrame, columns=(
            "Producto", "Precio", "Cantidad", "Subtotal"), show="headings", height=10,
            yscrollcommand=scrol_y.set, xscrollcommand=scrol_x.set)  # Corrección: Usar '='

        scrol_y.config(command=self.tree.yview)
        # Corrección: Usar .xview para la barra horizontal
        scrol_x.config(command=self.tree.xview)

        self.tree.heading("#1", text="Producto")
        self.tree.heading("#2", text="Precio")
        self.tree.heading("#3", text="Cantidad")
        self.tree.heading("#4", text="Subtotal")

        self.tree.column("#1", anchor="center")
        self.tree.column("#2", anchor="center")
        self.tree.column("#3", anchor="center")
        self.tree.column("#4", anchor="center")

        self.tree.pack(expand=True, fill=BOTH)

        lblframe1 = LabelFrame(frame2, text="Opciones",
                               bg="#C6D9E3", font="sans 12 bold")
        lblframe1.place(x=10, y=300, width=1060, height=100)

        boton_agregar = tk.Button(
            lblframe1, text="Agregar Articulo", bg="#dddddd", font="sans 12 bold")
        boton_agregar.place(x=50, y=10, width=240, height=50)

        boton_pagar = tk.Button(
            lblframe1, text="Pagar", bg="#dddddd", font="sans 12 bold")
        boton_pagar.place(x=400, y=10, width=240, height=50)

        boton_ver_facturas = tk.Button(
            lblframe1, text="Ver facturas", bg="#dddddd", font="sans 12 bold")
        boton_ver_facturas.place(x=750, y=10, width=240, height=50)
