def gcd(m,n):

    for i in range(1,min(m,n)+1):
        if (m%i)==0 and (n%i)==0 :
            mrcf=i #most recent common factor
    return(mrcf)
m=int(input('Enter m =>'))
n=int(input('Enter m =>'))
print(f'The greatest common divisor of {m} and {n} is {gcd(m,n)}')