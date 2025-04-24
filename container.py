from tkinter import *
import tkinter as tk
from ventas import Ventas
from inventario import Inventario


class Container(tk.Frame):
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.pack()
        self.place(x=0, y=0, width=800, height=400)
        self.config(bg="#C6D9E3")
        self.widgets()

    def show_frames(self, container):
        top_level = tk.Toplevel(self)
        frame = container(top_level)
        frame.config(bg="#C6D9E3")
        frame.pack(fill="both", expand=True)
        top_level.geometry("1100x650+120+20")
        top_level.resizable(False, False)

    def ventas(self):
        self.show_frames(Ventas)

    def inventario(self):
        self.show_frames(Inventario)

    def widgets(self):

        frame1 = tk.Frame(self, bg="#C6D9E3")
        frame1.pack()
        frame1.place(x=0, y=0, width=800, height=400)

        btnventas = Button(frame1, bg="green", fg="black",
                        text="Ir a ventas", command=self.ventas)
        btnventas.place(x=500, y=30, width=240, height=60)

        btninventario = Button(frame1, bg="blue", fg="white",
                            text="Ir a inventario", command=self.inventario)
        btninventario.place(x=500, y=130, width=240, height=60)
