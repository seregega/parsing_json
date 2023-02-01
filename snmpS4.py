import json
import math
import os
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
            print(i, '___=====FAIL=====___', receivesnmpS4.get(i))
    print('\n')
def main():
    compare_snmpS4()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()