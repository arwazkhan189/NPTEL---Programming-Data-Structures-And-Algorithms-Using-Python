def gcd(m,n):
    i=min(m,n)
    while (i>0):
        if (m%i==0) and (n%i==0):
            return(i)
        else:
            i-=1
m=int(input('Enter m =>'))
n=int(input('Enter m =>'))
print(f'The greatest common divisor of {m} and {n} is {gcd(m,n)}')