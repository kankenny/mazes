from mazes.cells.basic_cell import BasicCell
from mazes.grids.basic_grid import BasicGrid


def test_basic_grid() -> None:
    thicknesses = [1, 2, 3]

    for thickness in thicknesses:
        SIZE = 10

        grid = BasicGrid(SIZE, SIZE)

        start_coord = 0, 0
        sample_cell = grid[start_coord]
        print(sample_cell, repr(sample_cell))

        assert len(grid) == (SIZE * SIZE)

        for cell in grid:
            assert isinstance(cell, BasicCell)

        grid.to_png(
            output_name=f"examples/grids/grid_{thickness}.png", wall_thickness=thickness
        )
