from app import app
from firebase_admin import firestore

db = firestore.client()

@app.route('/write')
def hello():
    doc_ref = db.collection(u'users').document(u'alovelace')
    doc_ref.set({
        u'first': u'Ada',
        u'last': u'Lovelace',
        u'born': 1815
    })
    return "Done!"

@app.route('/read')
def hello():
    users_ref = db.collection(u'users')
    docs = users_ref.get()

    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))
    return "See result in terminal"
