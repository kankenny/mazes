from mazes.mazes.base_maze import BaseMaze

maze_registry = []


def maze_profiler(cls):
    """
    Decorator to register maze algorithms that subclass BaseMaze.
    """
    if issubclass(cls, BaseMaze):
        maze_registry.append(cls)
    else:
        raise TypeError(f"{cls.__name__} is not a subclass of BaseMaze")
    return cls
