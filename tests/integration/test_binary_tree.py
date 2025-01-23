from mazes.grids import BasicGrid
from mazes.mazes import BinaryTree


def test_binary_tree():
    grid = BasicGrid(10, 10)
    maze = BinaryTree(grid)()

    assert maze is not None

    print(maze)
    maze.to_png(output_name="examples/mazes/binary_tree.png")
