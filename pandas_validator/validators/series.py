from pandas_validator.core.exceptions import ValidationError


class BaseSeries(object):
    def __init__(self, series_type=None):
        self.series_type = series_type

    def validate(self, series):
        self._check_type(series)

    def _check_type(self, series):
        if self.series_type and not series.dtype.type == self.series_type:
            raise ValidationError('Series has the different type variables.')

    def is_valid(self, series):
        try:
            self.validate(series)
        except ValidationError:
            return False
        else:
            return True
