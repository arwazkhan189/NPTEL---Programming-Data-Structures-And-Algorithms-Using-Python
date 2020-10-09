def merge(a,b):
    (c,m,n)=([],len(a),len(b))
    (i,j)=(0,0)
    while i+j<m+n:
        if i==m:
            c.append(b[j])
            j+=1
        elif j==n:
            c.append(a[i])
            i+=1
        elif a[i]<=b[j]:
            c.append(a[i])
            i+=1
        elif a[i]>b[j]:
            c.append(b[j])
            j+=1
    return(c)
def mergesort(a,l,r):
    if r-l<=1:
        return(a[l:r])
    if r-l>1:
        m=(l+r)//2
        L=mergesort(a,l,m)
        R=mergesort(a,m,r)
        return(merge(L,R))
