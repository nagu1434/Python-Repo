def happy(n,i):
    while i<8:
        re=0
        while n>0:
            re+=(n%10)**2
            n=n//10
        i+=1    
        if(re==1):
            return 1
        else:
            return happy(re,i)
    return 0         
n=int(input())
re=happy(n,0)
if re==1:
    print("True")
else:
    print("False")