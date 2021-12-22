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
        expected_classes = ['Transport', 'Boat', 'Car', 'Electroscooter', 'Person']
        for cls in expected_classes:
            self.assertTrue(
                hasattr(main, cls),
                f"%@Проверьте, что вы определили класс {cls}"
            )
        
    def test_class_has_expected_methods(self):
        expected_methods = ['start_engine', 'stop_engine', 'move', 'stop']
        inspected_class = main.Transport

        object_methods = [
            method_name for method_name in dir(inspected_class)
                  if callable(getattr(inspected_class, method_name))]
        for method in expected_methods:
            self.assertIn(
                method, object_methods,
                f"%@Проверьте, что вы определили метод {method} в классе Transport"
            )
        
            self.assertIn(
                method, inspected_class.__abstractmethods__,
                f"%@Проверьте что метод {method} класса Transport является абстрактным методом"
            )

if __name__ == "__main__":
    unittest.main()
