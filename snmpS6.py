import json
import math
import os
from re import T
import requests
from pickle import dumps
def compare_snmpS6():
    r9 = requests.get('http://192.168.0.242/snmpS6.json')
    print('snmpS6')
    snmpS6 = {"s-cron-name1":"short_akb_test",
"s-cron-range1":"   0",
"s-cron-date1":"0.0.0 0:0",
"s-cron-name2":"relay_out",
"s-cron-range2":"   0",
"s-cron-date2":"0.0.0 0:0"}
    print(type(snmpS6))
    error = []
    with open("snmpS6.json", 'r') as test_data:
        receivesnmpS6 = json.loads(test_data.read())
        print(type(receivesnmpS6))
        if snmpS6.get('s-cron-name1') == receivesnmpS6.get('s-cron-name1'):
            print(True)
        if snmpS6.get('s-cron-range1') == receivesnmpS6.get('s-cron-range1'):
            print(True)
        if snmpS6.get('s-cron-date1') == receivesnmpS6.get('s-cron-date1'):
            print(True)
        if snmpS6.get('s-cron-name2') == receivesnmpS6.get('s-cron-name2'):
            print(True)
        if snmpS6.get('s-cron-range2') == receivesnmpS6.get('s-cron-range2'):
            print(True)
        if snmpS6.get('s-cron-date2') == receivesnmpS6.get('s-cron-date2'):
            print(True)

def main():
    compare_snmpS6()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()