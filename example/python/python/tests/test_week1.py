""" Test resources for week1 """
import io
import sys
import subprocess
import binascii

from hw.helloworld import main
from hw.helloworld import hello


class TestWeek1:
    """ Test class """
    GREETING = 'Hello'
    PLACE = 'World'
    HWSTRING = GREETING + ' ' + PLACE
    LOC_PATH = "example/python/python/tests/hw"

    def test_hello(self):
        """ check hello world """
        assert hello(self.GREETING, self.PLACE) == self.HWSTRING

    def test_main(self):
        """ Execute the hw script as a command line script """
        saved_stdout = sys.stdout
        try:
            out = io.StringIO()
            sys.stdout = out
            main()
            output = out.getvalue()
            assert output.strip() == self.HWSTRING
        finally:
            sys.stdout = saved_stdout

    def test_as_program(self):
        """ run the script """
        runscript = subprocess.check_output(["python", f"{self.LOC_PATH}/helloworld.py"]).strip()
        bin_string = binascii.a2b_qp(self.HWSTRING)
        assert runscript == bin_string
