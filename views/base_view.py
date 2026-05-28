from abc import ABC, abstractmethod

from models.player import Player


class BaseView(ABC):
    @abstractmethod
    def draw_field(self, field: list[list[str]], players: list[Player]) -> None: pass
    @abstractmethod
    def draw_text(self, text: str) -> None: pass

    @abstractmethod
    def get_input(self, prompt: str) -> str: pass