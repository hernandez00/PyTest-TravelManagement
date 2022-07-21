from RestAPITesting._util.EnumRequestsType   import EnumRequestsType as ERT

class AddressURL:
    def __init__(self):
        self.__protocolURL = 'http'
        self.__baseURL     = 'localhost'
        self.__portURL     = '8089'

    def getURL(self, requestType):
        return self.__protocolURL + '://' + self.__baseURL + ':' + self.__portURL + ERT.getRequestType(requestType)