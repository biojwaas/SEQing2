class fileExceptions(Exception):
    """Exception raised for errors occurred due to input

    Attributes:
        File -- Input File which caused the error
        Message -- explanation of the error
    """
    CONST_MESSAGE = "Some Error occurred"

    def __init__(self,file, message=CONST_MESSAGE):
        self.file = file
        self.message = message
        super(fileExceptions, self).__init__(self.message)