from app import app
from app.tsn import accidents
import json
from app.common.sorter import sorted_list

@app.route('/api/roads/<year>')
def roads(year):
    return json.dumps(sorted_list(20, lambda item: map(lambda it: it.strip(), item['Olycksvag'].split(',')), True, year, True), ensure_ascii=False)
