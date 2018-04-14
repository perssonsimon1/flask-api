from app import app
from firebase_admin import firestore
from app.tsn.accidents import r

db = firestore.client()

@app.route('/acc')
def publish():
    collection = db.collection('poi')
    result = r.json()
    for item in result['value']:
        collection.document(str(item['Id'])).set({
            u'lng': item['Longitud'],
            u'lat': item['Latitud']
        })
    return "hello"

@app.route('/read')
def read():
    docs = db.collection('poi').get()
    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))
    return "t"
