def primeproduct(m):
    product=1
    for i in range(2,(m//2)+1):
        if(m%i==0 and m>=0):
            product*=i
    if(product==m):
        return(True)
    else:
        return(False)
def delchar(s,c):
    if (len(c)!=1):
        return(s)
    else:
        n=''
        for i in s:
            if (i!=c):
                n+=i
        return(n)
def shuffle(l1,l2):
    l3=[]
    if len(l1)==len(l2):
        for i in range(len(l1)):
            l3.append(l1[i])
            l3.append(l2[i])
    else:
        if len(l1)<len(l2):
            l3=shuffle(l1,l2[0:len(l1)])
            l3.extend(l2[len(l1):])
        else:
            l3=shuffle(l1[:len(l2)],l2)
            l3.extend(l1[len(l2):])
    return(l3)
