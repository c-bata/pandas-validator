from unittest import TestCase
import numpy as np
import pandas as pd

from pandas_validator import validators
from pandas_validator.core.exceptions import ValidationError


class DataFrameValidatorFixture(validators.DataFrameValidator):
    x_points = validators.IntegerColumnValidator('x')
    y_points = validators.IntegerColumnValidator('y')


class DataFrameValidatorTest(TestCase):
    def setUp(self):
        self.validator = DataFrameValidatorFixture()

    def test_should_return_None_when_validate_is_success(self):
        df = pd.DataFrame({'x': [0, 1], 'y': [0, 1]})
        self.assertIsNone(self.validator.validate(df))

    def test_valid_when_given_float_series(self):
        df = pd.DataFrame({'x': [0, 1], 'y': [0., 1.]})
        self.assertRaises(ValidationError, self.validator.validate, df)

    def test_valid_when_matches_column_and_row_numbers(self):
        self.validator.row_num, self.validator.column_num = 3, 2
        df = pd.DataFrame({'x': [0, 1, 2], 'y': [1, 2, 3]})
        self.assertIsNone(self.validator.validate(df))

    def test_invalid_when_not_matches_column_numbers(self):
        self.validator.row_num, self.validator.column_num = 3, 3
        df = pd.DataFrame({'x': [0, 1, 2], 'y': [1, 2, 3]})
        self.assertRaises(ValidationError, self.validator.validate, df)

    def test_invalid_when_not_matches_row_numbers(self):
        self.validator.row_num, self.validator.column_num = 2, 2
        df = pd.DataFrame({'x': [0, 1, 2], 'y': [1, 2, 3]})
        self.assertRaises(ValidationError, self.validator.validate, df)
