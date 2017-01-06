from .columns import ColumnValidatorMixin
from .index import IndexValidator, ColumnsValidator
from ..core.exceptions import ValidationError


class DataFrameValidator(object):
    index = None
    columns = None

    column_num = None  # int The number of column.
    row_num = None  # int The number of row.

    def __init__(self, nullable=False, row_num=None, column_num=None):
        self.nullable = nullable
        self.row_num = row_num
        self.column_num = column_num
        self._setup_index_and_columns_validator()

    def _setup_index_and_columns_validator(self):
        if self.row_num is not None and self.index is None:
            self.index = IndexValidator(size=self.row_num)

        if self.column_num is not None and self.columns is None:
            self.columns = ColumnsValidator(size=self.column_num)

    def validate(self, df, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self._run_index_and_columns_validator(df)
        self._run_column_validator(df)
        self._check_dataframe_size(df)

    def _run_column_validator(self, df):
        fields = [getattr(self, x) for x in dir(self)]
        column_validators = [x for x in fields
                             if isinstance(x, ColumnValidatorMixin)]

        for v in column_validators:
            v.validate(df)
        return True

    def _run_index_and_columns_validator(self, df):
        if self.index is not None:
            self.index.validate(df.index)

        if self.columns is not None:
            self.columns.validate(df.columns)

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
