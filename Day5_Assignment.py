#Que1

def fun(x):
 for i in range(len(x)-x.count(0)):
      if x[i]==0:
         del x[i]
 return(x)             
       
list=[0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
n_zero=list.count(0)
fun(list)
print(list)
list.sort()
print(list)
for i in range(n_zero):
    list.append(0)
print("Required sorted list with zeros at RHS is", list)

"""Output

[1,2,10,4,1,56,2,1,3,56,4]
[1,1,1,2,2,3,4,4,10,56,56]
Required sorted list with zeros at RHS is 
[1,1,1,2,2,3,4,4,10,56,56,0,0,0,0,0]

"""

#Que 2
list1=[10,20,40,60,70,80]
list2=[5,15,25,35,45,55]
list=list1+list2
print("Merged list before sorting is ",list)
i=0
while(i<len(list)):
    j=i+1
    while(j<len(list)):
       if (list[j]<list[i]):
           t=list[i]
           list[i]=list[j]
           list[j]=t
       j=j+1
    i=i+1
print("Merged List after sorting is ",list)
    
"""   Output
Merged list before sorting is
[10,20,40,60,70,80,5,15,25,35,45,55]
Merged List after sorting is
[5,10,15,20,25,35,40,45,55,60,70,80]
"""
