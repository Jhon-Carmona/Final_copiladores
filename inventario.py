from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox


class Inventario(tk.Frame):
    def __init__(self, padre):
        super().__init__(padre)
        self.pack()
        self.widgets()

    def widgets(self):
        frame1 = tk.Frame(self, bg="#dddddd")
        frame1.pack()
        frame1.place(x=0, y=0, width=1100, height="100")

        titulo = tk.Label(self, text="INVANETARIOS", bg="#dddddd")
        titulo.pack()
        titulo.place(x=5, y=0, width=1090, heigth=90)
