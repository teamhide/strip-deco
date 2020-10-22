from functools import wraps


def func_decorator_without_wraps(func):
    def _func_deco(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return _func_deco


def func_decorator_with_wraps(func):
    @wraps(func)
    def _func_deco(*args, **kwargs):
        return func(*args, **kwargs)

    return _func_deco


class ClassDecoratorWithoutWraps:
    def __call__(self, func):
        def decorator(*args, **kwargs):
            return func(*args, **kwargs)

        return decorator


class ClassDecoratorWithWraps:
    def __call__(self, func):
        @wraps(func)
        def decorator(*args, **kwargs):
            return func(*args, **kwargs)

        return decorator
