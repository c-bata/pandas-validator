from unittest import TestCase
import pandas as pd
import numpy as np

from pandas_validator import validators
from pandas_validator.core.exceptions import ValidationError


class BaseSeriesTest(TestCase):
    def setUp(self):
        self.validator = validators.BaseSeries(series_type=np.int64)

    def test_is_valid_when_given_int64_series(self):
        self.series = pd.Series([0, 1])
        self.assertTrue(self.validator.is_valid(self.series))

    def test_is_invalid_when_given_float_series(self):
        self.series = pd.Series([0., 1.])
        self.assertFalse(self.validator.is_valid(self.series))

    def test_should_return_true_when_given_int64_series(self):
        self.series = pd.Series([0, 1])
        self.assertIsNone(self.validator.validate(self.series))

    def test_should_return_false_when_given_float_series(self):
        self.series = pd.Series([0., 1.])
        self.assertRaises(ValidationError,
                          self.validator.validate, self.series)

class IntegerSeriesTest(TestCase):
    def setUp(self):
        self.validator = validators.IntegerSeries(min_value=0, max_value=2)

    def test_is_invalid_by_too_low_value(self):
        self.series = pd.Series([-1, 0, 1, 2])
        self.assertFalse(self.validator.is_valid(self.series))

    def test_is_invalid_by_too_high_value(self):
        self.series = pd.Series([0, 1, 2, 3])
        self.assertFalse(self.validator.is_valid(self.series))

