import subprocess 
import time,csv
def convert(start_time): 
    start_time = start_time % (24 * 3600) 
    hour = start_time // 3600
    start_time %= 3600
    minutes = start_time // 60
    start_time %= 60
    return "%d:%02d" % (hour, minutes) 
def executeSomething(): 
   file_ = open("donnee.txt", "a") 
   x=subprocess.Popen("netstat -a", stdout=file_) 
   print ("code retour:",x.wait())
   print ("sortie standard")
   print (x.stdout.read())
   file_.close()
   time.sleep(10) 
while True:
   start_time=time.time()
   timenow=convert(start_time)
   if timenow=="0:00":
      print(timenow)
      f = open('donnee.txt', 'r+')
      f.truncate(0)
   else:  
      print(timenow)
      executeSomething()
    
# f = open('donnee.txt', 'r+')
# f.truncate(0)