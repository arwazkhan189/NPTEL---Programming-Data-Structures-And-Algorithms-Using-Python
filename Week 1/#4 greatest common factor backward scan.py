def gcd(m,n):
    for i in range(min(m,n),0,-1):
        if (m%i)==0 and (n%i)==0 :
            mrcf=i
            break
    return(mrcf)
m=int(input('Enter m =>'))
n=int(input('Enter m =>'))
print(f'The greatest common divisor of {m} and {n} is {gcd(m,n)}')