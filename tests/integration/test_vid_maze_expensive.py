from mazes.grids.colored_grid import ColoredGrid
from mazes.mazes import AldousBroder


def test_colored_grid():
    grid = ColoredGrid(10, 10)

    maze = AldousBroder(grid)()

    start_coord = maze.rows // 2, maze.cols // 2
    start = maze[start_coord]

    distances = start.distances()
    maze.distances = distances
    maze.to_vid(output_name="examples/vid_maze.mp4", display_distances=True)
