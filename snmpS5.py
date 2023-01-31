import json
import math
import os
from re import T
import requests
from pickle import dumps
def compare_snmpS5():
    r8 = requests.get('http://192.168.0.242/snmpS5.json')
    print('snmpS5')
    snmpS5 = r8.text
    print(snmpS5)
    snmpS5 = {"belt":" +3",
"time_mode":"0",
"ntp":"0.0.0.0",
"time":" 946685866"}
    error = []
    with open("snmpS5.json", 'r') as test_data:
        receivesnmpS5 = json.loads(test_data.read())
        print(receivesnmpS5)
        if snmpS5.get("belt") == receivesnmpS5.get("belt"):
            print(True)
        if snmpS5.get('time_mode') == receivesnmpS5.get('time_mode'):
            print(True)
        if snmpS5.get('ntp') == receivesnmpS5.get('ntp'):
            print(True)
        if snmpS5.get('time') != None:
            print(True)
    return True
def main():
    compare_snmpS5()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()