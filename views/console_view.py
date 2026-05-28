from colorama import init, Fore, Back

from models.player import Player
from views.base_view import BaseView

class Colors:
    def __init__(self):
        init(autoreset=True)
        self.__possible_colors = {
            "red": self.red,
            "green": self.green,
            "yellow": self.yellow,
            "blue": self.blue,
            "magenta": self.magenta,
            "cyan": self.cyan
        }

    def get_possible_colors(self): return self.__possible_colors

    def red(self, text): return Fore.RED + text
    def green(self, text): return Fore.GREEN + text
    def yellow(self, text): return Fore.YELLOW + text
    def blue(self, text): return Fore.BLUE + text
    def magenta(self, text): return Fore.MAGENTA + text
    def cyan(self, text): return Fore.CYAN + text

    def apply_color(self, color_name: str, text: str) -> str:
        if color_name in self.__possible_colors:
            return self.__possible_colors[color_name](text)
        return text

class ConsoleView(BaseView):
    def __init__(self):
        super().__init__()

        self.colors = Colors()

    def draw_field(self, field: list[list[str]], players: list[Player]) -> None:
        print("\n" * 2)

        for i in range(len(field[0])):
            print(f"  {i + 1}", end=" ")
        print()

        border_length =len(field[0]) * 4 + 1
        print("-" * border_length)

        for row in field:
            print("|", end=" ")
            for cell in row:
                if (cell == players[0].get_symbol()): print(self.colors.apply_color(players[0].get_color(), cell), end=" | ")
                elif (cell == players[1].get_symbol()): print(self.colors.apply_color(players[1].get_color(), cell), end=" | ")
                else: print(cell, end=" | ")
            print()

        print("-" * border_length)
        print("\n" * 2)

    def draw_text(self, text: str) -> None: print(text)

    def get_input(self, prompt: str) -> str: return input(prompt)

    def show_colors_for_choosing(self):
        print ("Available colors: ", end="")

        for name in self.colors.get_possible_colors().keys():
            print(name, end =", ")