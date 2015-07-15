from .series import (
    BaseSeriesValidator,
    IntegerSeriesValidator,
    FloatSeriesValidator,
    CharSeriesValidator,
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


class CharColumnValidator(ColumnValidatorMixin, CharSeriesValidator,):
    pass
