from tkinter import Tk, Frame  # Se importan las clases Tk y Frame de tkinter para crear la ventana principal y los marcos
from container import Container  # Se importa el módulo Container, que contiene la clase Container que maneja el contenido de la interfaz
from ttkthemes import ThemedStyle  # Se importa ThemedStyle para aplicar un tema visual al aplicativo


class Manager(Tk):
    def __init__(self, *args, **kwargs):
        """
        Constructor de la clase Manager que inicializa la ventana principal de la aplicación.
        """
        super().__init__(*args, **kwargs)  # Llama al constructor de la clase base Tk
        self.title("Caja Registradora version 1.0")  # Define el título de la ventana principal
        self.resizable(False, False)  # Deshabilita la opción de redimensionar la ventana
        self.configure(bg="#6CD9E3")  # Establece el color de fondo de la ventana principal
        self.geometry("800x400+120+20")  # Define el tamaño y la posición de la ventana principal

        # Crea un contenedor (Frame) dentro de la ventana principal para contener otros elementos
        self.container = Frame(self, bg="#6CD9E3")
        self.container.pack(fill="both", expand=True)  # Se asegura de que el contenedor ocupe todo el espacio disponible

        # Diccionario para almacenar las instancias de los frames
        self.frames = {
            Container: None  # Aquí se mapea la clase Container para poder cargarla más tarde
        }

        self.load_frames()  # Carga los frames definidos en el diccionario 'frames'
        self.show_frame(Container)  # Muestra el primer frame (Container) por defecto

        self.set_theme()  # Aplica un tema visual a la ventana

    def load_frames(self):
        """
        Método que carga las clases de los frames y las instancia dentro del contenedor.
        """
        for FrameClass in self.frames.keys():  # Itera sobre todas las clases de frames
            frame = FrameClass(self.container, self)  # Crea una instancia de cada clase de frame
            self.frames[FrameClass] = frame  # Almacena la instancia en el diccionario 'frames'

    def show_frame(self, frame_class):
        """
        Método que eleva el frame deseado al frente (lo hace visible).
        """
        frame = self.frames[frame_class]  # Obtiene el frame de la clase proporcionada
        frame.tkraise()  # Llama a tkraise para poner el frame sobre otros widgets

    def set_theme(self):
        """
        Método que aplica un tema visual a la ventana utilizando la librería 'ttkthemes'.
        """
        style = ThemedStyle(self)  # Crea una instancia de ThemedStyle para aplicar un tema
        style.set_theme("breeze")  # Establece el tema "breeze" para la ventana

# Función principal que ejecuta la aplicación
def main():
    app = Manager()  # Crea una instancia de la clase Manager
    app.mainloop()  # Inicia el bucle principal de la interfaz gráfica

# Si el archivo es ejecutado directamente, llama a la función principal
if __name__ == "__main__":
    main()
