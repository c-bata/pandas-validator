from unittest import TestCase
import pandas as pd
import numpy as np

import pandas_validator as pv


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
        self.assertTrue(self.validator.is_valid(df))

    def test_invalid_when_given_integer_series_to_float_column_validator(self):
        df = pd.DataFrame({'i': [0, 1], 'f': [0, 1]})
        self.assertFalse(self.validator.is_valid(df))


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
        self.assertTrue(self.validator.is_valid(df))

    def test_invalid_when_not_matches_row_numbers(self):
        df = pd.DataFrame({'x': [0, 1], 'y': [1., 2.]})
        self.assertFalse(self.validator.is_valid(df))

    def test_invalid_when_not_matches_column_numbers(self):
        df = pd.DataFrame({'x': [0, 1, 2], 'y': [1., 2., 3.], 'z': [1, 2, 3]})
        self.assertFalse(self.validator.is_valid(df))


class DataFrameValidatorFixtureWithIndex(pv.DataFrameValidator):
    """Fixture for testing the validation of index validator."""
    index = pv.IndexValidator(size=3, type=np.int64)


class DataFrameValidatorIndexTest(TestCase):
    """Testing the validation of index size and type."""
    def setUp(self):
        self.validator = DataFrameValidatorFixtureWithIndex()

    def test_valid_when_matches_index_size_and_type(self):
        df = pd.DataFrame([0, 1, 2])
        self.assertTrue(self.validator.is_valid(df))

    def test_invalid_when_not_matches_index_size(self):
        df = pd.DataFrame([0, 1, 2, 3])
        self.assertFalse(self.validator.is_valid(df))

    def test_invalid_when_not_matches_index_type(self):
        df = pd.DataFrame([0, 1, 2], index=['a', 'b', 'c'])
        self.assertFalse(self.validator.is_valid(df))


class DataFrameValidatorFixtureWithColumns(pv.DataFrameValidator):
    """Fixture for testing the validation of columns validator."""
    columns = pv.ColumnsValidator(size=2, type=np.object_)


class DataFrameValidatorColumnsIndexTest(TestCase):
    """Testing the validation of columns size and type"""
    def setUp(self):
        self.validator = DataFrameValidatorFixtureWithColumns()

    def test_valid_when_matches_columns_size_and_type(self):
        df = pd.DataFrame({'x': [0, 1, 2], 'y': [1., 2., 3.]})
        self.assertTrue(self.validator.is_valid(df))

    def test_invalid_when_not_matches_columns_size(self):
        df = pd.DataFrame({'x': [0, 1, 2], 'y': [1., 2., 3.], 'z': [1, 2, 3]})
        self.assertFalse(self.validator.is_valid(df))

    def test_invalid_when_not_matches_columns_type(self):
        df = pd.DataFrame([[0, 1, 2], [1., 2., 3.]])
        self.assertFalse(self.validator.is_valid(df))
