import os

from controllers.base_controller import BaseController
from views.console_view import ConsoleView

class ConsoleController(BaseController):
    def __init__(self, view: ConsoleView) -> None:
        super().__init__(view)

        self._view = view
        self._turn = 0

    def _clear_console(self): os.system("cls" if os.name == "nt" else "clear")
    def _wait(self): input("Press Enter to continue...")
    def __wait_and_clear_console(self):
        self._wait()
        self._clear_console()

    def set_name(self, player, player_number):
        while True:
            name = self._view.get_input(f"Enter name for Player {player_number}: ")

            if name.strip():
                player.set_name(name)
                break

            self._view.draw_text("Name cannot be empty!")

    def set_color(self, player, player_number):
        self._view.show_colors_for_choosing()

        while True:
            color = self._view.get_input(f"Choose color for {player.get_name()}: ").lower()

            if color in self._view.colors.get_possible_colors():
                player.set_color(color)
                break

            self._view.draw_text("Invalid color. Try again!")

    def set_symbol(self, player, player_number):
        while True:
            symbol = self._view.get_input(f"Enter 1-character symbol for {player.get_name()}: ")

            if len(symbol) == 1 and symbol != " ":
                player.set_symbol(symbol)
                break

            self._view.draw_text("Symbol must be exactly 1 character and not a space!")

    def start(self):
        self._view.draw_text("Four in the row\n\n")

        for index in range(len(self.players)):
            player = self.players[index]
            index += 1

            self.set_name(player, index)
            self.set_color(player, index)
            self.set_symbol(player, index)

            self._view.draw_text("\n")

        self._clear_console()
        self.loop()

    def loop(self):
        turn = 0

        while not self._field.is_full():
            player = self.players[turn]

            self._view.draw_field(self._field.get_field(), self.players)
            self._view.draw_text(f"Turn of the {'first' if turn == 0 else 'second'} player ({player.get_name()}, '{player.get_symbol()}'), ")

            col_input = self._view.get_input(f"Enter column number (1-{self._field.size}): ")

            try:
                col = int(col_input)
                if col < 0 or col > self._field.size: raise IndexError
            except ValueError:
                self._view.draw_text("Column number must be an valid number!")
                self.__wait_and_clear_console()
                continue
            except IndexError:
                self._view.draw_text(f"Column number must be between 1 and {self._field.size}!")
                self.__wait_and_clear_console()
                continue

            self._clear_console()

            if self._field.drop(col - 1, player.get_symbol()):
                if self._field.check_win(player.get_symbol()):
                    self._view.draw_field(self._field.get_field(), self.players)
                    self._view.draw_text(f"{player.get_name()} ({player.get_symbol()}) wins!")
                    return
                turn = 1 if turn == 0 else 0
            else:
                self._view.draw_text(f"Column is already taken!")
                self.__wait_and_clear_console()

        self._view.draw_text(f"Draw!")