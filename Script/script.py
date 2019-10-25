import argparse
import sys
import os
import csv
import re
import datetime

R=re.compile("\D+(\d\d\d\d)-(\d\d\d\d)\D+")
now = datetime.datetime.now()
currentYear = now.year
licenseText= ""

if '-l' in sys.argv:
    with open(sys.argv[sys.argv.index('-l')+1]) as f:
        licenseText = f.read()
        if not licenseText:
            print("The license template is empty. Please add an up to date license Template")
    f.close()

def licenseExistanceCheck(string,extension):
    if string == "":
        return False
    lines= string.splitlines()
    if extension:
        return ("#" in lines[0])
    else:
        return ("/*" in lines[0])

def processFile( filepath ):
    content = ''
    Check = False
    with open(filepath) as f:
        content = f.read()
    f.close()
    if filepath.endswith('.pri') or filepath.endswith('.pro'):
        extension=True
    else:
        extension=False
    if licenseExistanceCheck(content,extension):
        for date in R.finditer(content):
            if date:
                if date.group(2)<str(currentYear):
                    print(filepath)
                    content = content.replace(date.group(2),"2019")
                    Check = True
    else:
        if extension:
            print("the file ", filepath, "will receive the up to date license Template")
            lines = licenseText.splitlines()
            modified = "#\n"
            for x in range(1,len(lines)-2):
                l = lines[x]
                if l =="":
                    l = "#\n"+l
                else:
                    l = "# " + l + "\n"
                modified = modified + l
            modified = modified + " *#\n#\n"
            content = modified + content
            Check = True
        else:
            print("the file ", filepath, "will receive the up to date license Template")
            lines = licenseText.splitlines()
            modified = "/*\n"
            for x in range(1,len(lines)-2):
                l = lines[x]
                if l =="":
                    l = " *\n"+l
                else:
                    l = " * " + l + "\n"
                modified = modified + l
            modified = modified + " */\n"
            content = modified + content
            Check = True
    if Check == False:
        content = ''
    return content

def update(filepath, content):
    if content != '':
        with open(filepath,'w') as f:
            f.write(content)
        f.close()
        
parser = argparse.ArgumentParser(description='Update Copyright for GAMS files.')
parser.add_argument('--dry_run', help='show the user the files to be altered', action='store_true')
parser.add_argument('-p', help='folder path for the repository')
parser.add_argument('-e','--exclude', nargs='+', help='Folders to be ignored. You should add the folder in this form: folder1,folder2,folder3')
parser.add_argument('-l','--license', help='The license file directory')

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
pathindex = sys.argv.index('-p') +1 
path = str(sys.argv[pathindex])

dryrunmode = False
if '--dry_run' in sys.argv:
    print('You are in a dry run mode. These are the files to be changed after executing the script:')
    dryrunmode = True
exceptions = []
if '--exclude' in sys.argv:
    foldersIndex = sys.argv.index('--exclude')+1
    if len(sys.argv) == foldersIndex:
        print('you forgot to add exception folders')
        exit()
    exceptiontest = str(sys.argv[foldersIndex])
    if exceptiontest[0] == '-':
        print('you forgot to add exception folders')
        exit()
    exceptions = sys.argv[foldersIndex].split(",")
    
if '-e' in sys.argv:
    foldersIndex = sys.argv.index('-e')+1
    if len(sys.argv) == foldersIndex:
        print('you forgot to add exception folders')
        exit()
    exceptiontest = str(sys.argv[foldersIndex])
    if exceptiontest[0] == '-':
        print('you forgot to add exception folders')
        exit()
    exceptions = sys.argv[foldersIndex].split(",")    


files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for folder in sorted(d, reverse=True):
        if folder in exceptions:
            d.remove(folder)
            finish=False
    for file in f:
        if file.endswith('.pri'):
            files.append(os.path.join(r, file))
        elif file.endswith('.h'):
            files.append(os.path.join(r, file))
        elif file.endswith('.pro'):
            files.append(os.path.join(r, file))
        elif file.endswith('.cpp'):
            files.append(os.path.join(r, file))
        elif file.endswith('.rc'):
            files.append(os.path.join(r, file))
        elif file.endswith('.mm'):
            files.append(os.path.join(r, file))
for f in files:
    if dryrunmode == True:
        processFile(f)
    else:
        update(f,processFile(f))