class ElementsInOrderLimitError(Exception):

    def __init__(self, allowed_limit, message=f"Przekroczono limit", *args):
        self.allowed_limit = allowed_limit
        super().__init__(message, *args)

