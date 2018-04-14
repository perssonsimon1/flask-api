from app import app
from app.tsn import accidents
from app.common.converter import convert_to_geojson
import json

@app.route('/api/acc')
def publish():
    new_result = list()
    result = accidents.get().json()['value']
    for item in result:
        new_result.append(convert_to_geojson(item))
    final = {
        "type": "FeatureCollection",
        "features": new_result
    }
    return json.dumps(final, ensure_ascii=False)
