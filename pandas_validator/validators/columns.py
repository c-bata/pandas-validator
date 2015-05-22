from pandas_validator.validators import (
    BaseSeriesValidator,
    IntegerSeriesValidator,
    FloatSeriesValidator,
)


class ColumnValidatorMixin(BaseSeriesValidator):
    def __init__(self, label, *args, **kwargs):
        super(ColumnValidatorMixin, self).__init__(*args, **kwargs)
        self.label = label

    def validate(self, dataframe):
        super(ColumnValidatorMixin, self).validate(dataframe[self.label])


class IntegerColumnValidator(ColumnValidatorMixin, IntegerSeriesValidator):
    pass

class FloatColumnValidator(ColumnValidatorMixin, FloatSeriesValidator):
    pass
