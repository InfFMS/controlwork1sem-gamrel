m=0
while m<5:
    n=int(input())
    i=2
    k=0
    while k<5:
        if n%i==0:
            k+=1
            l=n/i
        i+=1
        if i>n/2:
            k=+10
            l=0
    print(n)
    print(l)
    k=0
    i=2
    m=+1