from app import app
from app.tsn import accidents
from app.common.converter import convert_to_geojson
from app.common.sorter import sorted_list
import json

@app.route('/api/accidents/<year>')
def acc(year):
    new_result = list()
    result = accidents.get(year).json()['value']
    for item in result:
        new_result.append(convert_to_geojson(item))
    final = {
        "type": "FeatureCollection",
        "features": new_result
    }
    return json.dumps(final, ensure_ascii=False)



@app.route('/api/accidents/count/<year>')
def municipality(year):
    return json.dumps(sorted_list(20, lambda item: item['Kommun'], True, year), ensure_ascii=False)

