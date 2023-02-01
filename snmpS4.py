import json
import math
import os
from re import T
import requests
from pickle import dumps
def compare_snmpS4():
    r7 = requests.get('http://192.168.0.242/snmpS4.json')
    print('snmpS4')
    snmpS4 = r7.json()
    print(snmpS4)
    param_snmpS4 = ['akb_count', 'akb_capac', 'settime', 'replacetime']
    with open("snmpS4.json", 'r') as test_data:
        receivesnmpS4 = json.loads(test_data.read())
        print(receivesnmpS4)
    for i in param_snmpS4:
        if snmpS4.get(i) == receivesnmpS4.get(i):
            print(i, ': PASS')
        else:
            print(i, '- FAIL', receivesnmpS4.get(i))
    print('\n')
    # error = []
    # with open("snmpS4.json", 'r') as test_data:
    #     receivesnmpS4 = test_data.read()
    #     print(len(snmpS4), len(receivesnmpS4))
    #     print(receivesnmpS4)
    #     for i in range(len(receivesnmpS4)):
    #         if snmpS4[i] == receivesnmpS4[i]:
    #             pass
    #         else:
    #             texter = [snmpS4[i - 100:i]]
    #             texter.extend(error)
    #     print(error)
    #     print("Тест пройден")
    # return True
def main():
    compare_snmpS4()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()