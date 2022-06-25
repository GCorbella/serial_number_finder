import os
import shutil
import datetime
import re
import math
import time
from pathlib import Path

sn = {}

def home():
    print("*" * 100)
    print("WELCOME TO PYTHON SERIAL NUMBER FINDER")
    print("*" * 100)
    directory = Path(input("In what directory do you want to search for the serial numbers? "))
    print("_" * 100)
    start = time.time()
    s_walk(directory)
    end = time.time()
    s_time = math.ceil(end - start)
    results(s_time)


def s_walk(directory):
    for dir, sdir, file in os.walk(directory):
        rute = Path(dir)
        for f in file:
            r_file = rute / f
            sin_sn = search_in(r_file)
            if sin_sn != False:
                sn[f] = [sin_sn]


def search_in(rute):
    f = open(rute,"r")
    text = f.read()
    return s_pattern(text)


def s_pattern(text):
    sn_pattern = r"N\w{3}\-\d{5}"
    s_serial = re.search(sn_pattern,text)
    if s_serial == None:
        return False
    else:
        return(s_serial.group())


def results(s_time):
    print(f"Search date: {datetime.date.today()}\n")
    print("FILE\t\t\tS.NUMBER")
    iteration = 0
    for key in sn:
        print(key, "\t", sn[key][0])
        iteration += 1
    print("")
    print(f"Serial numbers found = {len(sn)}")
    print(f"Search duration = {s_time} seconds")

home()