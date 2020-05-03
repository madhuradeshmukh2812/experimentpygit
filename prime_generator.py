def prime(m,n):
    for i in range(m,n+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=" ")
t=int(input("enter the no. of test cases:"))
i=0
while i<t:
    m,n=[int(x)for x in input("").split(" ")]
    prime(m,n)
    i=i+1
    print(" ")
