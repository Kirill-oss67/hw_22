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


class ClassTestCase(SkyproTestCase):

    def test_module_has_expected_classes(self):
        expected_classes = ['Warrior', 'Healer', 'Tree', 'Trap']
        for cls in expected_classes:
            self.assertTrue(
                hasattr(main, cls),
                f"%@Проверьте, что вы определили класс {cls}"
            )
        
    def test_class_Unit_has_expected_methods(self):
        inspected_class = main.Warrior
        expected_methods = ['attack', 'defence', 'move']
        
        object_methods = [
            method_name for method_name in dir(inspected_class)
                  if callable(getattr(inspected_class, method_name))]
        for method in expected_methods:
            self.assertIn(
                method, object_methods,
                f"%@Проверьте, что вы определили метод {method} в классе Transport"
            )

    def test_class_Unit_has_expected_methods(self):
        inspected_class = main.Warrior
        expected_methods = ['attack', 'defense', 'move']
        
        object_methods = [
            method_name for method_name in dir(inspected_class)
                  if callable(getattr(inspected_class, method_name))]
        for method in expected_methods:
            self.assertIn(
                method, object_methods,
                f"%@Проверьте, что вы определили метод {method} в классе {inspected_class.__name__}"
            )

    def test_class_Heal_has_expected_methods(self):
        inspected_class = main.Healer
        expected_methods = ['heal', 'defense', 'move']
        
        object_methods = [
            method_name for method_name in dir(inspected_class)
                  if callable(getattr(inspected_class, method_name))]
        for method in expected_methods:
            self.assertIn(
                method, object_methods,
                f"%@Проверьте, что вы определили метод {method} в классе {inspected_class.__name__}"
            )

    def test_class_Tree_has_expected_methods(self):
        inspected_class = main.Tree
        expected_methods = ['on_fire', 'defense',]
        
        object_methods = [
            method_name for method_name in dir(inspected_class)
                  if callable(getattr(inspected_class, method_name))]
        for method in expected_methods:
            self.assertIn(
                method, object_methods,
                f"%@Проверьте, что вы определили метод {method} в классе {inspected_class.__name__}"
            )

    def test_class_Trap_has_expected_methods(self):
        inspected_class = main.Trap
        expected_methods = ['attack',]
        
        object_methods = [
            method_name for method_name in dir(inspected_class)
                  if callable(getattr(inspected_class, method_name))]
        for method in expected_methods:
            self.assertIn(
                method, object_methods,
                f"%@Проверьте, что вы определили метод {method} в классе {inspected_class.__name__}"
            )


if __name__ == "__main__":
    unittest.main()