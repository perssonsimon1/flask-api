from app import app
from firebase_admin import firestore
from app.tsn.accidents import r

db = firestore.client()

@app.route('/acc')
def hello():
    result = r.json()
    return str(result['value'])
