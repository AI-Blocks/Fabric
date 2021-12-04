class ResultTypeError(Exception):
    """
    Raised when the result type coming from is not valid.
    """
    def __init__(self, model_name, expected_type, received_type):
        self.message = "Expected result type {}, got {}, for model {}".format(expected_type, received_type, model_name)
        super().__init__(self.message)

    def __str__(self):
        return self.message
