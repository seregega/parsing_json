import json
import math
import os
import requests
from pickle import dumps
def compare_prms2():
    r2 = requests.get('http://192.168.0.242/prms2.json')
    print('prms2.json')
    prms2 = r2.json()
    print(prms2)

    with open("prms2.json", 'r') as test_data:
        receiveprms2 = json.loads(test_data.read())
        print(receiveprms2)
        param_prms2 = ["upsIdentModel", "upsIdentUPSSoftwareVersion", "MAC_ADDR", "UPS_DATE", "UPS_SERIAL", "SNMP_SYSNAME", "SNMP_SYSCONTACT", "SNMP_SYSLOCATION", "SNMP_SYSDESCR" ]
        with open("prms2.json", 'r') as test_data:
            receiveprms2 = json.loads(test_data.read())
            print(receiveprms2)
        for i in param_prms2:
            if prms2.get(i) == receiveprms2.get(i):
                print(i, ': PASS')
            else:
                print(i, '- FAIL', receiveprms2.get(i))
        print('\n')
        if prms2.get("SYS_UPTIME") <= receiveprms2.get("SYS_UPTIME"):
            print("SYS_UPTIME: PASS")
        else:
            print("SYS_UPTIME: FAIL")
    #     if prms2.get("SYS_UPTIME") == receiveprms2.get("SYS_UPTIME"):
    #         print(True)
    #     if prms2.get("upsIdentModel") == receiveprms2.get("upsIdentModel"):
    #         print(True)
    #     if prms2.get("upsIdentUPSSoftwareVersion") == receiveprms2.get("upsIdentUPSSoftwareVersion"):
    #         print(True)
    #     if prms2.get("MAC_ADDR") == receiveprms2.get("MAC_ADDR"):
    #         print(True)
    #     if prms2.get("UPS_DATE") == receiveprms2.get("UPS_DATE"):
    #         print(True)
    #     if prms2.get("UPS_SERIAL") == receiveprms2.get("UPS_SERIAL"):
    #         print(True)
    #     if prms2.get("SNMP_SYSNAME") == receiveprms2.get("SNMP_SYSNAME"):
    #         print(True)
    #     if prms2.get("SNMP_SYSCONTACT") == receiveprms2.get("SNMP_SYSCONTACT"):
    #         print(True)
    #     if prms2.get("SNMP_SYSLOCATION") == receiveprms2.get("SNMP_SYSLOCATION"):
    #         print(True)
    #     if prms2.get("SNMP_SYSDESCR") == receiveprms2.get("SNMP_SYSDESCR"):
    #         print(True)
    # return True
def main():
    compare_prms2()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
