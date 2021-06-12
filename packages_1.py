'''import sys
import subprocess
import pkg_resources
import pdb
import os
required = {'cantools','selenium','fib'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed
if missing:
   python_1 = sys.executable
   subprocess.check_call([python_1, 'python', '-m' ,'pip', 'install', *missing])'''

'''package = 'PIL'
try:
 return __import__(package)
except ImportError:
    return None'''

'''import pip

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package]) 

list1 = ['selenium','cantools']
for i in list1:
    ad =  import_or_install(i)'''


'''import os
list1 = ['cantools','selenium']
for i in list1:
    package = i
    try:
       __import__package
    except:
       os.system("pip install "+ package)'''


'''import sys
import subprocess
import pkg_resources

required = {'mutagen', 'gTTS'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)'''




import subprocess
import time
def install(name):
    subprocess.call(['pip', 'install', name])

list1 = ['cantools','selenium','fib']
for i in list1:
    ad = install(i)

'''import subprocess
import sys

try:
    import pandas as pd
except ImportError:
    subprocess.call([sys.executable, "-m", "pip", "install", 'cantools'])'''

'''import subprocess

def install(name):
    subprocess.call(['pip', 'install', name])


ad = install('cantools')'''





