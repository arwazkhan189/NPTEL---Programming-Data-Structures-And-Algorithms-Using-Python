def quicksort(a,l,r):
    if r-l<=1:
        return()
    y=l+1
    for g in range(l+1,r):
        if a[g]<a[l]:
            a[y],a[g]=a[g],a[y]
            y+=1
    a[l],a[y-1]=a[y-1],a[l]
    quicksort(a,l,y-1)
    quicksort(a,y,r)
    return(a)
                
