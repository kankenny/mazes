from mazes.schemes.distances import Distances

from .basic_grid import BasicGrid


class ColoredGrid(BasicGrid):
    def __init__(self, rows: int, cols: int) -> None:
        super().__init__(rows, cols)
        self.distances = None

    @property
    def distances(self) -> Distances | None:
        return self._distances

    @distances.setter
    def distances(self, distances: Distances) -> None:
        self._distances = distances

    def background_color_for(self, cell):
        farthest_cell, max_dist = self.distances.max()

        distance = self.distances.cells[cell] if cell in self.distances.cells else None
        intensity = (max_dist - distance) / max_dist

        dark = round(255 * intensity)
        bright = 128 + round(127 * intensity)

        return dark, dark, bright
