
class ValidationError(Exception):
    """An error while validating data."""
    def __init__(self, message):
        super(ValidationError, self).__init__(message)

        self.message = message
