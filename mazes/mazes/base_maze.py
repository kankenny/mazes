from mazes.grids import BasicGrid


class BaseMaze:
    def __init__(self, grid: BasicGrid) -> None:
        self.grid = grid

    def __str__(self) -> str:
        return str(self.grid)

    def to_png(self, output_name: str = "maze.png") -> None:
        self.grid.to_png(output_name=output_name)
