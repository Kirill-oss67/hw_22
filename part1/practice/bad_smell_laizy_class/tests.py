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
    
    def test_class_Unit_has_expected_methods(self):
        self.assertFalse(
            hasattr(main, 'FieldAdapter'),
            "%@Кажется, ненужный класс всё еще существует"
        )

if __name__ == "__main__":
    unittest.main()
