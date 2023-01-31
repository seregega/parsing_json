import json
import math
import os
from re import T
import requests
from pickle import dumps
def compare_alarm():
    r3 = requests.get('http://192.168.0.242/alarm.json')
    print('alarm.json')
    alarm = r3.text
    print(alarm)
    alarm = {"up": 50,
"down": 50,
"load":100}

    error = []
    with open("alarm.json", 'r') as test_data:
        receivealarm = json.loads(test_data.read())
        print(receivealarm)
        if alarm.get("up") == receivealarm.get("up"):
            print(True)
        if alarm.get('down') == alarm.get('down'):
            print(True)
        if alarm.get('load') == receivealarm.get('load'):
            print(True)
    return True
def main():
    compare_alarm()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()