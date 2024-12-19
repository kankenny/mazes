from mazes.mazes.binary_tree import BinaryTree


def test_binary_tree():
    maze = BinaryTree(100, 100)

    assert maze is not None

    print(maze)
    maze.to_png(output_name="binary_tree.png")
