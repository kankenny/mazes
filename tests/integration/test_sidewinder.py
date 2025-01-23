from mazes.grids import BasicGrid
from mazes.mazes import Sidewinder


def test_sidewinder():
    grid = BasicGrid(10, 10)
    maze = Sidewinder(grid)()

    assert maze is not None

    print(maze)
    maze.to_png(output_name="examples/mazes/sidewinder.png")
