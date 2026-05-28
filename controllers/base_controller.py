from abc import ABC, abstractmethod

from models.player import Player
from views.base_view import BaseView

from models.field import Field

class BaseController(ABC):
    def __init__(self, view: BaseView):
        self._view = view
        self._field = Field(size=8)

        self._player1 = Player()
        self._player2 = Player()
        self.players = [self._player1, self._player2]

    @abstractmethod
    def start(self): pass
    @abstractmethod
    def loop(self): pass

    @abstractmethod
    def set_color(self, player, player_number): pass
    @abstractmethod
    def set_name(self, player, player_number): pass
    @abstractmethod
    def set_symbol(self, player, player_number): pass