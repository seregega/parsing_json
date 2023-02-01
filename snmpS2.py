import json
import math
import os
from re import T
import requests
from pickle import dumps
def compare_snmpS2():
    r5 = requests.get('http://192.168.0.242/snmpS2.json')
    print('snmpS2')
    snmpS2 = r5.json()
    print(snmpS2)
    param_snmpS2 = ['Dinp', 'Dinp2', 'Rout1', 'Rout2', 'Rout3', 'RoutN1', 'RoutN2', 'RoutN3']
    with open("snmpS2.json", 'r') as test_data:
        receivesnmpS2 = json.loads(test_data.read())
        print(receivesnmpS2)
    for i in param_snmpS2:
        if snmpS2.get(i) == receivesnmpS2.get(i):
            print(i, ': PASS')
        else:
            print(i, '- FAIL', receivesnmpS2.get(i))
    print('\n')
    # with open("snmpS2.json", 'r') as test_data:
    #     receivesnmpS2 = test_data.read()
    #     print(len(snmpS2), len(receivesnmpS2))
    #     print(receivesnmpS2)
    #     for i in range(len(receivesnmpS2)):
    #         if snmpS2[i] == receivesnmpS2[i]:
    #             pass
    #         else:
    #             texter = [snmpS2[i - 100:i]]
    #             texter.extend(error)
    #     print(error)
    #     print("Тест пройден")
    # return True
def main():
    compare_snmpS2()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()