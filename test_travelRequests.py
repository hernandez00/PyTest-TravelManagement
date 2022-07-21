from RestAPITesting.POST_GenerateToken          import getToken
from RestAPITesting.POST_RegisterTravel         import registerTravel
import pytest

class TestTravelManagement:
    pytest.adminToken  = ''
    pytest.commonToken = ''

    def test_GetAdminToken(self):
        pytest.adminToken = getToken(requestType='ADMIN_TOKEN')
        assert pytest.adminToken

    def test_GetCommonToken(self):
        pytest.commonToken = getToken(requestType='COMMON_TOKEN')
        assert pytest.commonToken

    def test_RegisterTravel(self):
        assert(registerTravel(pytest.adminToken, requestType='REGISTER_GETALL'))
"""
adminToken = getToken(requestType='COMMON_TOKEN')
registerTravel(adminToken=adminToken, requestType='REGISTER_GETALL')
"""