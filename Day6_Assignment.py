#Assignment6
list1=[1,2,3,4,5,7,8]
list2=["a","b","c","d","e"]

list=[(k,v) for k in list1 for v in list2 if list1.index(k)==list2.index(v)]
print("Required dictonary of above two list is\n",dict(list))



"""
Output
Required dictonary of above two list is
{1:"a",2:"b",3:"c",4:"d",5:"e"}

"""
