import requests

payload = { '$filter': 'Ar eq 2017'}

headers = {'content-type': 'application/json'}

r = requests.get("http://tsopendata.azure-api.net/Vagtrafikolyckor/v0.13/Olycksniva", params=payload, headers=headers)

