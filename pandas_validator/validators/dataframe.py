from .columns import ColumnValidatorMixin
from ..core.exceptions import ValidationError


class DataFrameValidator(object):
    column_num = None  # int The number of column.
    row_num = None  # int The number of row.

    def __init__(self):
        pass

    def validate(self, df):
        self._run_column_validator(df)
        self._check_dataframe_size(df)

    def _run_column_validator(self, df):
        fields = [getattr(self, x) for x in dir(self)]
        column_validators = [x for x in fields
                             if isinstance(x, ColumnValidatorMixin)]

        for v in column_validators:
            v.validate(df)
        return True

    def _check_dataframe_size(self, df):
        if self.column_num is not None and len(df.columns) != self.column_num:
            raise ValidationError('DataFrame columns number is not %s'
                                  % self.column_num)

        if self.row_num is not None and len(df.index) != self.row_num:
            raise ValidationError('DataFrame rows number is not %s'
                                  % self.row_num)

    def is_valid(self, df):
        try:
            self.validate(df)
        except ValidationError:
            return False
        else:
            return True
