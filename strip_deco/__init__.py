from inspect import isfunction, ismethod
from typing import Callable, Any


def is_valid_function(obj: Any) -> bool:
    return isfunction(obj) or ismethod(obj)


def stripdeco(obj: Any, depth: int = None, **kwargs) -> Callable:
    if not is_valid_function(obj=obj) or depth and depth == 0:
        return obj()

    try:
        self = obj.__self__
    except AttributeError:
        pass

    while True:
        if depth is not None:
            if depth <= 0:
                break
            else:
                depth -= 1

        try:
            obj = obj.__closure__[0].cell_contents
        except TypeError:
            break

    try:
        return obj(**kwargs)
    except TypeError:
        return obj(self, **kwargs)


__all__ = ["stripdeco"]
