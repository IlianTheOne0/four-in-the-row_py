import tkinter as tk
from tkinter import messagebox, simpledialog

from models.player import Player
from views.base_view import BaseView

class Colors:
    def __init__(self):
        self.__possible_colors = {
            "red": "red",
            "green": "green",
            "yellow": "yellow",
            "blue": "blue",
            "magenta": "magenta",
            "cyan": "cyan"
        }

    def get_possible_colors(self):
        return self.__possible_colors

class TkinterView(BaseView):
    def __init__(self):
        super().__init__()

        self.colors = Colors()
        self.root = tk.Tk()
        self.root.title("Four in the Row")
        self.root.resizable(False, False)

        self.grid_labels = []
        self.input_var = tk.StringVar()
        self.info_label = None

    def draw_field(self, field: list[list[str]], players: list[Player]) -> None:
        if not self.grid_labels:
            for row_id, row in enumerate(field):
                label_row = []
                for col_id, cell in enumerate(row):
                    label = tk.Label(self.root,
                                     text="O", font=("Courier New", 20, "bold"),
                                     width=4, height=2,
                                     fg="black", bg="#E0E0E0", relief="solid", bd=1
                                     )
                    label.grid(row=row_id, column=col_id, padx=2, pady=2)
                    label_row.append(label)

                self.grid_labels.append(label_row)

            exit_button = tk.Button(
                self.root,
                text="Exit",
                font=("Arial", 12, "bold"),
                bg="#ff4c4c",
                fg="white",
                command=self.root.destroy
            )

            exit_button.grid(row=len(field), column=0, columnspan=len(field[0]), pady=10, sticky="ew", padx=2)

        for row_id, row in enumerate(field):
            for col_id, cell in enumerate(row):
                fg_color = "black"
                display_text = cell if cell != " " else "O"

                if cell == players[0].get_symbol():
                    fg_color = players[0].get_color()
                elif cell == players[1].get_symbol():
                    fg_color = players[1].get_color()

                current_label = self.grid_labels[row_id][col_id]
                if current_label.cget("text") != display_text: current_label.config(text=display_text, fg=fg_color)

        self.root.update()

    def bind_click(self, callback):
        if not self.grid_labels:
            return

        for row in self.grid_labels:
            for col_id, label in enumerate(row):
                label.bind("<Button-1>", lambda event, col=col_id: callback(col))

    def draw_text(self, text: str) -> None:
        messagebox.showinfo("Game Info", text)

    def get_input(self, prompt: str) -> str:
        self.root.withdraw()
        result = simpledialog.askstring("Input", prompt)
        self.root.deiconify()

        return result if result is not None else ""