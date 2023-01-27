# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json
import math
from re import T
import requests
from pickle import dumps

def main():
    r1 = requests.get('http://192.168.0.242/prms.json')
    # print('prms.json')
    # print(r1.text)
    jsonData = r1.text
    dictReceive = json.loads(jsonData)
    print(dictReceive)

    with open('test_case10.json', 'r') as test_case:
        dictEtalon = json.loads(test_case.read())
    print(dictEtalon)
    print(math.floor(float(dictEtalon.get('commands')[0].get('IP_voltage_V'))))
    # print(dictReceive.values())



    '''
    r2 = requests.get('http://192.168.0.242/prms2.json')
    print('prms2.json')
    prms2 = r2.text
    print(prms2)
    r3 = requests.get('http://192.168.0.242/alarm.json')
    print('alarm.json')
    alarm = r3.text
    print(alarm)
    r4 = requests.get('http://192.168.0.242/snmpS.json')
    print('snpmS')
    snmpS = r4.text
    print(snmpS)
    r5 = requests.get('http://192.168.0.242/snmpS2.json')
    print('snmpS2')
    snmpS2 = r5.text
    print(snmpS2)
    r6 = requests.get('http://192.168.0.242/snmpS3.json')
    print('snmpS3')
    snmpS3 = r6.text
    print(snmpS3)
    r7 = requests.get('http://192.168.0.242/snmpS4.json')
    print('snmpS4')
    snmpS4 = r7.text
    print(snmpS4)
    r8 = requests.get('http://192.168.0.242/snmpS5.json')
    print('snmpS5')
    snmpS5 = r8.text
    print(snmpS5)
    r9 = requests.get('http://192.168.0.242/snmpS6.json')
    print('snmpS6')
    snmpS6 = r9.text
    print(snmpS6)
    r10 = requests.get('http://192.168.0.242/logList.json')
    print('LogList')
    LogList = r10.text
    print(LogList)
    r11 = requests.get('http://192.168.0.242/logger.csv')
    print('logger')
    logger = r11.text
    print(logger)
    '''
    # def compareDicts(a: dict[str, T], b: dict[str, T]):
    #     result = {}
    #
    #     for fieldName in a:
    #         compareItem = {'left': a[fieldName]}
    #         if b.keys().__contains__(fieldName):
    #             compareItem['right'] = b[fieldName]
    #             if isinstance(compareItem['left'], (float, int)) & isinstance(compareItem['right'], (float, int)):
    #                 compareItem['equals'] = int(compareItem['left']) == int(compareItem['right'])
    #             else:
    #                 compareItem['equals'] = False
    #         else:
    #             compareItem['right'] = None
    #             compareItem['equals'] = False
    #
    #         result[fieldName] = compareItem
    #
    #     for fieldName in b:
    #         if not result.keys().__contains__(fieldName):
    #             compareItem = {
    #                 'left': None,
    #                 'right': b[fieldName],
    #                 'equals': False
    #             }
    #
    #             result[fieldName] = compareItem
    #
    #     return result
    #
    # with open('test_case10.json', 'r') as test_data:
    #     case10 = test_data.read()
    #     dict1 = prms
    #     dict2 = case10
    """
    with open('prms.json', 'w') as my_file:
        my_file.write(prms)
    """



    # compareResult = compareDicts(dict1, dict2)
    # for field in compareResult:
    #     compareItem = compareResult[field]
    #     if not compareItem['equals']:
    #         print('field %s differs: %s and %s' % (field, compareItem['left'], compareItem['right']))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
