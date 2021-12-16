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


class funcTestCase(SkyproTestCase):
    
    def test_class_Unit_has_expected_methods(self):
        inspected_class = main.Cube
        unexpected_methods = ['get_x', 'get_y', 'get_z']
        
        object_methods = [
            method_name for method_name in dir(inspected_class)
                  if callable(getattr(inspected_class, method_name))]
        for method in unexpected_methods:
            self.assertNotIn(
                method, object_methods,
                f"%@Кажется, что часть методов здесь всё-таки лишняя :)"
                ", либо вы забыли их переименовать."
            )

if __name__ == "__main__":
    unittest.main()