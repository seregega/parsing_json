import json
import math
import os
from re import T
import requests
from pickle import dumps
def compare_snmpS5():
    r8 = requests.get('http://192.168.0.242/snmpS5.json')
    print('snmpS5')
    snmpS5 = r8.json()
    print(snmpS5)
    param_snmpS5 = ['belt', 'time_mode', 'ntp']
    with open("snmpS5.json", 'r') as test_data:
        receivesnmpS5 = json.loads(test_data.read())
        print(receivesnmpS5)
    for i in param_snmpS5:
        if snmpS5.get(i) == receivesnmpS5.get(i):
            print(i, ': PASS')
        else:
            print(i, '- FAIL', receivesnmpS5.get(i))
    print('\n')
    if snmpS5.get('time') <= receivesnmpS5.get('time'):
        print('time: PASS')
    else:
        print('time: FAIL')
    #     if snmpS5.get("belt") == receivesnmpS5.get("belt"):
    #         print(True)
    #     if snmpS5.get('time_mode') == receivesnmpS5.get('time_mode'):
    #         print(True)
    #     if snmpS5.get('ntp') == receivesnmpS5.get('ntp'):
    #         print(True)
    # return True
def main():
    compare_snmpS5()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()