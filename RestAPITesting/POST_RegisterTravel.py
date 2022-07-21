import requests
from json                                   import dumps
from requests.structures                    import CaseInsensitiveDict
from RestAPITesting._util.AddressURL        import AddressURL

def registerTravel(adminToken, requestType):

    URL = AddressURL().getURL(requestType)
    
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = adminToken

    data = """
    {
        "acompanhante": "Nenhum",
        "dataPartida": "2022-07-20",
        "dataRetorno": "2022-08-20",
        "localDeDestino": "Bahia",
        "regiao": "Norte"
    }
"""

    resp = requests.post(url=URL ,headers=headers, data=data)

    for headItem_k, headItem_v in resp.headers.items():
        print(f'{headItem_k:>23}: {headItem_v}')
    
    print(f"Body: \n {dumps(resp.json(), indent=4)}")

    jsonData = resp.json()
    
    if resp.status_code == 201:
        return jsonData['data']
    else: 
        return False