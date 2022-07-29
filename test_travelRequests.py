from RestAPITesting.POST_GenerateToken          import getToken
from RestAPITesting.POST_RegisterTravel         import registerTravel
from RestAPITesting.GET_AllTravels              import getAllTravels
import pytest

class TestTravelManagement:
    pytest.adminToken  = ''
    pytest.commonToken = ''

    def test_GetAdminToken(self):
        pytest.adminToken = getToken(requestType='ADMIN_TOKEN')
        assert pytest.adminToken == False

    def test_GetCommonToken(self):
        pytest.commonToken = getToken(requestType='COMMON_TOKEN')
        assert pytest.commonToken

    def test_RegisterTravel(self):
        assert(registerTravel(pytest.adminToken, requestType='REGISTER_GETALL'))
    
    def test_GetAllTravels(self):
        assert(getAllTravels(pytest.commonToken, requestType='GET_PUT_DELETE'))

"""
adminToken  = getToken(requestType='ADMIN_TOKEN')
commonToken = getToken(requestType='COMMON_TOKEN')

registerTravel(adminToken=adminToken, requestType='REGISTER_GETALL')
getAllTravels(commonToken=commonToken, requestType='GET_PUT_DELETE')
"""