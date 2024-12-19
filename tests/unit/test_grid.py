from mazes.cells.basic_cell import BasicCell
from mazes.grids.basic_grid import BasicGrid


def test_basic_grid() -> None:
    SIZE = 5

    grid = BasicGrid(SIZE, SIZE)

    assert len(grid) == (SIZE * SIZE)

    for cell in grid:
        assert isinstance(cell, BasicCell)
