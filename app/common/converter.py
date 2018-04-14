from app.common.const import accidentType_dict, intensity_dict, weather_dict, locationType_dict, lightCondition_dict


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
            "locationType": locationType_dict[obj['Platstyp']],
            "accidentType": accidentType_dict[obj['Olyckstyp']],
            "year": obj['Ar'],
            "month": obj['Manad'],
            "region": obj['Lan'],
            "municipality": obj['Kommun'],
            "intensity": intensity_dict[obj['Svarighetsgrad']],
            "road": obj['Olycksvag'],
            "roadCondition": obj['Vaglag'],
            "weather": weather_dict[obj['Vaderlek']],
            "lightCondition": lightCondition_dict[obj['Ljusforhallande']],
            "involved": involved,
            "involvedSize": len(involved)
        }
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
            "name": obj['Id']
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



