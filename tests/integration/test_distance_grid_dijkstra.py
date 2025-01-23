from mazes.grids.distance_grid import DistanceGrid
from mazes.mazes import BinaryTree


def test_distance_grid_dijkstra():
    grid = DistanceGrid(10, 10)
    maze = BinaryTree(grid)()

    start_coord = 0, 0
    start = grid[start_coord]
    distances = start.distances()

    maze.distances = distances
    print(maze)
    maze.to_png(
        output_name="examples/mazes/solved_dijkstra_binary_tree.png",
        display_distances=True,
        cell_size=30,
    )

    sw_coord = grid.rows - 1, 0
    print("Path from NW corner to SW corner:")
    maze.distances = distances.path_to(grid[sw_coord])
    print(maze)
    maze.to_png(
        output_name="examples/mazes/solved_dijkstra_binary_tree_1.png",
        display_distances=True,
        cell_size=30,
    )


def test_max_distance_dijkstra():
    grid = DistanceGrid(10, 10)
    maze = BinaryTree(grid)()

    start_coord = 0, 0
    start = grid[start_coord]
    distances = start.distances()
    new_start, _ = distances.max()

    new_distances = new_start.distances()
    goal, distance = new_distances.max()

    print("A longest path in the maze:")
    maze.distances = new_distances.path_to(goal)
    print(maze)
    maze.to_png(
        output_name="examples/mazes/dijkstra_longest_path.png",
        display_distances=True,
        cell_size=30,
    )
