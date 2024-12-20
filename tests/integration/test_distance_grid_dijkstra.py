from mazes.grids.distance_grid import DistanceGrid
from mazes.mazes.binary_tree import BinaryTree


def test_distance_grid_dijkstra():
    grid = DistanceGrid(10, 10)
    maze = BinaryTree(grid)()

    start_coord = 0, 0
    start = grid[start_coord]
    distances = start.distances()

    maze.distances = distances
    print(maze)
    maze.to_png(output_name="solved_dijkstra_binary_tree.png")
