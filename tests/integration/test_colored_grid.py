import random

from mazes.grids.colored_grid import ColoredGrid
from mazes.mazes import AldousBroder, BinaryTree, Sidewinder


def test_colored_grid():
    colors = ["reds", "blues", "yellows", "greens", "purples", "oranges", "whites", "blacks"]

    for color in colors:
        grid = ColoredGrid(25, 25)

        maze_generator = random.choice([AldousBroder, BinaryTree, Sidewinder])
        maze = maze_generator(grid)()

        start_coord = maze.rows // 2, maze.cols // 2
        start = maze[start_coord]

        distances = start.distances()
        maze.distances = distances
        maze.to_png(output_name=f"examples/colored_maze_{color}.png", cell_color=color)