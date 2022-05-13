import subprocess

proc = subprocess.Popen(["lsof -i"], stdout=subprocess.PIPE, shell=True)
out, err = proc.communicate()
print ("network connections output:")
print (out)