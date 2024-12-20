from mazes.grids.basic_grid import BasicGrid
from mazes.mazes.binary_tree import BinaryTree


def test_binary_tree():
    grid = BasicGrid(5, 5)
    maze = BinaryTree(grid)()

    assert maze is not None

    print(maze)
    maze.to_png(output_name="binary_tree.png")
