from mazes.grids.basic_grid import BasicGrid
from mazes.mazes.sidewinder import Sidewinder


def test_sidewinder():
    grid = BasicGrid(10, 10)
    maze = Sidewinder(grid)()

    assert maze is not None

    print(maze)
    maze.to_png(output_name="examples/mazes/sidewinder.png")
