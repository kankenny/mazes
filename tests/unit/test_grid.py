from mazes.cells.basic_cell import BasicCell
from mazes.grids.basic_grid import BasicGrid


def test_basic_grid() -> None:
    thicknesses = [0.5, 1, 1.5]

    for thickness in thicknesses:
        SIZE = 10

        grid = BasicGrid(SIZE, SIZE)

        start_coord = 0, 0
        sample_cell = grid[start_coord]
        print(sample_cell, repr(sample_cell))

        assert len(grid) == (SIZE * SIZE)

        for cell in grid:
            assert isinstance(cell, BasicCell)

        grid.to_png(output_name=f"examples/maze_{thickness}.png")
