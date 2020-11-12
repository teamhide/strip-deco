from strip_deco import stripdeco, run_after_strip
from .conftest import func_decorator_without_wraps, func_decorator_with_wraps


def test_stripdeco_func_deco_without_wraps():
    @func_decorator_without_wraps
    def test():
        pass

    assert test.__closure__ is not None
    orig = stripdeco(obj=test)
    assert orig.__closure__ is None


def test_stripdeco_func_deco_with_wraps():
    @func_decorator_with_wraps
    def test():
        pass

    assert test.__closure__ is not None
    orig = stripdeco(obj=test)
    assert orig.__closure__ is None


def test_stripdeco_func_deco_with_without_wraps_two_decorator():
    @func_decorator_without_wraps
    @func_decorator_without_wraps
    def test():
        pass

    assert test.__closure__ is not None
    orig = stripdeco(obj=test)
    assert orig.__closure__ is None


def test_stripdeco_func_deco_with_wraps_two_decorator():
    @func_decorator_with_wraps
    @func_decorator_with_wraps
    def test():
        pass

    assert test.__closure__ is not None
    orig = stripdeco(obj=test)
    assert orig.__closure__ is None


def test_stripdeco_func_deco_with_without_wraps_multiple_decorator():
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


def test_stripdeco_func_deco_with_without_wraps_depth():
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


def test_stripdeco_func_deco_with_wraps_depth():
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


def test_run_after_strip_func_deco_without_wraps():
    @func_decorator_without_wraps
    def test():
        return 1

    assert test.__closure__ is not None
    orig = run_after_strip(obj=test)
    assert orig == 1


def test_run_after_strip_func_deco_with_wraps():
    @func_decorator_with_wraps
    def test():
        return 1

    assert test.__closure__ is not None
    orig = run_after_strip(obj=test)
    assert orig == 1


def test_run_after_strip_func_deco_with_without_wraps_two_decorator():
    @func_decorator_without_wraps
    @func_decorator_without_wraps
    def test():
        return 1

    assert test.__closure__ is not None
    orig = run_after_strip(obj=test)
    assert orig == 1


def test_run_after_strip_func_deco_with_wraps_two_decorator():
    @func_decorator_with_wraps
    @func_decorator_with_wraps
    def test():
        return 1

    assert test.__closure__ is not None
    orig = run_after_strip(obj=test)
    assert orig == 1


def test_run_after_strip_func_deco_with_without_wraps_multiple_decorator():
    @func_decorator_without_wraps
    @func_decorator_without_wraps
    @func_decorator_without_wraps
    @func_decorator_without_wraps
    @func_decorator_without_wraps
    @func_decorator_without_wraps
    def test():
        return 1

    assert test.__closure__ is not None
    orig = run_after_strip(obj=test)
    assert orig == 1


def test_run_after_strip_func_deco_with_without_wraps_depth():
    @func_decorator_without_wraps
    @func_decorator_without_wraps
    @func_decorator_without_wraps
    @func_decorator_without_wraps
    def test():
        return 1

    assert test.__closure__ is not None
    orig = run_after_strip(obj=test, depth=1)
    assert orig == 1
    orig = run_after_strip(obj=test, depth=2)
    assert orig == 1
    orig = run_after_strip(obj=test, depth=3)
    assert orig == 1
    orig = run_after_strip(obj=test, depth=4)
    assert orig == 1


def test_run_after_strip_func_deco_with_wraps_depth():
    @func_decorator_with_wraps
    @func_decorator_with_wraps
    @func_decorator_with_wraps
    @func_decorator_with_wraps
    def test():
        return 1

    assert test.__closure__ is not None
    orig = run_after_strip(obj=test, depth=1)
    assert orig == 1
    orig = run_after_strip(obj=test, depth=2)
    assert orig == 1
    orig = run_after_strip(obj=test, depth=3)
    assert orig == 1
    orig = run_after_strip(obj=test, depth=4)
    assert orig == 1
