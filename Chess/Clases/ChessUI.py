import pygame
import os
import sys

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

        # Cargar imágenes de los peones blancos y negros
        self.white_pawn_image = pygame.image.load(os.path.join(self.images_dir, "white pawn.png"))
        self.black_pawn_image = pygame.image.load(os.path.join(self.images_dir, "black pawn.png"))

    def draw_chessboard(self):
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    color = self.WHITE
                else:
                    color = self.BLACK
                pygame.draw.rect(self.window, color, (col * self.square_size, row * self.square_size, self.square_size, self.square_size))

    def draw_pawns(self):
        for row in range(8):
            # Dibujar peones blancos en la segunda fila
            if row == 1:
                for col in range(8):
                    x = col * self.square_size
                    y = row * self.square_size
                    self.window.blit(self.white_pawn_image, (x, y))
            # Dibujar peones negros en la séptima fila
            elif row == 6:
                for col in range(8):
                    x = col * self.square_size
                    y = row * self.square_size
                    self.window.blit(self.black_pawn_image, (x, y))

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

            # Dibujar peones en el tablero
            self.draw_pawns()

            # Actualizar la pantalla
            pygame.display.update()

        # Salir del programa
        pygame.quit()
        sys.exit()
