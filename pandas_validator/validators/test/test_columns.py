from unittest import TestCase
import pandas as pd

from pandas_validator import validators


class IntegerColumnTest(TestCase):
    def setUp(self):
        self.dataframe = pd.DataFrame({'label1': [0, 1], 'label2': [1., 2.]})

    def test_is_valid(self):
        column_validator = validators.IntegerColumn('label1')
        self.assertTrue(column_validator.is_valid(self.dataframe))

    def test_is_invalid(self):
        column_validator = validators.IntegerColumn('label2')
        self.assertFalse(column_validator.is_valid(self.dataframe))
