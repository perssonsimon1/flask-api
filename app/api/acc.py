from app import app
from app.tsn.accidents import r

@app.route('/api/acc')
def publish():
    result = r.json()
    return str(result['value'])
