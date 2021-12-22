import sys
import unittest
from pathlib import Path
import os
import main

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[: basefolder_index + 1])
sys.path.append(str(basepath))
from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402


class FuncTestCase(SkyproTestCase):

    def test_module_has_expected_classes(self):
        self.assertTrue(
            hasattr(main.SomeClass, 'sorted_func'),
            "%@Проверьте что в классе SomeClass создан метод sorted_func"
        )

        some_inst = main.SomeClass()
        self.assertTrue(
            some_inst.sorted_func() == [1, 1, 2, 2, 3, 4],
            "%@Проверьте, что Ваш метод объединяет в себе все возможности представленных методов"
        )

    def test_class_Unit_has_expected_methods(self):
        inspected_class = main.SomeClass
        unexpected_methods = ['sorted', 'sorting', 'asc_sorted']
        
        object_methods = [
            method_name for method_name in dir(inspected_class)
                  if callable(getattr(inspected_class, method_name))]
        for method in unexpected_methods:
            self.assertNotIn(
                method, object_methods,
                f"%@Проверьте, что в Вашем классе не осталось старых методов"
            )

if __name__ == "__main__":
    unittest.main()