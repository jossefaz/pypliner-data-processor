class ArgumentMissingException(Exception) :

    def __init__(self, missing_args):
        self.message = "the missing argument is {}".format(missing_args)

    def __str__(self):
        return repr(self.message)