import argparse
import sys
import os
"""from pathlib import Path"""

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
print(args)
print(sys.argv)

print(sys.argv[2])

"""argument check if sys.argv[1] """


""" get the files list """
path = str(sys.argv[2])

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.cpp' in file:
            files.append(os.path.join(r, file))
        elif '.h' in file:
            files.append(os.path.join(r, file))
        elif '.pro' in file:
            files.append(os.path.join(r, file))
        elif '.pri' in file:
            files.append(os.path.join(r, file))
for f in files:
    print(f)
    
check = input('These files will be altered, are you sure you want to proceed? Y/N: ')
if check == 'n' or check == 'N':
    print('The script will be exited. You can restart the procedure with the correct path')
else:
    '''do the processing'''
    
    
