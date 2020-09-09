def gcd(m,n):
    #Assume m>=n
    if m<n:
        m,n=n,m
        while (m%n) !=0:
            diff=m-n
            #diff > n ? possible!
            m,n=(max(n,diff),min(n,diff))
        return (n)
m=int(input('Enter m =>'))
n=int(input('Enter m =>'))
print(f'The greatest common divisor of {m} and {n} is {gcd(m,n)}')