# from distutils import text_file
from datetime import date
import subprocess 
import time
import sqlite3
import csv
def script():
  def convert(start_time): 
    start_time = start_time % (24 * 3600) 
    hour = start_time // 3600
    start_time %= 3600
    minutes = start_time // 60
    start_time %= 60
    return "%d:%02d:%d" % (hour, minutes,start_time) 
  def executeSomething(): 
   time.sleep(30)
   file_ = open("donnee.txt", "a") 
   x=subprocess.Popen("netstat -a ", stdout=file_) 
   print ("code retour:",x.wait())
   print ("sortie standard")
   file_.close()
   with open('donnee.txt',encoding="unicode_escape") as f:
         for line in f:
            start_time=time.time()
            timenow=convert(start_time)
            today = date.today()
            if '20.199.120.85:https' in line.split() :
               adresse='20.199.120.85:https'
               info=adresse[0:13]+';'+str(today)+';'+timenow+"\n"
               if info not in f:
                  file = open("file.txt", "a")
                  file.write(adresse[0:13]+';'+str(today)+';'+timenow+"\n")
                  file.close()
                  txt_file=r"file.txt"
                  csv_file=r"script.csv"
                  in_txt=csv.reader(open(txt_file,"r"),delimiter=";")
                  outt_csv=csv.writer(open(csv_file,"w"))
                  outt_csv.writerows(in_txt)
                  del outt_csv

  while True:
   start_time=time.time()
   timenow=convert(start_time)
   if timenow=="0:00":
      print(timenow)
      f = open('donnee.txt', 'r+')
      f.truncate(0)
      c = open('file.txt', 'r+')
      c.truncate(0)
      v = open('script.csv', 'r+')
      v.truncate(0)
      conn = sqlite3.connect('.\\db\\connec.db')
      cursor = conn.cursor()
      cursor.execute('DELETE FROM connection ')
      conn.commit()
      # time.sleep(20)
   else:  
      print(timenow)
      executeSomething()
      
# script()    
