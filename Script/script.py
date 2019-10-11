import argparse
import sys
import os
import csv
import re

R=re.compile("\D+(\d\d\d\d)-(\d\d\d\d)\D+")
def yearUpdate( filepath ):
    with open(filepath,'r+') as f:
        lines = [line.rstrip('\n') for line in open(filepath)]
        for x in lines:
            '''date = re.match(R,str(x))'''
            for date in R.finditer(x):
                if date:
                    print(filepath)
                    print(date.groups())
                    if date.group(2)<"2019":
                        '''R.sub('2019',str(x),count=2)'''
                        str(x).replace(str(date.group(2)),"2019")
                        print(str(x))
        

parser = argparse.ArgumentParser(description='Update Copyright for GAMS files.')
parser.add_argument('-p', help='folder path for the repository')
"""parser.add_argument('-y', help='Current year') will be implemented later either with a date module or manually"""

"""if there are no arguments show help"""
if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit(1)   
    
"""if there are incorrect arguments, show help"""
try:
    options = parser.parse_args()
except:
    parser.print_help()
    sys.exit(0)

args = parser.parse_args()
"""data_folder = Path()"""
"""
print(args)
print(sys.argv)
print(sys.argv[2]) inline function"""

""" get the files list """
path = str(sys.argv[2])

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if file.endswith('.pri'):
            files.append(os.path.join(r, file))
        elif file.endswith('.h'):
            files.append(os.path.join(r, file))
        elif file.endswith('.pro'):      
            files.append(os.path.join(r, file))
        elif file.endswith('.cpp'):
            files.append(os.path.join(r, file))
for f in files:
    yearUpdate(f)

check = input('These files will be altered, are you sure you want to proceed? Y/N: ')
if check == 'n' or check == 'N':
    print('The script will be exited. You can restart the procedure with the correct path')
    sys.exit(0)