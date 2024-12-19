from mazes.grids.basic_grid import BasicGrid


class BaseMaze:
    def __init__(self, rows, cols) -> None:
        self.grid: BasicGrid = BasicGrid(rows, cols)

    def __str__(self) -> str:
        return str(self.grid)
