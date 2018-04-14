import requests

headers = {'content-type': 'application/json'}

dataCache = dict()

def get(year='2017', skip=0):
    if year in dataCache:
        if skip in dataCache[year]:
            return dataCache[year][skip]
    
    payload = { '$filter': 'Ar eq ' + year, '$skip': skip}
    data = requests.get("http://tsopendata.azure-api.net/Vagtrafikolyckor/v0.13/Olycksniva", params=payload, headers=headers)
    if not (year in dataCache):
        dataCache[year] = dict()
    dataCache[year][skip] = data

    return data
