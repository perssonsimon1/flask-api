from app import app
from app.tsn import accidents
import json

def sortedList(numElements, keyFunc, descending = True, keyFuncReturnsList = False):
    itemDict = dict()
    result = accidents.get().json()['value']
    for item in result:
        keyRet = keyFunc(item)
        if keyFuncReturnsList:
            keys = keyRet
        else:
            keys = [keyRet]
        
        for key in keys:
            if key in itemDict:
                itemDict[key] += 1
            else:
                itemDict[key] = 1
    
    itemsInList = sorted(itemDict.items(), key = lambda it: it[1], reverse = descending)
    list_result = list()
    for thing, count in itemsInList:
        list_result.append({
            "item": thing,
            "count": count
        })
    
    final = {
        "list": list_result
    }
    return json.dumps(final, ensure_ascii=False)