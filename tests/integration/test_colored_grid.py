from mazes.grids.colored_grid import ColoredGrid
from mazes.mazes.binary_tree import BinaryTree


def test_colored_grid():
    grid = ColoredGrid(25, 25)
    maze = BinaryTree(grid)()

    start_coord = maze.rows // 2, maze.cols // 2
    start = maze[start_coord]

    distances = start.distances()
    maze.distances = distances

    colors = ["reds", "blues", "yellows", "greens", "purples", "oranges", "blacks"]

    for color in colors:
        maze.to_png(output_name=f"colored_maze_{color}.png", cell_color=color)
