from mazes.grids.colored_grid import ColoredGrid
from mazes.mazes.binary_tree import BinaryTree


def test_colored_grid():
    grid = ColoredGrid(10, 10)
    maze = BinaryTree(grid)()

    start_coord = maze.rows // 2, maze.cols // 2
    start = maze[start_coord]

    distances = start.distances()
    maze.distances = distances

    print("Flood fill:")
    print(maze)
    maze.to_png(output_name="colored_maze.png")
