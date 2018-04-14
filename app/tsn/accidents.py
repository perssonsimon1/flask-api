import requests

headers = {'content-type': 'application/json'}

def get():
    payload = { '$filter': 'Ar eq 2017'}
    return requests.get("http://tsopendata.azure-api.net/Vagtrafikolyckor/v0.13/Olycksniva", params=payload, headers=headers)
