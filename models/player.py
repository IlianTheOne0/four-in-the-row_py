class Player:
    def __init__(self):
        self.__name = ""
        self.__symbol = ""
        self.__color = ""

    def set_name(self, name:str) -> None: self.__name = name if name and name.strip() else self.__name
    def get_name(self) -> str: return self.__name

    def set_color(self, color:str) -> None: self.__color = color if color else self.__color
    def get_color(self) -> str: return self.__color

    def set_symbol(self, symbol:str) -> None: self.__symbol = symbol if symbol and len(symbol) == 1 else self.__symbol
    def get_symbol(self) -> str: return self.__symbol