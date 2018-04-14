from app import app
from app.tsn import accidents
from app.common.converter import convert_to_geojson, convert_to_geojson_id
from app.common.sorter import sorted_list
import json

@app.route('/api/accidents/<year>')
def acc(year):
    new_result = list()

    result = list()

    has_data = True
    skip_counter = 0
    while has_data:
        res = accidents.get(year, skip_counter).json()['value']
        if len(res) > 0:
            for r in res:
                result.append(r)
            skip_counter += 10000
        else:
            has_data = False

    for item in result:
        new_result.append(convert_to_geojson(item))
    final = {
        "type": "FeatureCollection",
        "features": new_result
    }
    return json.dumps(final, ensure_ascii=False)

@app.route('/api/accidents/pos/<year>')
def acc_pos(year):
    new_result = list()

    result = list()

    has_data = True
    skip_counter = 0
    while has_data:
        res = accidents.get(year, skip_counter).json()['value']
        if len(res) > 0:
            for r in res:
                result.append(r)
            skip_counter += 10000
        else:
            has_data = False

    for item in result:
        new_result.append(convert_to_geojson_id(item))
    final = {
        "type": "FeatureCollection",
        "features": new_result
    }
    return json.dumps(final, ensure_ascii=False)



@app.route('/api/accidents/count/<year>')
def municipality(year):
    return json.dumps(sorted_list(20, lambda item: item['Kommun'], True, year), ensure_ascii=False)

