from .series import *


class IntegerColumnValidator(IntegerSeriesValidator):
    def __init__(self, label, *args, **kwargs):
        super(IntegerColumnValidator, self).__init__(*args, **kwargs)
        self.label = label

    def is_valid(self, dataframe):
        return super(IntegerColumnValidator, self).is_valid(dataframe[self.label])
