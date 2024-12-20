from .basic_grid import BasicGrid


class DistanceGrid(BasicGrid):
    def __init__(self, rows: int, cols: int) -> None:
        super().__init__(rows, cols)
        self.distances = None

    def contents_of(self, cell) -> str:
        if self.distances is not None and cell in self.distances.cells:
            return str_base(self.distances[cell], 36)
        else:
            return super().contents_of(cell)


# With help of https://github.com/crux888 and his similar repo
# (from https://stackoverflow.com/questions/2063425)


def str_base(number, base):
    if number < 0:
        return "-" + str_base(-number, base)
    else:
        (d, m) = divmod(number, base)
        if d:
            return str_base(d, base) + digit_to_char(m)
        else:
            return digit_to_char(m)


def digit_to_char(digit):
    if digit < 10:
        return chr(ord("0") + digit)
    else:
        return chr(ord("a") + digit - 10)
