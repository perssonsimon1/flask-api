intensity = {
    "Dödsolycka": 4,
    "Svår olycka": 3,
    "Lindrig olycka": 2,
    "Okänd svårhetsgrad": 1,
    "Ej personskadeolycka": 0
}


def convert_to_geojson(obj):
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
            "intensity": intensity[obj['Svarighetsgrad']],
            "road_condition": obj['Vaglag'],
            "weather": obj['Vaderlek'],
            "light_condition": obj['Ljusforhallande'],
            "involved": convert_involvement(obj)
        }
    }

    return geojson

def convert_involvement(obj):
    prefix = "Trafikelement"
    items = list()
    for i in range(1, 22):
        item = obj[prefix + str(i)]
        if item:
            items.append(item)
        else:
            return items
    return items



