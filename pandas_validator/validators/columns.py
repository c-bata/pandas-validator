from .series import *


class IntegerColumnVaridator(IntegerSeriesValidator):
    def __init__(self, label, *args, **kwargs):
        super(IntegerColumnVaridator, self).__init__(*args, **kwargs)
        self.label = label

    def is_valid(self, dataframe):
        return super(IntegerColumnVaridator, self).is_valid(dataframe[self.label])
