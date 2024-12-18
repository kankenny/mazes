from mazes.cells.basic_cell import BasicCell


def test_cell_init() -> None:
    c = BasicCell(1, 2)

    assert c.row == 1 and c.col == 2
    assert (
        c.north_cell is None
        and c.south_cell is None
        and c.east_cell is None
        and c.west_cell is None
    )

    assert len(c.links) == 0 and len(c.neighbors) == 0
