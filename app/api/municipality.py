from app import app
from firebase_admin import firestore
import json

db = firestore.client()

@app.route('/api/municipality')
def muni():
    docs = db.collection('stats').get()
    items = list()
    for doc in docs:
        items.append(doc.to_dict())
    return json.dumps(items, ensure_ascii=False)




