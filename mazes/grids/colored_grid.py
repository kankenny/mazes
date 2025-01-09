from mazes.heuristics.distances import Distances

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

    def background_color_for(self, cell, c=(255, 0, 0)):
        farthest_cell, max_dist = self.distances.max()

        distance = self.distances.cells.get(cell, 0.1)
        intensity = distance / max_dist

        r = round((1 - intensity) * 255 + intensity * c[0])
        g = round((1 - intensity) * 255 + intensity * c[1])
        b = round((1 - intensity) * 255 + intensity * c[2])

        return r, g, b
