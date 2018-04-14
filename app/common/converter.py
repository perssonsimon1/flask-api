from app.common.const import intensity_dict, weather_dict, locationType_dict, lightCondition_dict

def convert_to_geojson_info(obj):
    involved = convert_involvement(obj)
    geojson = {
        "locationType": locationType_dict[obj['Platstyp']],
        "accidentType": obj['Olyckstyp'],
        "region": obj['Lan'],
        "municipality": obj['Kommun'],
        "road": obj['Olycksvag'],
        "roadCondition": obj['Vaglag'],
        "weather": weather_dict[obj['Vaderlek']],
        "lightCondition": lightCondition_dict[obj['Ljusforhallande']],
        "involved": involved
    }

    return geojson

def convert_to_geojson_id(obj):
    involved = convert_involvement(obj)
    geojson = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [obj['Longitud'], obj['Latitud']]
        },
        "properties": {
            "name": obj['Id'],
            "accidentType": accidentType_dict[obj['Olyckstyp']],
            "month": obj['Manad'],
            "in": intensity_dict[obj['Svarighetsgrad']],
            "inv": len(involved)
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



