# strip-deco
[![license]](/LICENSE)
[![pypi]](https://pypi.org/project/strip-deco/)
[![pyversions]](http://pypi.python.org/pypi/strip-deco)
![badge](https://action-badges.now.sh/teamhide/strip-deco)
[![Downloads](https://pepy.tech/badge/strip-deco)](https://pepy.tech/project/strip-deco)

---

**strip-deco** easily strip decorator from function or class method

## Installation

```python
pip3 install strip-deco
```

## Example of function decorator
```python
from strip_deco import stripdeco


def deco(func):
    def _deco(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return _deco
    
@deco
def test():
    pass
    

stripdeco(obj=test)


@deco
@deco
@deco
def test():
    pass
    

stripdeco(obj=test)
```

## Example of class decorator
```python
from strip_deco import stripdeco


class Deco:
    def __call__(self, func):
        def deco(*args, **kwargs):
            return func(*args, **kwargs)
        return deco
       
 
@Deco()
def test():
    pass
    
    
stripdeco(obj=test)


@Deco()
@Deco()
@Deco()
def test():
    pass


stripdeco(obj=test, depth=2)
```

## Example of class method
```python
from strip_deco import stripdeco


def deco(func):
    def _deco(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return _deco


class Service:
    @deco
    def run(self):
        pass
    
    @deco
    def run_with_arguments(self, user_id):
        pass


        
        
stripdeco(obj=Service().run)
stripdeco(obj=Service().run_with_arguments, user_id=1)  # Case of other arguments
```

## Example of class method with init
```python
from strip_deco import stripdeco


def deco(func):
    def _deco(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return _deco


class Service:
    def __init__(self, repo):
        self.repo = repo

    @deco
    def run(self):
        pass
    
    @deco
    def run_with_arguments(self, user_id):
        pass


        
        
stripdeco(obj=Service(repo="repo").run)
stripdeco(obj=Service(repo="repo").run_with_arguments, user_id=1)  # Case of other arguments
```

- strip-deco automatically removes  any kind of decorators. (class/function)
- It supports both decorator,`functools wraps` and non functools wraps .
- If you specify depth paramater, it will strip order by outside.
- The class argument is required when executing class method.


[license]: https://img.shields.io/badge/License-GPLv3-blue.svg
[pypi]: https://img.shields.io/pypi/v/strip-deco
[pyversions]: https://img.shields.io/pypi/pyversions/strip-deco