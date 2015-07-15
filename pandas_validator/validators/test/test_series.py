from unittest import TestCase
import pandas as pd
import numpy as np

import pandas_validator as pv
from pandas_validator.core.exceptions import ValidationError


class BaseSeriesValidatorTest(TestCase):
    def setUp(self):
        self.validator = pv.BaseSeriesValidator(series_type=np.int64)

    def test_is_valid_when_given_int64_series(self):
        series = pd.Series([0, 1])
        self.assertTrue(self.validator.is_valid(series))

    def test_is_invalid_when_given_float_series(self):
        series = pd.Series([0., 1.])
        self.assertFalse(self.validator.is_valid(series))

    def test_should_return_true_when_given_int64_series(self):
        series = pd.Series([0, 1])
        self.assertIsNone(self.validator.validate(series))

    def test_should_return_false_when_given_float_series(self):
        series = pd.Series([0., 1.])
        self.assertRaises(ValidationError, self.validator.validate, series)


class IntegerSeriesValidatorTest(TestCase):
    def setUp(self):
        self.validator = pv.IntegerSeriesValidator(min_value=0, max_value=2)

    def test_is_valid(self):
        series = pd.Series([0, 1, 2])
        self.assertTrue(self.validator.is_valid(series))

    def test_is_invalid_by_too_low_value(self):
        series = pd.Series([-1, 0, 1, 2])
        self.assertFalse(self.validator.is_valid(series))

    def test_is_invalid_by_too_high_value(self):
        series = pd.Series([0, 1, 2, 3])
        self.assertFalse(self.validator.is_valid(series))


class FloatSeriesValidatorTest(TestCase):
    def setUp(self):
        self.validator = pv.FloatSeriesValidator(min_value=0, max_value=2)

    def test_is_valid(self):
        series = pd.Series([0., 1., 2.])
        self.assertTrue(self.validator.is_valid(series))

    def test_is_invalid_when_given_integer_series(self):
        series = pd.Series([0, 1, 2])
        self.assertFalse(self.validator.is_valid(series))

    def test_is_invalid_by_too_low_value(self):
        series = pd.Series([-0.1, 0., 1.])
        self.assertFalse(self.validator.is_valid(series))

    def test_is_invalid_by_too_high_value(self):
        series = pd.Series([0., 1., 2.1])
        self.assertFalse(self.validator.is_valid(series))


class CharSeriesValidatorTest(TestCase):
    def setUp(self):
        self.validator = pv.CharSeriesValidator(min_length=0, max_length=4)

    def test_is_valid(self):
        series = pd.Series(['', 'ab', 'abcd'])
        self.assertTrue(self.validator.is_valid(series))

    def test_is_invalid_when_given_integer_series(self):
        series = pd.Series([0, 1, 2])
        self.assertFalse(self.validator.is_valid(series))

    def test_is_invalid_by_too_long_length(self):
        series = pd.Series(['', 'ab', 'abcde'])
        self.assertFalse(self.validator.is_valid(series))
