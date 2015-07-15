from unittest import TestCase
import pandas as pd

import pandas_validator as pv
from pandas_validator.core.exceptions import ValidationError


class DataFrameValidatorFixture(pv.DataFrameValidator):
    """Fixture for testing the validation of column type."""
    integer_field = pv.IntegerColumnValidator('i')
    float_field = pv.FloatColumnValidator('f')


class DataFrameValidatorTest(TestCase):
    """Testing the validation of column type."""
    def setUp(self):
        self.validator = DataFrameValidatorFixture()

    def test_valid(self):
        df = pd.DataFrame({'i': [0, 1], 'f': [0., 1.]})
        self.assertIsNone(self.validator.validate(df))

    def test_invalid_when_given_integer_series_to_float_column_validator(self):
        df = pd.DataFrame({'i': [0, 1], 'f': [0, 1]})
        self.assertRaises(ValidationError, self.validator.validate, df)


class DataFrameValidatorFixtureWithSize(pv.DataFrameValidator):
    """Fixture for testing the validation of column and row number."""
    row_num = 3
    column_num = 2


class DataFrameValidatorSizeTest(TestCase):
    """Testing the validation of column and row number."""
    def setUp(self):
        self.validator = DataFrameValidatorFixtureWithSize()

    def test_valid_when_matches_row_numbers(self):
        df = pd.DataFrame({'x': [0, 1, 2], 'y': [1., 2., 3.]})
        self.assertIsNone(self.validator.validate(df))

    def test_invalid_when_not_matches_row_numbers(self):
        df = pd.DataFrame({'x': [0, 1], 'y': [1., 2.]})
        self.assertRaises(ValidationError, self.validator.validate, df)

    def test_invalid_when_not_matches_column_numbers(self):
        df = pd.DataFrame({'x': [0, 1, 2], 'y': [1., 2., 3.], 'z': [1, 2, 3]})
        self.assertRaises(ValidationError, self.validator.validate, df)
