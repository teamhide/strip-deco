from strip_deco import stripdeco, run_after_strip
from .conftest import ClassDecoratorWithWraps, ClassDecoratorWithoutWraps


def test_stripdeco_class_deco_without_wraps():
    @ClassDecoratorWithoutWraps()
    def test():
        pass

    assert test.__closure__ is not None
    orig = stripdeco(obj=test)
    assert orig.__closure__ is None


def test_stripdeco_class_deco_with_wraps():
    @ClassDecoratorWithWraps()
    def test():
        pass

    assert test.__closure__ is not None
    orig = stripdeco(obj=test)
    assert orig.__closure__ is None


def test_stripdeco_class_deco_without_wraps_two_decorator():
    @ClassDecoratorWithoutWraps()
    @ClassDecoratorWithoutWraps()
    def test():
        pass

    assert test.__closure__ is not None
    orig = stripdeco(obj=test)
    assert orig.__closure__ is None


def test_stripdeco_class_deco_with_wraps_two_decorator():
    @ClassDecoratorWithWraps()
    @ClassDecoratorWithWraps()
    def test():
        pass

    assert test.__closure__ is not None
    orig = stripdeco(obj=test)
    assert orig.__closure__ is None


def test_stripdeco_class_deco_with_wraps_multiple_decorator():
    @ClassDecoratorWithWraps()
    @ClassDecoratorWithWraps()
    @ClassDecoratorWithWraps()
    @ClassDecoratorWithWraps()
    @ClassDecoratorWithWraps()
    @ClassDecoratorWithWraps()
    def test():
        pass

    assert test.__closure__ is not None
    orig = stripdeco(obj=test)
    assert orig.__closure__ is None


def test_stripdeco_class_deco_without_wraps_depth():
    @ClassDecoratorWithoutWraps()
    @ClassDecoratorWithoutWraps()
    @ClassDecoratorWithoutWraps()
    @ClassDecoratorWithoutWraps()
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


def test_stripdeco_class_deco_with_wraps_depth():
    @ClassDecoratorWithWraps()
    @ClassDecoratorWithWraps()
    @ClassDecoratorWithWraps()
    @ClassDecoratorWithWraps()
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


def test_run_after_strip_class_deco_without_wraps():
    @ClassDecoratorWithoutWraps()
    def test():
        return 1

    assert test.__closure__ is not None
    orig = run_after_strip(obj=test)
    assert orig == 1


def test_run_after_strip_class_deco_with_wraps():
    @ClassDecoratorWithWraps()
    def test():
        return 1

    assert test.__closure__ is not None
    orig = run_after_strip(obj=test)
    assert orig == 1


def test_run_after_strip_class_deco_without_wraps_two_decorator():
    @ClassDecoratorWithoutWraps()
    @ClassDecoratorWithoutWraps()
    def test():
        return 1

    assert test.__closure__ is not None
    orig = run_after_strip(obj=test)
    assert orig == 1


def test_run_after_strip_class_deco_with_wraps_multiple_decorator():
    @ClassDecoratorWithWraps()
    @ClassDecoratorWithWraps()
    @ClassDecoratorWithWraps()
    @ClassDecoratorWithWraps()
    @ClassDecoratorWithWraps()
    @ClassDecoratorWithWraps()
    def test():
        return 1

    assert test.__closure__ is not None
    orig = run_after_strip(obj=test)
    assert orig == 1


def test_run_after_strip_class_deco_without_wraps_depth():
    @ClassDecoratorWithoutWraps()
    @ClassDecoratorWithoutWraps()
    @ClassDecoratorWithoutWraps()
    @ClassDecoratorWithoutWraps()
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


def test_run_after_strip_class_deco_with_wraps_depth():
    @ClassDecoratorWithWraps()
    @ClassDecoratorWithWraps()
    @ClassDecoratorWithWraps()
    @ClassDecoratorWithWraps()
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
