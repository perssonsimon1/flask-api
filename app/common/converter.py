intensity = {
    "Dödsolycka": 4,
    "Svår olycka": 3,
    "Lindrig olycka": 2,
    "Okänd svårhetsgrad": 1,
    "Ej personskadeolycka": 0
}


def convert_to_geojson(obj):
    involved = convert_involvement(obj)
    geojson = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [obj['Longitud'], obj['Latitud']]
        },
        "properties": {
            "name": obj['Id'],
            "locationType": obj['Platstyp'],
            "accidentType": obj['Olyckstyp'],
            "intensity": intensity[obj['Svarighetsgrad']],
            "roadCondition": obj['Vaglag'],
            "weather": obj['Vaderlek'],
            "lightCondition": obj['Ljusforhallande'],
            "involved": involved,
            "involvedSize": len(involved)
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



