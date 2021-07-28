a= int(input("enter a number:"))
n1=0
n2=1
sum=0
if a<=0:
    print( "please enter value more than 0")
else:
    for b in range(0, a):
        print(sum, end=" ")
        n1=n2
        n2= sum
        sum= n1+ n2
    
