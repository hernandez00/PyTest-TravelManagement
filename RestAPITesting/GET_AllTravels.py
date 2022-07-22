from json                                   import dumps
import json
from requests.structures                    import CaseInsensitiveDict
from RestAPITesting._util.AddressURL        import AddressURL
import requests

def getAllTravels(commonToken, requestType):
    
    URL = AddressURL().getURL(requestType) #+ '?reagiao=Norte'

    headers = CaseInsensitiveDict()
    headers['Content-Type']  = 'application/json'
    headers['Authorization'] = commonToken

    resp = requests.get(url=URL, headers=headers)

    showResponse(resp)

    jsonData = resp.json()

    if resp.status_code == 200:
        return jsonData['data']
    else:
        return False

def showResponse(response):
    for headItem_k, headItem_v in response.headers.items():
        print(f'{headItem_k:>23}: {headItem_v}')
    
    print(f"Body: \n {dumps(response.json(), indent=4)}")    