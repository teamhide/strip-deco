from strip_deco import stripdeco
from .conftest import ClassDecoratorWithWraps, ClassDecoratorWithoutWraps


def test_class_deco_without_wraps_two_decorator():
    @ClassDecoratorWithoutWraps()
    @ClassDecoratorWithoutWraps()
    def test():
        return 1

    assert test.__closure__ is not None
    result = stripdeco(obj=test)
    assert result == 1


def test_class_deco_with_wraps_two_decorator():
    @ClassDecoratorWithWraps()
    @ClassDecoratorWithWraps()
    def test():
        return 1

    assert test.__closure__ is not None
    result = stripdeco(obj=test)
    assert result == 1


def test_class_deco_with_wraps_multiple_decorator():
    @ClassDecoratorWithWraps()
    @ClassDecoratorWithWraps()
    @ClassDecoratorWithWraps()
    @ClassDecoratorWithWraps()
    @ClassDecoratorWithWraps()
    @ClassDecoratorWithWraps()
    def test():
        return 1

    assert test.__closure__ is not None
    result = stripdeco(obj=test)
    assert result == 1


def test_class_deco_without_wraps_depth():
    @ClassDecoratorWithoutWraps()
    @ClassDecoratorWithoutWraps()
    @ClassDecoratorWithoutWraps()
    @ClassDecoratorWithoutWraps()
    def test():
        return 1

    assert test.__closure__ is not None
    result = stripdeco(obj=test, depth=1)
    assert result == 1
    result = stripdeco(obj=test, depth=2)
    assert result == 1
    result = stripdeco(obj=test, depth=3)
    assert result == 1
    result = stripdeco(obj=test, depth=4)
    assert result == 1


def test_class_deco_with_wraps_depth():
    @ClassDecoratorWithWraps()
    @ClassDecoratorWithWraps()
    @ClassDecoratorWithWraps()
    @ClassDecoratorWithWraps()
    def test():
        return 1

    assert test.__closure__ is not None
    result = stripdeco(obj=test, depth=1)
    assert result == 1
    result = stripdeco(obj=test, depth=2)
    assert result == 1
    result = stripdeco(obj=test, depth=3)
    assert result == 1
    result = stripdeco(obj=test, depth=4)
    assert result == 1
