from mazes.grids.colored_grid import ColoredGrid
from mazes.mazes.hunt_and_kill import HuntAndKill


def test_hunt_and_kill():
    grid = ColoredGrid(25, 25)
    maze = HuntAndKill(grid)()

    assert maze is not None

    start_coord = maze.rows // 2, maze.cols // 2
    start = maze[start_coord]

    distances = start.distances()
    maze.distances = distances

    print(maze)
    maze.to_png(output_name="examples/hunt_and_kill.png")
