import numpy as np

from pandas_validator.core.exceptions import ValidationError


class BaseSeriesValidator(object):
    def __init__(self, series_type=None):
        self.series_type = series_type

    def validate(self, series):
        self._check_type(series)

    def _check_type(self, series):
        if (self.series_type is not None and
                not series.dtype.type == self.series_type):
            raise ValidationError('Series has the different type variables.')

    def is_valid(self, series):
        try:
            self.validate(series)
        except ValidationError:
            return False
        else:
            return True


class IntegerSeriesValidator(BaseSeriesValidator):
    def __init__(self, min_value=None, max_value=None, series_type=np.int64):
        super(IntegerSeriesValidator, self).__init__(series_type)

        self.max_value, self.min_value = max_value, min_value

    def validate(self, series):
        super(IntegerSeriesValidator, self).validate(series)

        if (self.max_value is not None and
                len(series[series > self.max_value]) > 0):
            raise ValidationError('Series has the value greater than max.')

        if (self.min_value is not None and
                len(series[series < self.min_value]) > 0):
            raise ValidationError('Series has the value smaller than min.')
