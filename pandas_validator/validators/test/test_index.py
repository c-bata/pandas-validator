from unittest import TestCase
import pandas as pd
import numpy as np

import pandas_validator as pv
from pandas_validator.core.exceptions import ValidationError


class BaseIndexValidatorTest(TestCase):
    def setUp(self):
        self.validator = pv.BaseIndexValidator(size=3, type=np.int64)

    def test_is_valid_when_size_and_type_are_ok(self):
        index = pd.Index([0, 1, 2])
        self.assertIsNone(self.validator.validate(index))

    def test_is_invalid_when_size_is_not_ok(self):
        index = pd.Index([0, 1, 2, 3])
        self.assertRaises(ValidationError, self.validator.validate, index)

    def test_is_invalid_when_type_is_not_ok(self):
        index = pd.Index(['a', 'b', 'c'])
        self.assertRaises(ValidationError, self.validator.validate, index)
