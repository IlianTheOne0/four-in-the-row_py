from controllers.base_controller import BaseController
from views.tkinter_view import TkinterView


class TkinterController(BaseController):
    def __init__(self, view: TkinterView) -> None:
        super().__init__(view)

        self._view = view
        self._turn = 0

    def set_name(self, player, player_number):
        while True:
            name = self._view.get_input(f"Enter name for Player {player_number}: ")

            if name.strip():
                player.set_name(name)
                break

            self._view.draw_text("Name cannot be empty!")

    def set_color(self, player, player_number):
        while True:
            color = self._view.get_input(f"Choose color for {player.get_name()}:\n({self._view.colors.get_possible_colors().keys()})").lower()
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
        for index in range(len(self.players)):
            player = self.players[index]
            index += 1

            self.set_name(player, index)
            self.set_color(player, index)
            self.set_symbol(player, index)

        self.loop()

    def loop(self):
        self._view.draw_field(self._field.get_field(), self.players)
        self._view.bind_click(self.make_move)
        self._view.root.mainloop()

    def make_move(self, col_index: int):
        player = self.players[self._turn]

        if self._field.drop(col_index, player.get_symbol()):
            self._view.draw_field(self._field.get_field(), self.players)

            if self._field.check_win(player.get_symbol()):
                self._view.draw_text(f"{player.get_name()} ({player.get_symbol()}) wins!")
                self._view.root.destroy()
                return

            if self._field.is_full():
                self._view.draw_text("Draw!")
                self._view.root.destroy()
                return

            self._turn = 1 if self._turn == 0 else 0
        else:
            self._view.draw_text("Column is already full!")