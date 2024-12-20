from collections import defaultdict
from typing import Dict

DistanceType = Dict["BasicCell", int]  # type: ignore[name-defined]
# -- see tox.ini for reasoning of this heap of mess


class Distances:
    def __init__(self, root: "BasicCell") -> None:  # type: ignore[name-defined]
        self.root = root
        self.cells: defaultdict["BasicCell", int] = defaultdict(int)  # type: ignore[name-defined]
        self.cells[root] = 0

    def __getitem__(self, cell: "BasicCell") -> int:  # type: ignore[name-defined]
        return self.cells[cell]

    def set_distance(self, cell: "BasicCell", distance: int) -> None:  # type: ignore[name-defined]
        self.cells[cell] = distance

    def get_cells(self) -> list["BasicCell"]:  # type: ignore[name-defined]
        return list(self.cells.keys())

    def path_to(self, goal_cell: "BasicCell") -> "Distances":  # type: ignore[name-defined]
        current = goal_cell

        breadcrumbs = Distances(self.root)
        breadcrumbs.cells[current] = self.cells[current]

        while current != self.root:
            for neighbor in current.links:
                if self.cells[neighbor] < self.cells[current]:
                    breadcrumbs.cells[neighbor] = self.cells[neighbor]
                    current = neighbor

        return breadcrumbs

    def max(self) -> tuple["BasicCell", int]:  # type: ignore[name-defined]
        max_distance = 0
        max_cell = self.root

        for cell, distance in self.cells.items():
            if distance > max_distance:
                max_cell = cell
                max_distance = distance

        return max_cell, max_distance
