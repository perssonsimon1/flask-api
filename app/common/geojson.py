
def convert(obj):
    geojson = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [obj['Longitud'], obj['Latitud']]
        },
        "properties": {
            "name": obj['Id'],
            "location_type": obj['Platstyp'],
            "accident_type": obj['Olyckstyp'],
            "intensity": obj['Svarighetsgrad'],
            "road_condition": obj['Vaglag'],
            "weather": obj['Vaderlek'],
            "light_condition": obj['Ljusforhallande']
        }
    }

    return geojson
