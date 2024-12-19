from mazes.mazes.sidewinder import Sidewinder


def test_sidewinder():
    maze = Sidewinder(100, 100)

    assert maze is not None

    print(maze)
    maze.to_png(output_name="sidewinder.png")
