import json
import math
import os
from re import T
import requests
from pickle import dumps
def compare_snmpS2():
    r5 = requests.get('http://192.168.0.242/snmpS2.json')
    print('snmpS2')
    snmpS2 = r5.text
    print(snmpS2)
    error = []
    with open("snmpS2.json", 'r') as test_data:
        receivesnmpS2 = test_data.read()
        print(len(snmpS2), len(receivesnmpS2))
        print(receivesnmpS2)
        for i in range(len(receivesnmpS2)):
            if snmpS2[i] == receivesnmpS2[i]:
                pass
            else:
                texter = [snmpS2[i - 100:i]]
                texter.extend(error)
        print(error)
        print("Тест пройден")
    return True
def main():
    compare_snmpS2()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()