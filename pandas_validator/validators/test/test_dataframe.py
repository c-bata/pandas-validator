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

    def test_should_raise_exception_when_given_float_series(self):
        df = pd.DataFrame({'x': [0, 1], 'y': [0., 1.]})
        self.assertRaises(ValidationError, self.validator.validate, df)

