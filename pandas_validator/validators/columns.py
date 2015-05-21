from .series import *


class IntegerColumnValidator(IntegerSeriesValidator):
    def __init__(self, label, *args, **kwargs):
        super(IntegerColumnValidator, self).__init__(*args, **kwargs)
        self.label = label

    def validate(self, dataframe):
        super(IntegerColumnValidator, self).validate(dataframe[self.label])
