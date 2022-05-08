import csv
def test():
   file_ = open("data.txt", "a") 
   file_.write("hiiii hasna cv\n")
#    with open("data.txt", "r") as f:
#        f_contents=f.read()
#        print(f_contents)
   with open('data.txt') as inf:
       reader = csv.reader(inf, delimiter=" ")
       second_col = list(zip(*reader))[0]
       print(second_col)
   file_.close()
a=0
while a<20:
    test()
    a=a+1