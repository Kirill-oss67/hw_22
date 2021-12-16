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
        expected_classes = ['Unit', 'Field', 'Main']
        for cls in expected_classes:
            self.assertTrue(
                hasattr(main, cls),
                f"%@Кажется, что удалено что-то лишнее.."
            )

    def test_module_has_expected_classes(self):
        unexpected_classes = ['GameItem', ]
        for cls in unexpected_classes:
            self.assertFalse(
                hasattr(main, cls),
                f"%@Кажется, ненужный класс всё еще присутствует в модуле.."
            )

if __name__ == "__main__":
    unittest.main()