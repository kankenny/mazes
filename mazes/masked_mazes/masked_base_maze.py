from mazes.grids import MaskedGrid


class MaskedBaseMaze:
    def __init__(self, grid: MaskedGrid) -> None:
        self.grid = grid

    def __str__(self) -> str:
        return str(self.grid)

    def to_png(self, output_name: str = "maze.png") -> None:
        self.grid.to_png(output_name=output_name)
