def gcd(m,n):
    if (m>n) and (m%n==0):
        return (n)
    else: 
        r=m%n #remainder
        return(gcd(n,r))

m=int(input('Enter m =>'))
n=int(input('Enter m =>'))
print(f'The greatest common divisor of {m} and {n} is {gcd(m,n)}')