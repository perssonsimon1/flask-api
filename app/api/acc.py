from app import app
from app.tsn.accidents import r
from app.common import geojson
import json

@app.route('/api/acc')
def publish():
    new_result = list()
    result = r.json()['value']
    for item in result:
        new_result.append(geojson.convert(item))
    result = json.dumps(new_result, ensure_ascii=False)
    return result.encode('utf8')
