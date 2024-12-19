import random

from mazes.grids.basic_grid import BasicGrid


class BinaryTree:
    def __init__(self, grid) -> None:
        self.grid: BasicGrid = grid

        for cell in self.grid.iter_each_cell():
            neighbors = []

            if cell.north_cell:
                neighbors.append(cell.north_cell)
            if cell.east_cell:
                neighbors.append(cell.east_cell)

            neighbor = random.sample(neighbors, k=1)[0]

            if neighbor:
                cell.link(neighbor)
