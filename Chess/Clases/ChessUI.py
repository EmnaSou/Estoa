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
        
        #Tamaño de los peones
        self.piezas_size = (50, 50)  # Anchura y altura deseada para los peones
        
        # Cargar imágenes de los peones blancos y negros
        self.white_pawn = pygame.image.load(os.path.join(self.images_dir, "white pawn.png"))
        self.black_pawn = pygame.image.load(os.path.join(self.images_dir, "black pawn.png"))
    
        # Cargar imágenes de los peones blancos y negros y ajustar su tamaño
        self.white_pawn = pygame.transform.scale(pygame.image.load(os.path.join(self.images_dir, "white pawn.png")), self.piezas_size)
        self.black_pawn = pygame.transform.scale(pygame.image.load(os.path.join(self.images_dir, "black pawn.png")), self.piezas_size)

        #Alfiles
        self.white_rook = pygame.image.load(os.path.join(self.images_dir, "white rook.png"))
        self.black_rook = pygame.image.load(os.path.join(self.images_dir, "black rook.png"))
        self.white_rook = pygame.transform.scale(pygame.image.load(os.path.join(self.images_dir, "white rook.png")), self.piezas_size)
        self.black_rook = pygame.transform.scale(pygame.image.load(os.path.join(self.images_dir, "black rook.png")), self.piezas_size)
        
        #Caballos
        self.white_knight = pygame.image.load(os.path.join(self.images_dir, "white knight.png"))
        self.black_knight = pygame.image.load(os.path.join(self.images_dir, "black knight.png"))
        self.white_knight = pygame.transform.scale(pygame.image.load(os.path.join(self.images_dir, "white knight.png")), self.piezas_size)
        self.black_knight = pygame.transform.scale(pygame.image.load(os.path.join(self.images_dir, "black knight.png")), self.piezas_size)
         
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
                    x = col * self.square_size + (self.square_size - self.piezas_size[0]) // 2
                    y = row * self.square_size + (self.square_size - self.piezas_size[0]) // 2 
                    self.window.blit(self.white_pawn, (x, y))
            # Dibujar peones negros en la séptima fila
            elif row == 6:
                for col in range(8):
                    x = col * self.square_size + (self.square_size - self.piezas_size[0]) // 2
                    y = row * self.square_size + (self.square_size - self.piezas_size[1]) // 2
                    self.window.blit(self.black_pawn, (x, y))
                    
    def draw_rooks(self):
        # Dibujar torres blancas en las esquinas superiores
        self.window.blit(self.white_rook, (self.square_size // 2 - self.piezas_size[0] // 2, self.square_size // 2 - self.piezas_size[1] // 2))
        self.window.blit(self.white_rook, ((7 * self.square_size) + self.square_size // 2 - self.piezas_size[0] // 2, self.square_size // 2 - self.piezas_size[1] // 2))
        # Dibujar torres negras en las esquinas inferiores
        self.window.blit(self.black_rook, (self.square_size // 2 - self.piezas_size[0] // 2, (7 * self.square_size) + self.square_size // 2 - self.piezas_size[1] // 2))
        self.window.blit(self.black_rook, ((7 * self.square_size) + self.square_size // 2 - self.piezas_size[0] // 2, (7 * self.square_size) + self.square_size // 2 - self.piezas_size[1] // 2))

    def draw_knights(self):
        # Dibujar caballos blancos en las esquinas superiores
        self.window.blit(self.white_knight, (self.square_size // 2 - self.piezas_size[0] // 2, (self.square_size - self.piezas_size[1]) // 2))
        self.window.blit(self.white_knight, ((6 * self.square_size) + self.square_size // 2 - self.piezas_size[0] // 2, (self.square_size - self.piezas_size[1]) // 2))
        # Dibujar caballos negros en las esquinas inferiores
        self.window.blit(self.black_knight, (self.square_size // 2 - self.piezas_size[0] // 2, (7 * self.square_size) + (self.square_size - self.piezas_size[1]) // 2))
        self.window.blit(self.black_knight, ((6 * self.square_size) + self.square_size // 2 - self.piezas_size[0] // 2, (7 * self.square_size) + (self.square_size - self.piezas_size[1]) // 2))


    
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
            self.draw_rooks()

            # Actualizar la pantalla
            pygame.display.update()

        # Salir del programa
        pygame.quit()
        sys.exit()
