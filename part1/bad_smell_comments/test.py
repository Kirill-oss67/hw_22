import sys
import unittest
from pathlib import Path
import os
import main
import inspect

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[: basefolder_index + 1])
sys.path.append(str(basepath))
from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402


class ClassTestCase(SkyproTestCase):

    def test_module_has_expected_classes(self):
        code_strings = inspect.getsource(main.Unit)
        self.assertNotIn(
            "#", code_strings,
            "%@Проверьте, удалили ли вы все комментарии?"
        )
        unexpected_variables = [
            '\sf[i]*eld_1_param[:]\s', 
            '\sfield_2_param[:]\s',
            '\sd[:]\s',
            '\sfl[:]\s',
            '\scr[:]\s',
            'points_per_action',
            'mvmntobjbfld'
        ]
        for variable in unexpected_variables:
            self.assertNotRegex(
                code_strings, variable,
                f"%@ Похоже в коде еще остались плохие переменные {variable}"
            )


if __name__ == "__main__":
    unittest.main()