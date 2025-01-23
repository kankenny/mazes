from mazes.grids.basic_grid import BasicGrid
from mazes.mazes import AldousBroder, BinaryTree, HuntAndKill, Sidewinder, Wilson


def test_deadends():
    maze_algorithms = [AldousBroder, BinaryTree, Sidewinder, HuntAndKill, Wilson]
    maze_dim = 25

    maze_averages = {}

    sample_size = 100

    for maze_alg in maze_algorithms:
        print("Running: ", maze_alg.__name__)

        deadend_counts = []

        for _ in range(sample_size):
            grid = BasicGrid(maze_dim, maze_dim)
            maze = maze_alg(grid)()
            deadend_counts.append(len(maze.dead_ends()))

        total_deadends = sum(deadend_counts)
        average_deadends = total_deadends / sample_size
        maze_averages[maze_alg.__name__] = average_deadends

    total_cells = maze_dim * maze_dim
    print(f"\nAverage deadends per {maze_dim}x{maze_dim} maze ({total_cells} cells):")

    for maze, average in sorted(
        maze_averages.items(), key=lambda item: item[1], reverse=True
    ):
        percentage = (average * 100) / total_cells
        print(f"{maze:<15} {average:6.2f}/625     ({percentage:.2f}%)")
