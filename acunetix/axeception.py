class AXException(Exception):
    HTTP_ERROR = "httpError"
    AUTH_ERROR = "authError"
    SERVER_RESOURCE = "serverResource"
    NOT_ALLOWED_CRITICYLITY_PROFILE = "Criticallity not found"

    def __init__(self, key, message):
        Exception.__init__(self, message)
        self.key = key


# for raising myErrors (raise AXException), call that when u tryna raise exceptions, bitch!
# raise AXException()
