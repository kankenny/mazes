from mazes.mazes.binary_tree import BinaryTree


def test_binary_tree():
    maze = BinaryTree(10, 10)

    assert maze is not None

    print(maze)
