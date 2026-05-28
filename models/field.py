class Field:
    def __init__(self, size: int = 8):
        self.size = size
        self.__field = [[" " for _ in range(size)] for _ in range(size)]

    def get_field(self):
        result = []

        for row in self.__field:
            new_row = []
            for cell in row:
                new_row.append(cell)
            result.append(new_row)

        return result

    def drop(self, col: int, symbol: str) -> bool:
        if col < 0 or col >= self.size: return False

        for row in range(self.size - 1, -1, -1):
            if self.__field[row][col] == " ":
                self.__field[row][col] = symbol
                return True

        return False

    def is_full(self) -> bool:
        for col in range(self.size):
            if self.__field[0][col] == " ":
                return False

        return True

    def check_win(self, symbol: str) -> bool:
        for row in range(self.size):
            for col in range(self.size - 3):
                if (
                    self.__field[row][col] == symbol and
                    self.__field[row][col + 1] == symbol and
                    self.__field[row][col + 2] == symbol and
                    self.__field[row][col + 3] == symbol
                ):
                    return True

        for row in range(self.size - 3):
            for col in range(self.size - 3):
                if (
                    self.__field[row][col] == symbol and
                    self.__field[row + 1][col] == symbol and
                    self.__field[row + 2][col] == symbol and
                    self.__field[row + 3][col] == symbol
                ):
                    return True

        for row in range(self.size - 3):
            for col in range(self.size - 3):
                if (
                    self.__field[row][col] == symbol and
                    self.__field[row + 1][col + 1] == symbol and
                    self.__field[row + 2][col + 2] == symbol and
                    self.__field[row + 3][col + 3] == symbol
                ):
                    return True

        for row in range(3, self.size):
            for col in range(self.size - 3):
                if (
                    self.__field[row][col] == symbol and
                    self.__field[row - 1][col + 1] == symbol and
                    self.__field[row - 2][col + 2] == symbol and
                    self.__field[row - 3][col + 3] == symbol
                ):
                    return True
                
        return False