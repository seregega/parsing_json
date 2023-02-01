import json
import math
import os
import requests
from pickle import dumps
def compare_snmpS3():
    r6 = requests.get('http://192.168.0.242/snmpS3.json')
    print('snmpS3')
    snmpS3 = r6.json()
    print(snmpS3)
    param_snmpS3 = ['IPA', 'IPG', 'mask', 'auto']
    with open("snmpS3.json", 'r') as test_data:
        receivesnmpS3 = json.loads(test_data.read())
        print(receivesnmpS3)
    for i in param_snmpS3:
        if snmpS3.get(i) == receivesnmpS3.get(i):
            print(i, ': PASS')
        else:
            print(i, '___=====FAIL=====___', receivesnmpS3.get(i))
    print('\n')
    # with open("snmpS3.json", 'r') as test_data:
    #     receivesnmpS3 = test_data.read()
    #     print(len(snmpS3), len(receivesnmpS3))
    #     print(receivesnmpS3)
    #     for i in range(len(receivesnmpS3)):
    #         if snmpS3[i] == receivesnmpS3[i]:
    #             pass
    #         else:
    #             texter = [snmpS3[i - 100:i]]
    #             texter.extend(error)
    #     print(error)
    #     print("Тест пройден")
    # return True
def main():
    compare_snmpS3()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()