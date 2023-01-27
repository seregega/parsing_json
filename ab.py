from re import T


def compareDicts(a: dict[str, T], b: dict[str, T]):
    result = {}

    for fieldName in a:
        compareItem = {'left': a[fieldName]}
        if b.keys().__contains__(fieldName):
            compareItem['right'] = b[fieldName]
            if isinstance(compareItem['left'], (float, int)) & isinstance(compareItem['right'], (float, int)):
                compareItem['equals'] = int(compareItem['left']) == int(compareItem['right'])
            else:
                compareItem['equals'] = False
        else:
            compareItem['right'] = None
            compareItem['equals'] = False

        result[fieldName] = compareItem

    for fieldName in b:
        if not result.keys().__contains__(fieldName):
            compareItem = {
                'left': None,
                'right': b[fieldName],
                'equals': False
            }

            result[fieldName] = compareItem

    return result


# test
dict1: dict[str, float] = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}
dict2 = {
    'b': 2,
    'c': 3.2,
    'd': 7,
    'e': 5
}

compareResult = compareDicts(dict1, dict2)
for field in compareResult:
    compareItem = compareResult[field]
    if not compareItem['equals']:
        print('field %s differs: %s and %s' % (field, compareItem['left'], compareItem['right']))