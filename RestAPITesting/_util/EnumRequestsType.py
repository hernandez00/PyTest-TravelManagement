from enum import Enum

class EnumRequestsType(Enum):
    TOKEN            = '/api/v1/auth'
    REGISTER_GETALL  = '/api/v1/viagens'
    GET_PUT_DELETE   = '/api/v1/viagens/'
    
    def getRequestType(requestType):
        for request in EnumRequestsType:
            if request.name == requestType:
                return request.value