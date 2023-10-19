N=int(input("enter a number"))
Tab=[]
i=1
S=0
while i<=N:
    D= N// i
    if N % i==0 :
        Tab.append(D)
        S=S+1
    i=i+1
print("the number of divisors is:" ,   S)
print("divisors are :" ,  Tab)
