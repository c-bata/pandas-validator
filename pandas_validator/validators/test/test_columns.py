from unittest import TestCase
import pandas as pd

from pandas_validator import validators


class IntegerColumnValidatorTest(TestCase):
    def setUp(self):
        self.dataframe = pd.DataFrame({'label1': [0, 1], 'label2': [1., 2.]})

    def test_is_valid(self):
        column_validator = validators.IntegerColumnValidator('label1')
        self.assertTrue(column_validator.is_valid(self.dataframe))

    def test_is_invalid(self):
        column_validator = validators.IntegerColumnValidator('label2')
        self.assertFalse(column_validator.is_valid(self.dataframe))

class FloatColumnValidatorTest(TestCase):
    def setUp(self):
        self.dataframe = pd.DataFrame({'label1': [0., 1.], 'label2': [1, 2]})

    def test_is_valid(self):
        column_validator = validators.FloatColumnValidator('label1')
        self.assertTrue(column_validator.is_valid(self.dataframe))

    def test_is_invalid(self):
        column_validator = validators.FloatColumnValidator('label2')
        self.assertFalse(column_validator.is_valid(self.dataframe))

class CharColumnValidatorTest(TestCase):
    def setUp(self):
        self.dataframe = pd.DataFrame({'label1': ['', 'aa'], 'label2': [0, 1]})

    def test_is_valid(self):
        column_validator = validators.CharColumnValidator('label1')
        self.assertTrue(column_validator.is_valid(self.dataframe))

    def test_is_invalid(self):
        column_validator = validators.CharColumnValidator('label2')
        self.assertFalse(column_validator.is_valid(self.dataframe))
