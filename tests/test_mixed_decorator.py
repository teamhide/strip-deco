from strip_deco import stripdeco, run_after_strip
from .conftest import (
    ClassDecoratorWithWraps,
    ClassDecoratorWithoutWraps,
    func_decorator_with_wraps,
    func_decorator_without_wraps,
)


def test_stripdeco_mixed_class_with_wrap_and_func_with_wrap():
    @ClassDecoratorWithWraps()
    @func_decorator_with_wraps
    def test():
        pass

    assert test.__closure__ is not None
    orig = stripdeco(obj=test)
    assert orig.__closure__ is None


def test_stripdeco_mixed_class_without_wrap_and_func_without_wrap():
    @ClassDecoratorWithoutWraps()
    @func_decorator_without_wraps
    def test():
        pass

    assert test.__closure__ is not None
    orig = stripdeco(obj=test)
    assert orig.__closure__ is None


def test_stripdeco_mixed_class_with_wrap_and_func_without_wrap():
    @ClassDecoratorWithWraps()
    @func_decorator_without_wraps
    def test():
        pass

    assert test.__closure__ is not None
    orig = stripdeco(obj=test)
    assert orig.__closure__ is None


def test_stripdeco_mixed_class_without_wrap_and_func_with_wrap():
    @ClassDecoratorWithWraps()
    @func_decorator_without_wraps
    def test():
        pass

    assert test.__closure__ is not None
    orig = stripdeco(obj=test)
    assert orig.__closure__ is None


def test_stripdeco_mixed_class_with_wrap_and_func_with_wrap_depth():
    @ClassDecoratorWithWraps()
    @func_decorator_with_wraps
    @ClassDecoratorWithWraps()
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


def test_stripdeco_mixed_class_without_wrap_and_func_without_wrap_depth():
    @ClassDecoratorWithoutWraps()
    @func_decorator_without_wraps
    @ClassDecoratorWithoutWraps()
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


def test_stripdeco_mixed_class_with_wrap_and_func_without_wrap_depth():
    @ClassDecoratorWithWraps()
    @func_decorator_without_wraps
    @ClassDecoratorWithWraps()
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


def test_stripdeco_mixed_class_without_wrap_and_func_with_wrap_depth():
    @ClassDecoratorWithWraps()
    @func_decorator_without_wraps
    @ClassDecoratorWithWraps()
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


def test_run_after_strip_mixed_class_with_wrap_and_func_with_wrap():
    @ClassDecoratorWithWraps()
    @func_decorator_with_wraps
    def test():
        return 1

    assert test.__closure__ is not None
    orig = run_after_strip(obj=test)
    assert orig == 1


def test_run_after_strip_mixed_class_without_wrap_and_func_without_wrap():
    @ClassDecoratorWithoutWraps()
    @func_decorator_without_wraps
    def test():
        return 1

    assert test.__closure__ is not None
    orig = run_after_strip(obj=test)
    assert orig == 1


def test_run_after_strip_mixed_class_with_wrap_and_func_without_wrap():
    @ClassDecoratorWithWraps()
    @func_decorator_without_wraps
    def test():
        return 1

    assert test.__closure__ is not None
    orig = run_after_strip(obj=test)
    assert orig == 1


def test_run_after_strip_mixed_class_without_wrap_and_func_with_wrap():
    @ClassDecoratorWithWraps()
    @func_decorator_without_wraps
    def test():
        return 1

    assert test.__closure__ is not None
    orig = run_after_strip(obj=test)
    assert orig == 1


def test_run_after_strip_mixed_class_with_wrap_and_func_with_wrap_depth():
    @ClassDecoratorWithWraps()
    @func_decorator_with_wraps
    @ClassDecoratorWithWraps()
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


def test_run_after_strip_mixed_class_without_wrap_and_func_without_wrap_depth():
    @ClassDecoratorWithoutWraps()
    @func_decorator_without_wraps
    @ClassDecoratorWithoutWraps()
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


def test_run_after_strip_mixed_class_with_wrap_and_func_without_wrap_depth():
    @ClassDecoratorWithWraps()
    @func_decorator_without_wraps
    @ClassDecoratorWithWraps()
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


def test_run_after_strip_mixed_class_without_wrap_and_func_with_wrap_depth():
    @ClassDecoratorWithWraps()
    @func_decorator_without_wraps
    @ClassDecoratorWithWraps()
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
