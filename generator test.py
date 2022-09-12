def isPrime(x):
    if x < 2:
        pass
    elif x==2:
        print(x)
    for n in range(2,x):
        if x % n==0:
            pass
        elif x % n != 0:
            print(x)
    print(x)

def primeGenerator (a,b):
    for nums in range(a,b):
        yield isPrime(nums)



f=int(input())
t=int(input())
print(list(primeGenerator(f,t)))