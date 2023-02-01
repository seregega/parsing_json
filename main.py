# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json
import math
import os
import requests
from pickle import dumps

parameters = ["IP_voltage_V", "IP_fault_voltage_V", "OP_voltage_V", "OP_current_PERC", "IP_freq_HZ", "Temp_DEG",
              "_7_Utility_fault__", "_5_Bypass_act__", "_4_UPS_failed__", "_3_UPS_type__", "_2_Test_in_progress__", "_1_Shutdown_act__",
                "_0_Beeper_on__"]

def compareprms(test, run):
    with open(test, 'r') as test_case:
        dictEtalon = json.loads(test_case.read())
    with open(run, 'r') as prms:
        dictReceive = json.loads(prms.read())

    print(test, '\n')
    for i in parameters:
        if (math.floor(float(dictEtalon.get('commands')[0].get(i)))) == dictReceive.get(i):
            print(i, ': PASS')
        else:
            print(i, '- ___=====FAIL=====___', dictReceive.get(i))
    print('\n')

def main():
    dictEtalon = {}
    dictReceive = {}

    dict = {'test1.json': 'run1.json', 'test2.json': 'run2.json', 'test3.json': 'run3.json', 'test4.json': 'run4.json', 'test5.json': 'run5.json', 'test6.json': 'run6.json',
            'test7.json': 'run7.json', 'test8.json': 'run8.json', 'test9.json': 'run9.json', 'test10.json': 'run10.json'}

    for val in dict.items():
        compareprms(val[0], val[1])

    '''
    r2 = requests.get('http://192.168.0.242/prms2.json')
    print('prms2.json')
    prms2 = r2.text
    print(prms2)
    r3 = requests.get('http://192.168.0.242/alarm.json')
    print('alarm.json')
    alarm = r3.text
    print(alarm)
    r4 = requests.get('http://192.168.0.242/snmpS.json')
    print('snpmS')
    snmpS = r4.text
    print(snmpS)
    r5 = requests.get('http://192.168.0.242/snmpS2.json')
    print('snmpS2')
    snmpS2 = r5.text
    print(snmpS2)
    r6 = requests.get('http://192.168.0.242/snmpS3.json')
    print('snmpS3')
    snmpS3 = r6.text
    print(snmpS3)
    r7 = requests.get('http://192.168.0.242/snmpS4.json')
    print('snmpS4')
    snmpS4 = r7.text
    print(snmpS4)
    r8 = requests.get('http://192.168.0.242/snmpS5.json')
    print('snmpS5')
    snmpS5 = r8.text
    print(snmpS5)
    r9 = requests.get('http://192.168.0.242/snmpS6.json')
    print('snmpS6')
    snmpS6 = r9.text
    print(snmpS6)
    r10 = requests.get('http://192.168.0.242/logList.json')
    print('LogList')
    LogList = r10.text
    print(LogList)
    r11 = requests.get('http://192.168.0.242/logger.csv')
    print('logger')
    logger = r11.text
    print(logger)
    '''


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
