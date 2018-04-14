import requests

headers = {'content-type': 'application/json'}

def get(year='2017', skip=0):
    payload = { '$filter': 'Ar eq ' + year, '$skip': skip}
    return requests.get("http://tsopendata.azure-api.net/Vagtrafikolyckor/v0.13/Olycksniva", params=payload, headers=headers)
