import subprocess

import subprocess
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)



##### Popen
def TestPopen():
  import subprocess
  subprocess.Popen("ls",shell=True)
#   for i in range(5) :
#     print ("no wait and continue do other things")
TestPopen()


##### Popen and wait
def TestWait():
  import subprocess
  import datetime
  print (datetime.datetime.now())
  p=subprocess.Popen("sleep 10",shell=True)
  p.wait()
  print (p.returncode)
  print (datetime.datetime.now())

TestWait()
 
