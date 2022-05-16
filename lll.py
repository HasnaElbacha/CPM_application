test_list = [[1,2], [4,5], [1,2], [4,5], [1,2]]
print ("The original list is : " +  str(test_list))
  
# using naive method
# to remove duplicated 
# from list 
res = []
for i in test_list:
    if i not in res:
        res.append(i)
  
# printing list after removal 
print ("The list after removing duplicates : " + str(res))