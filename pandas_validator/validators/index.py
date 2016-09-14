from ..core.exceptions import ValidationError


class BaseIndexValidator(object):
    def __init__(self, size=None, type=None):
        self.size = size
        self.type = type

    def validate(self, index):
        self._check_size(index)
        self._check_type(index)

    def _check_size(self, index):
        if self.size is not None and index.size != self.size:
            raise ValidationError('Index has the different size.')

    def _check_type(self, index):
        if self.type is not None and index.dtype.type != self.type:
            raise ValidationError('Index has the different type.')

    def is_valid(self, index):
        try:
            self.validate(index)
        except ValidationError:
            return False
        else:
            return True


class IndexValidator(BaseIndexValidator):
    pass


class ColumnsValidator(BaseIndexValidator):
    pass
