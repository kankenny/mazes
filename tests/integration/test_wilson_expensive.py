from mazes.grids import ColoredGrid
from mazes.mazes import Wilson


def test_wilson():
    grid = ColoredGrid(25, 25)
    maze = Wilson(grid)()

    assert maze is not None

    start_coord = maze.rows // 2, maze.cols // 2
    start = maze[start_coord]

    distances = start.distances()
    maze.distances = distances

    print(maze)
    maze.to_png(output_name="examples/mazes/wilson.png")
