from tkinter import *
import tkinter as tk
from ventas import Ventas  # Se importa el módulo Ventas, que contiene la interfaz de ventas
from inventario import Inventario  # Se importa el módulo Inventario, que contiene la interfaz de inventario
from PIL import Image, ImageTk  # Se importa la librería PIL para trabajar con imágenes

class Container(tk.Frame):
    def __init__(self, padre, controlador):
        """
        Constructor de la clase Container que inicializa la interfaz gráfica.
        Recibe el padre (ventana principal) y un controlador como parámetros.
        """
        super().__init__(padre)  # Llamada al constructor de la clase base (tk.Frame)
        self.controlador = controlador  # Almacena el controlador para posibles interacciones
        # self.pack()  # No es necesario si usas place en el mismo widget
        self.place(x=0, y=0, width=800, height=400)  # Posiciona el contenedor en la ventana
        self.config(bg="#C6D9E3")  # Establece el color de fondo del contenedor
        self.widgets()  # Llama al método que inicializa los componentes de la interfaz

    def show_frames(self, container):
        """
        Abre una nueva ventana (Toplevel) y muestra el frame correspondiente.
        Recibe el contenedor (frame) a mostrar (Ventas o Inventario).
        """
        top_level = tk.Toplevel(self)  # Crea una ventana secundaria
        frame = container(top_level)  # Crea el frame correspondiente (Ventas o Inventario)
        frame.config(bg="#C6D9E3")  # Establece el color de fondo del frame
        frame.pack(fill="both", expand=True)  # Expande el frame para que ocupe todo el espacio
        top_level.geometry("1100x650+120+20")  # Establece el tamaño de la ventana secundaria
        top_level.resizable(False, False)  # Evita que la ventana sea redimensionada

    def ventas(self):
        """
        Método que abre la pantalla de ventas.
        Llama al método show_frames con el contenedor Ventas.
        """
        self.show_frames(Ventas)

    def inventario(self):
        """
        Método que abre la pantalla de inventario.
        Llama al método show_frames con el contenedor Inventario.
        """
        self.show_frames(Inventario)

    def widgets(self):
        """
        Método que configura todos los widgets (componentes visuales) en el contenedor principal.
        Incluye botones, imágenes y texto.
        """
        # Crea un frame dentro del contenedor principal
        frame1 = tk.Frame(self, bg="#C6D9E3")  # El color de fondo se mantiene coherente con la interfaz
        frame1.place(x=0, y=0, width=800, height=400)  # Define la posición y tamaño del frame

        # Crea el botón "Ir a ventas"
        btnventas = Button(frame1, bg="#f4b400", fg="white",  # Define el color de fondo y el texto
                           font=("sans", 18, "bold"), text="Ir a ventas", command=self.ventas)  # Vincula el botón con el método ventas
        btnventas.place(x=500, y=30, width=240, height=60)  # Posiciona el botón en la ventana

        # Crea el botón "Ir a inventario"
        btninventario = Button(frame1, bg="#c62e26", fg="white",  # Define el color de fondo y el texto
                               font=("sans", 18, "bold"), text="Ir a inventario", command=self.inventario)  # Vincula el botón con el método inventario
        btninventario.place(x=500, y=130, width=240, height=60)  # Posiciona el botón en la ventana

        # Carga y muestra el logo de la aplicación
        self.logo_image = Image.open("imagenes/registradora.png")  # Abre la imagen del logo desde el archivo
        self.logo_image = self.logo_image.resize((280, 280))  # Redimensiona la imagen para que tenga un tamaño adecuado
        self.logo_image = ImageTk.PhotoImage(self.logo_image)  # Convierte la imagen a un formato compatible con tkinter
        self.logo_label = tk.Label(frame1, image=self.logo_image, bg="#C6D9E3")  # Crea un label que contiene la imagen
        self.logo_label.place(x=100, y=30)  # Posiciona la imagen en el contenedor

        # Texto de derechos de autor al final de la ventana
        copyright_label = tk.Label(
            frame1, text=" 2025 uniremington code. Todos los derechos reservados", font="sans 12 bold", bg="#C6D9E3", fg="gray")
        copyright_label.place(x=180, y=350)  # Posiciona el texto en la parte inferior de la ventana
