
# import time
# import sqlite3
# import subprocess
# def script():
#     def convert(start_time): 
#        start_time = start_time % (24 * 3600) 
#        hour = start_time // 3600
#        start_time %= 3600
#        minutes = start_time // 60
#        start_time %= 60
#        return "%d:%02d" % (hour, minutes) 
#     def executeSomething(): 
#        file_ = open("donnee.txt", "a") 
#        x=subprocess.Popen("netstat ", stdout=file_) 
#        print ("code retour:",x.wait())
#        print ("sortie standard")
#        file_.close()
#        with open('donnee.txt',encoding="unicode_escape") as f:
#          for line in f:
#             print(line.split())
            
#        time.sleep(10)
#        time.sleep(10)     
#     while True:
#         start_time=time.time()
#         timenow=convert(start_time)
#         print(timenow)
#         if timenow=="22:59":
#            print(timenow)
#            conn = sqlite3.connect('.\\db\\connec.db')
#            cursor = conn.cursor()
#            cursor.execute('DELETE FROM connection ')
#            conn.commit()
#            print("done")
#            f = open('donnee.txt', 'r+')
#            f.truncate(0)
#         else:  
#            print(timenow)
#            executeSomething()       
#         time.sleep(10)
# # script()
# # f = open('donnee.txt', 'r+')
# # f.truncate(0)
#µµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµ
# import time
# import sqlite3
# import subprocess
# def script():
#     def convert(start_time): 
#        start_time = start_time % (24 * 3600) 
#        hour = start_time // 3600
#        start_time %= 3600
#        minutes = start_time // 60
#        start_time %= 60
#        return "%d:%02d" % (hour, minutes) 
#     def executeSomething(): 
#        file_ = open("donnee.txt", "a") 
#        x=subprocess.Popen("netstat ", stdout=file_) 
#        print ("code retour:",x.wait())
#        print ("sortie standard")
#        file_.close()
#        with open('donnee.txt',encoding="unicode_escape") as f:
#          for line in f:
#             print(line.split())
#             file=open("file.txt", "a")
#             file.write(line.split())
#             file.close()
#        time.sleep(10)
#        time.sleep(10)     
#     while True:
#         start_time=time.time()
#         timenow=convert(start_time)
#         print(timenow)
#         if timenow=="22:59":
#            print(timenow)
#            conn = sqlite3.connect('.\\db\\connec.db')
#            cursor = conn.cursor()
#            cursor.execute('DELETE FROM connection ')
#            conn.commit()
#            print("done")
#            f = open('donnee.txt', 'r+')
#            f.truncate(0)
#         else:  
#            print(timenow)
#            executeSomething()       
#         time.sleep(10)
# script()
# f = open('donnee.txt', 'r+')
# f.truncate(0)