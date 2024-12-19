import random

from mazes.mazes.base_maze import BaseMaze


class BinaryTree(BaseMaze):
    def __init__(self, rows: int, cols: int) -> None:
        super().__init__(rows, cols)

        for cell in self.grid.iter_each_cell():
            neighbors = []

            if cell.north_cell:
                neighbors.append(cell.north_cell)
            if cell.east_cell:
                neighbors.append(cell.east_cell)

            if len(neighbors) != 0:
                neighbor = random.sample(neighbors, k=1)[0]

            if neighbor:
                cell.link(neighbor)
