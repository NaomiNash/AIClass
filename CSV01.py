#!/usr/bin/env python3

import csv
import re

if __name__ == '__main__' :
    myFile = open('Animals.csv','r')
    myReader = csv.reader(myFile)
    headers = None
    for line in myReader :
        for i in range(0, len(line)) :
            line[i] = (line[i].strip())    
            if headers is None :
                headers = line
                print(headers)
            else :
                if i == len(line)-1 :
                    line[i] = bool(line[i])
        print(line)
    print('Hello, World')
