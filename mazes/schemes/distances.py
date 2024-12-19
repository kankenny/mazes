from typing import Dict

from mazes.cells.basic_cell import BasicCell

DistanceType = Dict[BasicCell, int]


class Distances:
    def __init__(self, root: BasicCell) -> None:
        self.root = root
        self.cells: DistanceType = {}
        self.cells[self.root] = 0

    def __getitem__(self, cell: BasicCell) -> int:
        return self.cells[cell]

    def set_distance(self, cell: BasicCell, distance: int) -> None:
        self.cells[self.root] = distance

    def get_cells(self) -> list[BasicCell]:
        return list(self.cells.keys())
