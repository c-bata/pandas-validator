from unittest import TestCase
import pandas as pd

import pandas_validator as pv


class IntegerColumnValidatorTest(TestCase):
    def setUp(self):
        self.dataframe = pd.DataFrame({'label1': [0, 1], 'label2': [1., 2.]})

    def test_is_valid(self):
        column_validator = pv.IntegerColumnValidator('label1')
        self.assertTrue(column_validator.is_valid(self.dataframe))

    def test_is_invalid(self):
        column_validator = pv.IntegerColumnValidator('label2')
        self.assertFalse(column_validator.is_valid(self.dataframe))


class FloatColumnValidatorTest(TestCase):
    def setUp(self):
        self.dataframe = pd.DataFrame({'label1': [0., 1.], 'label2': [1, 2]})

    def test_is_valid(self):
        column_validator = pv.FloatColumnValidator('label1')
        self.assertTrue(column_validator.is_valid(self.dataframe))

    def test_is_invalid(self):
        column_validator = pv.FloatColumnValidator('label2')
        self.assertFalse(column_validator.is_valid(self.dataframe))


class CharColumnValidatorTest(TestCase):
    def setUp(self):
        self.dataframe = pd.DataFrame({'label1': ['', 'aa'], 'label2': [0, 1]})

    def test_is_valid(self):
        column_validator = pv.CharColumnValidator('label1')
        self.assertTrue(column_validator.is_valid(self.dataframe))

    def test_is_invalid(self):
        column_validator = pv.CharColumnValidator('label2')
        self.assertFalse(column_validator.is_valid(self.dataframe))
