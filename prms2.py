import json
import math
import os
from re import T
import requests
from pickle import dumps
def compare_prms2():
    r2 = requests.get('http://192.168.0.242/prms2.json')
    print('prms2.json')
    prms2 = r2.text
    print(prms2)
    prms2 = {"SYS_UPTIME":  17882012,
"upsIdentModel":"                                                  MKI111/MKI211",
"upsIdentUPSSoftwareVersion":"                                                      M06_U0003",
"MAC_ADDR":"00:80:e1:00:42:42",
"UPS_DATE":"30.11.2022",
"UPS_SERIAL":"                MKI111S22010999",
"SNMP_SYSNAME":"                      SNMP name",
"SNMP_SYSCONTACT":"                   SNMP contact",
"SNMP_SYSLOCATION":"                  SNMP location",
"SNMP_SYSDESCR":"               SNMP description"
}

    error = []
    with open("prms2.json", 'r') as test_data:
        receiveprms2 = json.loads(test_data.read())
        print(receiveprms2)
        # if prms2.get("SYS_UPTIME") == receiveprms2.get("SYS_UPTIME"):
        #     print(True)
        if prms2.get("upsIdentModel") == receiveprms2.get("upsIdentModel"):
            print(True)
        if prms2.get("upsIdentUPSSoftwareVersion") == receiveprms2.get("upsIdentUPSSoftwareVersion"):
            print(True)
        if prms2.get("MAC_ADDR") == receiveprms2.get("MAC_ADDR"):
            print(True)
        if prms2.get("UPS_DATE") == receiveprms2.get("UPS_DATE"):
            print(True)
        if prms2.get("UPS_SERIAL") == receiveprms2.get("UPS_SERIAL"):
            print(True)
        if prms2.get("SNMP_SYSNAME") == receiveprms2.get("SNMP_SYSNAME"):
            print(True)
        if prms2.get("SNMP_SYSCONTACT") == receiveprms2.get("SNMP_SYSCONTACT"):
            print(True)
        if prms2.get("SNMP_SYSLOCATION") == receiveprms2.get("SNMP_SYSLOCATION"):
            print(True)
        if prms2.get("SNMP_SYSDESCR") == receiveprms2.get("SNMP_SYSDESCR"):
            print(True)
    return True
def main():
    compare_prms2()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
