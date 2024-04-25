import pygame
import sys
import os
#from Clases.Piezas.alfil import alfil
#from Clases.Piezas.caballo import caballo
from Clases.Piezas.Peon import Peon
#from Clases.Piezas.reina import reina
#from Clases.Piezas.rey import rey
#from Clases.Piezas.torre import torre


class ChessUI:
    def __init__(self, window_width=600, window_height=600):
        # Inicialización de Pygame
        pygame.init()

        # Dimensiones de la ventana
        self.window_width = window_width
        self.window_height = window_height

        # Definir colores
        self.WHITE = (255, 231, 186)  # Beige para los cuadrados blancos
        self.BLACK = (165, 113, 71)   # Marrón para los cuadrados negros

        # Crear ventana
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Tablero de Ajedrez")
        
        # Tamaño del cuadrado del tablero
        self.square_size = self.window_width // 8  

        # Directorio donde se encuentran las imágenes de las piezas
        self.images_dir = os.path.join("Clases", "Imagenes")

        # Cargar imágenes de los peones
        self.white_pawn_image = pygame.image.load(os.path.join(self.images_dir, "white_pawn.png"))
        self.black_pawn_image = pygame.image.load(os.path.join(self.images_dir, "black_pawn.png"))

        # Crear instancia de peón blanco en la posición (1, 2)
        self.white_pawn = Peon(color="white", position=(1, 2))

    def draw_chessboard(self):
        square_size = self.window_width // 8  # Tamaño de cada cuadrado del tablero
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    color = self.WHITE
                else:
                    color = self.BLACK
                pygame.draw.rect(self.window, color, (col * square_size, row * square_size, square_size, square_size))

    def run(self):
        # Bucle principal del juego
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Dibujar el tablero de ajedrez
            self.window.fill(self.WHITE)  # Llenar la ventana con color blanco
            self.draw_chessboard()

            # Actualizar la pantalla
            pygame.display.update()

        # Salir del programa
        pygame.quit()
        sys.exit()
