from mazes.mazes.sidewinder import Sidewinder


def test_sidewinder():
    maze = Sidewinder(10, 10)

    assert maze is not None

    print(maze)
