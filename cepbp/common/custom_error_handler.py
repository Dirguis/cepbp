class CustomError(Exception):
    """
    Custom error class, to pass a custom message and data to the user as needed

    Parameters
    ----------
    msg: string
      Error message
    data: anything
      Whatever data is useful to print
    """
    def __init__(self, msg, data=''):
        self.msg = msg
        self.data = data

    def __str__(self):
        return repr(self.msg, self.data)
