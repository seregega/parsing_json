import json
import math
import os
from re import T
import requests
from pickle import dumps
def compare_alarm():
    r3 = requests.get('http://192.168.0.242/alarm.json')
    print('alarm.json')
    alarm = r3.json()
    print(alarm)
    param_alarm = ['up', 'down', 'load']
    with open("alarm.json", 'r') as test_data:
        receivealarm = json.loads(test_data.read())
        print(receivealarm)
    for i in param_alarm:
        if alarm.get(i) == receivealarm.get(i):
            print(i, ': PASS')
        else:
            print(i, '- FAIL', receivealarm.get(i))
    print('\n')

def main():
    compare_alarm()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()