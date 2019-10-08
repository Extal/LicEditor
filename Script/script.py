import argparse
import sys
import os
import csv

def yearUpdate( filepath ):
    with open(filepath) as f:
        lines = [line.rstrip('\n') for line in open(filepath)]
        print ("Read String is : ",lines[:5])
        

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

"""data_folder = Path()"""
args = parser.parse_args()
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