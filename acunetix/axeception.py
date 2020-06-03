class AXException(Exception):
    HTTP_ERROR = "httpError"
    AUTH_ERROR = "authError"
    SERVER_RESOURCE = "serverResource"
    NOT_ALLOWED_CRITICYLITY_PROFILE = "Criticallity not found"
    NOT_ALLOWED_SCAN_PROFILE = "Scan Profile not found"
    JSON_PARSING_ERROR = "Decoding JSON has failed"

    def __init__(self, key, message):
        Exception.__init__(self, message)
        self.key = key


# for raising myErrors (raise AXException), call that when u tryna raise exceptions, bitch!
# raise AXException()
