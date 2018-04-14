from firebase_admin import firestore
from app.tsn import accidents

db = firestore.client()


docs = db.collection(u'municipalities').get()

p = dict()



for doc in docs:
    p[doc.id] = doc.to_dict()


print(p)
