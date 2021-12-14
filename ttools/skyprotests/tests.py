import unittest
import sys
from io import StringIO


class StatMixin:
    def send_stat(self, result):
        if result.wasSuccessful():
            print(f"Тест {result.testsRun} пройден успешно!")


class SkyproTestCase(StatMixin, unittest.TestCase):
    def run(self, *args, **kwargs):
        result = super().run(*args, **kwargs)
        x = len(result.failures) - 1
        if len(result.failures) == 0:
            pass
        else:
            error_ind = result.failures[x][-1].rfind("%@")
            if error_ind != -1:
                error_text = result.failures[x][-1][error_ind + 2 :]
                testcase = result.failures[x][0]
                new_error_output = (testcase, error_text)
                result.failures[x] = new_error_output
        self.send_stat(result)


class StdoutCapturing(list):
    """
    Class for capturing function stdout.
    Usage:
        with Capturing() as func_output:
            func()

    check func() output in func_output variable
    """

    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio  # free up some memory
        sys.stdout = self._stdout
