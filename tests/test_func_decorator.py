from strip_deco import stripdeco
from .conftest import func_decorator_without_wraps, func_decorator_with_wraps


def test_func_deco_without_wraps():
    @func_decorator_without_wraps
    def test():
        pass

    assert test.__closure__ is not None
    orig = stripdeco(obj=test)
    assert orig.__closure__ is None


def test_func_deco_with_wraps():
    @func_decorator_with_wraps
    def test():
        pass

    assert test.__closure__ is not None
    orig = stripdeco(obj=test)
    assert orig.__closure__ is None


def test_func_deco_with_without_wraps_two_decorator():
    @func_decorator_without_wraps
    @func_decorator_without_wraps
    def test():
        pass

    assert test.__closure__ is not None
    orig = stripdeco(obj=test)
    assert orig.__closure__ is None


def test_func_deco_with_wraps_two_decorator():
    @func_decorator_with_wraps
    @func_decorator_with_wraps
    def test():
        pass

    assert test.__closure__ is not None
    orig = stripdeco(obj=test)
    assert orig.__closure__ is None


def test_func_deco_with_without_wraps_multiple_decorator():
    @func_decorator_without_wraps
    @func_decorator_without_wraps
    @func_decorator_without_wraps
    @func_decorator_without_wraps
    @func_decorator_without_wraps
    @func_decorator_without_wraps
    def test():
        pass

    assert test.__closure__ is not None
    orig = stripdeco(obj=test)
    assert orig.__closure__ is None


def test_func_deco_with_without_wraps_depth():
    @func_decorator_without_wraps
    @func_decorator_without_wraps
    @func_decorator_without_wraps
    @func_decorator_without_wraps
    def test():
        pass

    assert test.__closure__ is not None
    orig = stripdeco(obj=test, depth=1)
    assert orig.__closure__ is not None
    orig = stripdeco(obj=test, depth=2)
    assert orig.__closure__ is not None
    orig = stripdeco(obj=test, depth=3)
    assert orig.__closure__ is not None
    orig = stripdeco(obj=test, depth=4)
    assert orig.__closure__ is None


def test_func_deco_with_wraps_depth():
    @func_decorator_with_wraps
    @func_decorator_with_wraps
    @func_decorator_with_wraps
    @func_decorator_with_wraps
    def test():
        pass

    assert test.__closure__ is not None
    orig = stripdeco(obj=test, depth=1)
    assert orig.__closure__ is not None
    orig = stripdeco(obj=test, depth=2)
    assert orig.__closure__ is not None
    orig = stripdeco(obj=test, depth=3)
    assert orig.__closure__ is not None
    orig = stripdeco(obj=test, depth=4)
    assert orig.__closure__ is None
