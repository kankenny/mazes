from collections import defaultdict
from typing import Dict

DistanceType = Dict["BasicCell", int]  # type: ignore[name-defined]
# -- see tox.ini


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
