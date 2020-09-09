def gcd(m,n):
    if m<n:
        m,n=n,m
    while (m%n)!=0:
        m,n=n,m%n   #remainder m%n < n always 
    return (n)
m=int(input('Enter m =>'))
n=int(input('Enter m =>'))
print(f'The greatest common divisor of {m} and {n} is {gcd(m,n)}')