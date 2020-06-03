class AXException(Exception):
    HTTP_ERROR = "httpError"
    AUTH_ERROR = "authError"
    SERVER_RESOURCE = "serverResource"
    def __init__(self, key, message):
        Exception.__init__(self, message)
        self.key = key


# for raising myErrors (raise AXException), call that when u tryna raise exceptions, bitch!
# raise AXException()
