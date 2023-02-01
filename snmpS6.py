import json
import math
import os
import requests
from pickle import dumps
def compare_snmpS6():
    r9 = requests.get('http://192.168.0.242/snmpS6.json')
    snmpS6 = r9.json()
    print('snmpS6')
    param_snmpS6 = ['s-cron-name1', 's-cron-range1', 's-cron-date1', 's-cron-name2', 's-cron-range2', 's-cron-date2']
    with open("snmpS6.json", 'r') as test_data:
        receivesnmpS6 = json.loads(test_data.read())
    for i in param_snmpS6:
        if snmpS6.get(i) == receivesnmpS6.get(i):
            print(i, ': PASS')
        else:
            print(i, '___=====FAIL=====___', receivesnmpS6.get(i))
    print('\n')
        # if snmpS6.get('s-cron-name1') == receivesnmpS6.get('s-cron-name1'):
        #     print(True)
        # if snmpS6.get('s-cron-range1') == receivesnmpS6.get('s-cron-range1'):
        #     print(True)
        # if snmpS6.get('s-cron-date1') == receivesnmpS6.get('s-cron-date1'):
        #     print(True)
        # if snmpS6.get('s-cron-name2') == receivesnmpS6.get('s-cron-name2'):
        #     print(True)
        # if snmpS6.get('s-cron-range2') == receivesnmpS6.get('s-cron-range2'):
        #     print(True)
        # if snmpS6.get('s-cron-date2') == receivesnmpS6.get('s-cron-date2'):
        #     print(True)

def main():
    compare_snmpS6()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()