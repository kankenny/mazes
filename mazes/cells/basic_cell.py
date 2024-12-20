from collections import defaultdict
from typing import Optional

from mazes.schemes.distances import Distances


class BasicCell:
    def __init__(self, row: int, col: int) -> None:
        self.row: int = row
        self.col: int = col

        self._north_cell: Optional["BasicCell"] = None
        self._south_cell: Optional["BasicCell"] = None
        self._east_cell: Optional["BasicCell"] = None
        self._west_cell: Optional["BasicCell"] = None

        self.neighbors: list["BasicCell"] = []

        self.links: defaultdict["BasicCell", bool] = defaultdict(bool)

    def __str__(self) -> str:
        return f"Basic Cell: at row={self.row} and col={self.col}"

    def __repr__(self) -> str:
        return f"BasicCell(row={self.row}, col={self.col})"

    @property
    def north_cell(self) -> Optional["BasicCell"]:
        if self._north_cell and self._north_cell not in self.neighbors:
            self.neighbors.append(self._north_cell)
        return self._north_cell

    @north_cell.setter
    def north_cell(self, cell: Optional["BasicCell"]) -> None:
        self._north_cell = cell

    @property
    def south_cell(self) -> Optional["BasicCell"]:
        if self._south_cell and self._south_cell not in self.neighbors:
            self.neighbors.append(self._south_cell)
        return self._south_cell

    @south_cell.setter
    def south_cell(self, cell: Optional["BasicCell"]) -> None:
        self._south_cell = cell

    @property
    def east_cell(self) -> Optional["BasicCell"]:
        if self._east_cell and self._east_cell not in self.neighbors:
            self.neighbors.append(self._east_cell)
        return self._east_cell

    @east_cell.setter
    def east_cell(self, cell: Optional["BasicCell"]) -> None:
        self._east_cell = cell

    @property
    def west_cell(self) -> Optional["BasicCell"]:
        if self._west_cell and self._west_cell not in self.neighbors:
            self.neighbors.append(self._west_cell)
        return self._west_cell

    @west_cell.setter
    def west_cell(self, cell: Optional["BasicCell"]) -> None:
        self._west_cell = cell

    def link(self, cell: "BasicCell", is_bidir: bool = True) -> "BasicCell":
        self.links[cell] = True
        if is_bidir:
            cell.link(self, is_bidir=False)
        return self

    def unlink(self, cell: "BasicCell", is_bidir: bool = True) -> "BasicCell":
        self.links.pop(cell, None)
        if is_bidir:
            cell.unlink(self, is_bidir=False)
        return self

    def get_links(self) -> list["BasicCell"]:
        return list(self.links.keys())

    def is_linked(self, cell: "BasicCell") -> bool:
        return self.links.get(cell, False)

    def get_neighbors(self) -> list["BasicCell"]:
        return self.neighbors

    def distances(self) -> Distances:
        distances = Distances(root=self)
        frontier = [self]

        while len(frontier) != 0:
            new_frontier = []

            for cell in frontier:
                for linked_cell in cell.get_links():
                    if linked_cell in distances.cells:
                        continue

                    distances.set_distance(linked_cell, distances[cell] + 1)
                    new_frontier.append(linked_cell)

            frontier = new_frontier

        return distances
