from strip_deco import stripdeco
from .conftest import (
    ClassDecoratorWithWraps,
    ClassDecoratorWithoutWraps,
    func_decorator_with_wraps,
    func_decorator_without_wraps,
)


def test_class_deco_without_wraps():
    class Test:
        @ClassDecoratorWithoutWraps()
        def run(self):
            return 1

    assert Test().run.__closure__ is not None
    orig = stripdeco(obj=Test().run)
    assert orig == 1


def test_class_deco_with_wraps():
    class Test:
        @ClassDecoratorWithWraps()
        def run(self):
            return 1

    assert Test().run.__closure__ is not None
    result = stripdeco(obj=Test().run)
    assert result == 1


def test_class_deco_without_wraps_two_decorator():
    class Test:
        @ClassDecoratorWithoutWraps()
        @ClassDecoratorWithoutWraps()
        def run(self):
            return 1

    assert Test().run.__closure__ is not None
    result = stripdeco(obj=Test().run)
    assert result == 1


def test_class_deco_with_wraps_two_decorator():
    class Test:
        @ClassDecoratorWithWraps()
        @ClassDecoratorWithWraps()
        def run(self):
            return 1

    assert Test().run.__closure__ is not None
    result = stripdeco(obj=Test().run)
    assert result == 1


def test_class_deco_with_wraps_multiple_decorator():
    class Test:
        @ClassDecoratorWithWraps()
        @ClassDecoratorWithWraps()
        @ClassDecoratorWithWraps()
        @ClassDecoratorWithWraps()
        @ClassDecoratorWithWraps()
        @ClassDecoratorWithWraps()
        def run(self):
            return 1

    assert Test().run.__closure__ is not None
    result = stripdeco(obj=Test().run)
    assert result == 1


def test_class_deco_without_wraps_depth():
    class Test:
        @ClassDecoratorWithoutWraps()
        @ClassDecoratorWithoutWraps()
        @ClassDecoratorWithoutWraps()
        @ClassDecoratorWithoutWraps()
        def run(self):
            return 1

    assert Test().run.__closure__ is not None
    result = stripdeco(obj=Test().run, depth=1)
    assert result == 1
    result = stripdeco(obj=Test().run, depth=2)
    assert result == 1
    result = stripdeco(obj=Test().run, depth=3)
    assert result == 1
    result = stripdeco(obj=Test().run, depth=4)
    assert result == 1


def test_class_stripdeco_class_deco_with_wraps_depth():
    class Test:
        @ClassDecoratorWithWraps()
        @ClassDecoratorWithWraps()
        @ClassDecoratorWithWraps()
        @ClassDecoratorWithWraps()
        def run(self):
            return 1

    assert Test().run.__closure__ is not None
    result = stripdeco(obj=Test().run, depth=1)
    assert result == 1
    result = stripdeco(obj=Test().run, depth=2)
    assert result == 1
    result = stripdeco(obj=Test().run, depth=3)
    assert result == 1
    result = stripdeco(obj=Test().run, depth=4)
    assert result == 1


def test_class_has_init_class_deco_with_wraps_depth():
    class Test:
        def __init__(self, user_id):
            self.user_id = user_id

        @ClassDecoratorWithWraps()
        def run(self):
            return self.user_id

    user_id = 1
    assert Test(user_id=user_id).run.__closure__ is not None
    orig = stripdeco(obj=Test(user_id=user_id).run, depth=1)
    assert orig == user_id


def test_class_has_init_class_deco_without_wraps_depth():
    class Test:
        def __init__(self, user_id):
            self.user_id = user_id

        @ClassDecoratorWithoutWraps()
        def run(self):
            return self.user_id

    user_id = 1
    assert Test(user_id=user_id).run.__closure__ is not None
    orig = stripdeco(obj=Test(user_id=user_id).run, depth=1)
    assert orig == user_id


def test_class_has_init_function_deco_without_wraps_depth():
    class Test:
        def __init__(self, user_id):
            self.user_id = user_id

        @func_decorator_without_wraps
        def run(self):
            return self.user_id

    user_id = 1
    assert Test(user_id=user_id).run.__closure__ is not None
    orig = stripdeco(obj=Test(user_id=user_id).run, depth=1)
    assert orig == user_id


def test_class_has_init_function_deco_with_wraps_depth():
    class Test:
        def __init__(self, user_id):
            self.user_id = user_id

        @func_decorator_with_wraps
        def run(self):
            return self.user_id

    user_id = 1
    assert Test(user_id=user_id).run.__closure__ is not None
    orig = stripdeco(obj=Test(user_id=user_id).run, depth=1)
    assert orig == user_id


def test_class_has_init_run_and_argument_after_strip_class_deco_with_wraps_depth():
    class Test:
        def __init__(self, user_id):
            self.user_id = user_id

        @ClassDecoratorWithWraps()
        def run(self, user_pw):
            return f"{self.user_id}{user_pw}"

    user_id = 1
    user_pw = 2
    assert Test(user_id=user_id).run.__closure__ is not None
    orig = stripdeco(obj=Test(user_id=user_id).run, user_pw=user_pw, depth=1,)
    assert orig == f"{user_id}{user_pw}"


def test_class_has_init_run_and_argument_after_strip_class_deco_without_wraps_depth():
    class Test:
        def __init__(self, user_id):
            self.user_id = user_id

        @ClassDecoratorWithoutWraps()
        def run(self, user_pw):
            return f"{self.user_id}{user_pw}"

    user_id = 1
    user_pw = 2
    assert Test(user_id=user_id).run.__closure__ is not None
    orig = stripdeco(obj=Test(user_id=user_id).run, user_pw=user_pw, depth=1,)
    assert orig == f"{user_id}{user_pw}"


def test_class_has_init_run_and_argument_after_strip_function_deco_with_wraps_depth():
    class Test:
        def __init__(self, user_id):
            self.user_id = user_id

        @func_decorator_with_wraps
        def run(self, user_pw):
            return f"{self.user_id}{user_pw}"

    user_id = 1
    user_pw = 2
    assert Test(user_id=user_id).run.__closure__ is not None
    orig = stripdeco(obj=Test(user_id=user_id).run, user_pw=user_pw, depth=1,)
    assert orig == f"{user_id}{user_pw}"


def test_class_has_init_run_and_argument_after_strip_function_deco_without_wraps_depth():
    class Test:
        def __init__(self, user_id):
            self.user_id = user_id

        @func_decorator_without_wraps
        def run(self, user_pw):
            return f"{self.user_id}{user_pw}"

    user_id = 1
    user_pw = 2
    assert Test(user_id=user_id).run.__closure__ is not None
    orig = stripdeco(obj=Test(user_id=user_id).run, user_pw=user_pw, depth=1,)
    assert orig == f"{user_id}{user_pw}"
