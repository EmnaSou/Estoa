import tkinter as tk

class ChessUI:
    def __init__(self, master):
        self.master = master
        master.title("Chess Game")

        # Creamos el tablero como una matriz de etiquetas
        self.board_labels = []
        for i in range(8):
            row = []
            for j in range(8):
                label = tk.Label(master, text=" ", width=2, height=1, relief="ridge")
                label.grid(row=i, column=j)
                row.append(label)
            self.board_labels.append(row)

    def update_board(self, board_state):
        # Actualizamos el estado del tablero con la matriz de piezas
        for i in range(8):
            for j in range(8):
                piece = board_state[i][j]
                self.board_labels[i][j].config(text=piece)

def main():
    root = tk.Tk()
    chess_ui = ChessUI(root)
    board_state = [
        ["R", "N", "B", "Q", "K", "B", "N", "R"],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        ["r", "n", "b", "q", "k", "b", "n", "r"]
    ]
    chess_ui.update_board(board_state)
    root.mainloop()

if __name__ == "__main__":
    main()
