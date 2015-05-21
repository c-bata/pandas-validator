from pandas_validator.validators import BaseSeriesValidator
from pandas_validator.core.exceptions import ValidationError


class DataFrameValidator(object):
    def __init__(self):
        pass

    def validate(self, df):
        self._run_column_validator(df)

    def _run_column_validator(self, df):
        fields = [getattr(self, x) for x in dir(self) if not x.startswith('__')]
        column_validators = [x for x in fields if isinstance(x, BaseSeriesValidator)]

        for v in column_validators:
            v.validate(df)
        return True

    def is_valid(self, df):
        try:
            self.validate(df)
        except ValidationError:
            return False
        else:
            return True
