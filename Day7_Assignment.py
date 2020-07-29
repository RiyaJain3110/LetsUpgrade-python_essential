#Que1:
#Using list comprehension
port1={21:"FTP",22:"SSH",23:"telnet",80:"http"}
print("Old dictionary is:")
print(port1)
port2= dict((v,k) for k,v in port1.items())
print("New dictionary is:")
print(port2)

'''
#Output1:
Old dictionary is:
{21: 'FTP', 22: 'SSH', 23: 'telnet', 80: 'http'}
New dictionary is:
{'FTP': 21, 'SSH': 22, 'telnet': 23, 'http': 80}
'''

#Que2:
#Using list comprehension
list1 = [(1, 2), (3, 4), (5, 6)]
print([sum(tup) for tup in list1])

'''
#Output2:
[3, 7, 11]

'''

#Que3:
list2 = [(1,2,3), [1,2], ['a','hit','less']] 
# Using list comprehension 

out = [item for t in list2 for item in t]
print(out) 

'''
Output3:
	[1, 2, 3, 1, 2, 'a', 'hit', 'less']

'''

