from collections import defaultdict
from typing import Optional


class Cell:
    def __init__(self, row: int, col: int) -> None:
        self.row: int = row
        self.col: int = col

        self._north_cell: Optional["Cell"] = None
        self._south_cell: Optional["Cell"] = None
        self._east_cell: Optional["Cell"] = None
        self._west_cell: Optional["Cell"] = None

        self.neighbors: list["Cell"] = []

        self.links: defaultdict["Cell", bool] = defaultdict(bool)

    @property
    def north_cell(self) -> Optional["Cell"]:
        if self._north_cell and self._north_cell not in self.neighbors:
            self.neighbors.append(self._north_cell)
        return self._north_cell

    @north_cell.setter
    def north_cell(self, cell: Optional["Cell"]) -> None:
        self._north_cell = cell

    @property
    def south_cell(self) -> Optional["Cell"]:
        if self._south_cell and self._south_cell not in self.neighbors:
            self.neighbors.append(self._south_cell)
        return self._south_cell

    @south_cell.setter
    def south_cell(self, cell: Optional["Cell"]) -> None:
        self._south_cell = cell

    @property
    def east_cell(self) -> Optional["Cell"]:
        if self._east_cell and self._east_cell not in self.neighbors:
            self.neighbors.append(self._east_cell)
        return self._east_cell

    @east_cell.setter
    def east_cell(self, cell: Optional["Cell"]) -> None:
        self._east_cell = cell

    @property
    def west_cell(self) -> Optional["Cell"]:
        if self._west_cell and self._west_cell not in self.neighbors:
            self.neighbors.append(self._west_cell)
        return self._west_cell

    @west_cell.setter
    def west_cell(self, cell: Optional["Cell"]) -> None:
        self._west_cell = cell

    def link(self, cell: "Cell", is_bidir: bool = True) -> "Cell":
        self.links[cell] = True
        if is_bidir:
            cell.link(self, is_bidir=False)
        return self

    def unlink(self, cell: "Cell", is_bidir: bool = True) -> "Cell":
        self.links.pop(cell, None)
        if is_bidir:
            cell.unlink(self, is_bidir=False)
        return self

    def get_links(self) -> list["Cell"]:
        return list(self.links.keys())

    def is_linked(self, cell: "Cell") -> bool:
        return self.links.get(cell, False)

    def get_neighbors(self) -> list["Cell"]:
        return self.neighbors
