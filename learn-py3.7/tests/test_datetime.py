import unittest

import datetime

from tests import coutln

class DatetimeTest(unittest.TestCase):
    def test_datetime(self):
        """
        python -m unittest tests.test_datetime.DatetimeTest.test_datetime
        :return:
        """
        now = datetime.datetime.now()
        coutln(str(now))
        coutln(now.strftime("%d/%m/%Y %I:%M:%S %p"))
        coutln(now.strftime("%-d/%-m/%Y %I:%M:%S %p"))
