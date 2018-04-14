from app import app
from app.tsn import accidents
import json

def sorted_list(numElements, keyFunc, descending=True, year='2017'):
    item_dict = dict()
    result = accidents.get().json()['value']
    for item in result:
        key = keyFunc(item)
        if key in item_dict:
            item_dict[key] += 1
        else:
            item_dict[key] = 1

    items_in_list = sorted(item_dict.items(), key = lambda it: it[1], reverse = descending)
    list_result = list()
    for thing, count in items_in_list:
        list_result.append({
            "name": thing,
            "count": count
        })

    return list_result
