import sys
import time
import argparse
from datetime import datetime
from base import MiBand2
from constants import ALERT_TYPES

parser = argparse.ArgumentParser()
parser.add_argument('-m', '--mac', required=True, help='Mac address of the device')
args = parser.parse_args()

MAC = args.mac # sys.argv[1]

band = MiBand2(MAC, debug=True)
band.setSecurityLevel(level="medium")

band.authenticate()

def l(x):
    print ('Realtime heart:', x)


def b(x):
    print ('Raw heart:', x)


def f(x):
    print ('Raw accel heart:', x)

try:
    while True:
        # band.start_heart_rate_realtime(heart_measure_callback=l)
        band.start_raw_data_realtime(
                # heart_measure_callback=l,
                # heart_raw_callback=b,
                accel_raw_callback=f)
        time.sleep(2)
finally:
    band.disconnect()