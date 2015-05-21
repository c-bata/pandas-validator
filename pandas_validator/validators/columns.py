from .series import *


class IntegerColumn(IntegerSeries):
    def __init__(self, label, *args, **kwargs):
        super(IntegerColumn, self).__init__(*args, **kwargs)
        self.label = label

    def is_valid(self, dataframe):
        return super(IntegerColumn, self).is_valid(dataframe[self.label])
