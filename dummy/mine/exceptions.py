from rest_framework.exceptions import ParseError


class ParseException(ParseError):
    def __init__(self, detail=None, code=None, errors=None):
        return super(ParseException, self).__init__(detail, code)