from app import app
from app.tsn import accidents
import json
from app.common.sorter import sorted_list

@app.route('/api/roads')
def roads(year):
    return json.dumps(sorted_list(20, lambda item: item['Olycksvag'], True), ensure_ascii=False)
