from inspect import isfunction, ismethod
from typing import Callable, Any


def is_valid_function(obj: Any) -> bool:
    return isfunction(obj) or ismethod(obj)


def stripdeco(obj: Any, depth: int = None) -> Callable:
    if not is_valid_function(obj=obj):
        return obj

    if depth == 0:
        return obj

    while True:
        if depth is not None:
            if depth <= 0:
                return obj
            else:
                depth -= 1

        try:
            obj = obj.__closure__[0].cell_contents
        except TypeError:
            break

    return obj


__all__ = ["stripdeco"]
