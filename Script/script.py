import argparse
import sys
import os
import csv
import re

R=re.compile("\D+(\d\d\d\d)-(\d\d\d\d)\D+")
def processFile( filepath ):
    content = ''
    Check = False
    with open(filepath) as f:
        content = f.read()
        for date in R.finditer(content):
            if date:
                if date.group(2)<"2019":
                    print(filepath)
                    content = content.replace(date.group(2),"2019")
                    Check = True
    f.close()
    if Check == False:
        content = ''
    return content

def update(filepath, content):
    if content != '':
        with open(filepath,'w') as f:
            f.write(content)
        f.close()
        
parser = argparse.ArgumentParser(description='Update Copyright for GAMS files.')
parser.add_argument('-p', help='folder path for the repository')
"""parser.add_argument('-y', help='Current year') will be implemented later either with a date module or manually"""
parser.add_argument('--dry_run', help='show the user the files to be altered')

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


path = str(sys.argv[len(sys.argv)-1])

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
    processFile(f)
    if len(sys.argv)<4:
        update(f,processFile(f))
if len(sys.argv)>3:
    print('You are in a dry run mode. These are the files to be changed after executing the script.')