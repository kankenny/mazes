import random

from mazes.grids.colored_grid import ColoredGrid
from mazes.mazes import AldousBroder, BinaryTree, Sidewinder


def test_gif_maze():
    colors = [
        "reds",
        "blues",
        "yellows",
        "greens",
        "purples",
        "oranges",
        "whites",
        "blacks",
    ]

    for color in colors:
        grid = ColoredGrid(25, 25)

        maze_generator = random.choice([AldousBroder, BinaryTree, Sidewinder])
        maze = maze_generator(grid)()

        start_coord = maze.rows // 2, maze.cols // 2
        start = maze[start_coord]

        distances = start.distances()
        maze.distances = distances
        maze.to_gif(output_name=f"examples/gif_maze_{color}.gif", cell_color=color, display_distances=True)
