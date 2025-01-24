maze_registry = []


def maze_profiler(cls):
    from mazes.masked_mazes.masked_base_maze import (
        MaskedBaseMaze,
    )  # not importing on the module level to prevent circular imports
    from mazes.mazes.base_maze import BaseMaze

    """
    Decorator to register maze algorithms that subclass BaseMaze or MaskedBaseMaze.
    """
    if issubclass(cls, BaseMaze) or issubclass(cls, MaskedBaseMaze):
        maze_registry.append(cls)
    else:
        raise TypeError(
            f"{cls.__name__} is not a subclass of BaseMaze or MaskedBaseMaze"
        )
    return cls
