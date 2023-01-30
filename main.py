# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json
import math
import os
from re import T
import requests
from pickle import dumps


def main():
    # r1 = requests.get('http://192.168.0.242/prms.json')
    # # print('prms.json')
    # # print(r1.text)
    # jsonData = r1.text
    # dictReceive = json.loads(jsonData)
    # print(dictReceive)

    with open('test_case2.json', 'r') as test_case:
        dictEtalon = json.loads(test_case.read())
    print(dictEtalon)
    # print(math.floor(float(dictEtalon.get('commands')[0].get("IP_fault_voltage_V"))))
    with open('prms_2run.json', 'r') as prms:
        dictReceive = json.loads(prms.read())
    print(dictReceive)

    # print(dictReceive.get('IP_voltage_V'))
    def compareprms():
        if (math.floor(float(dictEtalon.get('commands')[0].get('IP_voltage_V')))) == dictReceive.get('IP_voltage_V'):
            print(True)
        if (math.floor(float(dictEtalon.get('commands')[0].get('IP_fault_voltage_V')))) == dictReceive.get(
                'IP_fault_voltage_V'):
            print(True)
        if (math.floor(float(dictEtalon.get('commands')[0].get('OP_voltage_V')))) == dictReceive.get('OP_voltage_V'):
            print(True)
        if (math.floor(float(dictEtalon.get('commands')[0].get('OP_current_PERC')))) == dictReceive.get('OP_current_PERC'):
            print(True)
        if (math.floor(float(dictEtalon.get('commands')[0].get('IP_freq_HZ')))) == dictReceive.get('IP_freq_HZ'):
            print(True)
        if (math.floor(float(dictEtalon.get('commands')[0].get('BATT_V')))) == dictReceive.get('BATT_V'):
            print(True)
        else:
            print(dictReceive.get('BATT_V'))
        if (math.floor(float(dictEtalon.get('commands')[0].get('Temp_DEG')))) == dictReceive.get('Temp_DEG'):
            print(True)
        if (math.floor(float(dictEtalon.get('commands')[0].get('_7_Utility_fault__')))) == dictReceive.get(
                '_7_Utility_fault__'):
            print(True)
        if (math.floor(float(dictEtalon.get('commands')[0].get('_5_Bypass_act__')))) == dictReceive.get('_5_Bypass_act__'):
            print(True)
        if (math.floor(float(dictEtalon.get('commands')[0].get('_4_UPS_failed__')))) == dictReceive.get('_4_UPS_failed__'):
            print(True)
        if (math.floor(float(dictEtalon.get('commands')[0].get('_3_UPS_type__')))) == dictReceive.get('_3_UPS_type__'):
            print(True)
        if (math.floor(float(dictEtalon.get('commands')[0].get('_2_Test_in_progress__')))) == dictReceive.get(
                '_2_Test_in_progress__'):
            print(True)
        if (math.floor(float(dictEtalon.get('commands')[0].get('_1_Shutdown_act__')))) == dictReceive.get(
                '_1_Shutdown_act__'):
            print(True)
        if (math.floor(float(dictEtalon.get('commands')[0].get('_0_Beeper_on__')))) == dictReceive.get('_0_Beeper_on__'):
            print(True)
    #compareprms()
    for filename in ['test_case1.json', 'test_case2.json', 'test_case3.json', 'test_case4.json', 'test_case5.json', 'test_case6.json', 'test_case7.json', 'test_case8.json', 'test_case9.json', 'test_case10.json']:
        compareprms()

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
