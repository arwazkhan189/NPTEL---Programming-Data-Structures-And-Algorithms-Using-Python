def contracting(l):
  diff=abs(l[0]-l[1])
  for i in range(1,len(l)-1):
    new_diff=abs(l[i]-l[i+1])
    if new_diff<diff:
        diff=new_diff
    else:
      return False
  return True
def counthv(l):
    hc=0
    vc=0
    for i in range(1,len(l)-1):
        if l[i]>l[i+1] and l[i]>l[i-1]:
            hc+=1
        elif l[i]<l[i+1] and l[i]<l[i-1]:
            vc+=1
    return ([hc,vc])
def leftrotate(m):
    n=len(m)
    #operation C1 <-> C3
    for j in range(n // 2):
        for i in range(n):
            m[i][j], m[i][n - 1 - j] = m[i][n - 1 - j], m[i][j]
    #transposing the matrix
    for i in range(n):
        for j in range(i):
            m[i][j], m[j][i] = m[j][i], m[i][j]
    return m
