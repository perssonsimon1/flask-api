from app import app
from app.tsn import accidents
from app.common import geojson
import json

@app.route('/api/acc')
def publish():
    new_result = list()
    result = accidents.get().json()['value']
    for item in result:
        new_result.append(geojson.convert(item))
    final = {
        "type": "FeatureCollection",
        "features": new_result
    }
    return json.dumps(final, ensure_ascii=False)
