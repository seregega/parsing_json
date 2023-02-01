import json
import math
import os
import requests
from pickle import dumps
def compare_snmpS():
    r4 = requests.get('http://192.168.0.242/snmpS.json')
    print('snpmS')
    snmpS = r4.json()
    print(snmpS)
    param_snmpS = ['s_serv1', 's_serv2', 's_serv3', 's_serv4', 's_serv5', 'r_com', 'w_com']

    error = []
    with open("snmpS.json", 'r') as test_data:
        receivesnmpS = json.loads(test_data.read())
    for i in param_snmpS:
        if snmpS.get(i) == receivesnmpS.get(i):
            print(i, ': PASS')
        else:
            print(i, '___=====FAIL=====___', receivesnmpS.get(i))
    print('\n')
        # if snmpS.get('s_serv2') == receivesnmpS.get('s_serv2'):
        #     print(True)
        # if snmpS.get('s_serv3') == receivesnmpS.get('s_serv3'):
        #     print(True)
        # if snmpS.get('s_serv4') == receivesnmpS.get('s_serv4'):
        #     print(True)
        # if snmpS.get('s_serv5') == receivesnmpS.get('s_serv5'):
        #     print(True)
        # if snmpS.get('r_com') == receivesnmpS.get('r_com'):
        #     print(True)
        # if snmpS.get('w_com') == receivesnmpS.get('w_com'):
        #     print(True)
def main():
    compare_snmpS()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()