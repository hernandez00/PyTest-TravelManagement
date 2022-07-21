from json                                   import dumps
from requests.structures                    import CaseInsensitiveDict
from requests.exceptions                    import ConnectionError
from RestAPITesting._util.AddressURL        import AddressURL
import requests
import sys

def showResponse(response):
    for headItem_k, headItem_v in response.headers.items():
        print(f'{headItem_k:>23}: {headItem_v}')
    
    print(f"Body: \n {dumps(response.json(), indent=4)}")

def getToken(requestType):
    
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"

    print(headers)
    if requestType == 'ADMIN_TOKEN':
        data = """
            {
                "email": "admin@email.com",
                "senha": "654321"
            }
            """

    elif requestType == 'COMMON_TOKEN':
        data = """
            {
                "email": "usuario@email.com",
                "senha": "123456"
            }
            """    
    else: 
        print('Tipo de requisição invalida.')
        return False

    requestType = 'TOKEN'

    URL = AddressURL().getURL(requestType)

    try:
        resp = requests.post(url=URL, headers=headers, data=data)
    except ConnectionError as erro:
        print(f'Impossível se conectar: \nErrno: {erro.errno} \nFilename: {erro.filename} \nFilename2: {erro.filename2} \nArgs: {erro.args} '+
               '\nRequest: {erro.request} \nstrError: {erro.strerror} \nWinerror: {erro.winerror} \n')
        sys.exit()
    
    showResponse(resp)

    jsonData = resp.json()

    if resp.status_code == 200:
        return jsonData['data']['token']
    else: 
        return False