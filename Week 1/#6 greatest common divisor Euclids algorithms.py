def gcd(m,n):
    #Assume m>=n
    if m<n:
        m,n=n,m
    if (m%n)==0:
        return (n)
    else:
        diff=m-n
        #diff > n ? possible!
        return (gcd(max(n,diff),min(n,diff)))
m=int(input('Enter m =>'))
n=int(input('Enter m =>'))
print(f'The greatest common divisor of {m} and {n} is {gcd(m,n)}')