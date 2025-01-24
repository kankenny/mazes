from mazes.grids.masked_grid import Mask, MaskedGrid
from mazes.masked_mazes import MaskedAldousBroder


def test_mask():
    mask = Mask(10, 10)

    mask[0, 0] = False
    mask[2, 2] = False
    mask[4, 4] = False

    grid = MaskedGrid(mask)
    maze = MaskedAldousBroder(grid)()

    assert maze is not None

    print(maze)
    maze.to_png(output_name="examples/masked_mazes/basic_mask.png")
