def contracting(l):
    if len(l) < 3:
        return(True)
    return((abs(l[1]-l[0]) > abs(l[2]-l[1])) and contracting(l[1:]))

###################

def contracting_iterative(l):
    if len(l) < 3:
        return(True)
    for i in range(len(l)-2):
        diff = abs(l[i+1]-l[i])
        if diff <= abs(l[i+2]-l[i+1]):
            return(False)
    return(True)

###################

def counthv(l):
    hills = 0
    valleys = 0
    for i in range(1,len(l)-1):
        if l[i] > l[i-1] and l[i] > l[i+1]:
            hills = hills + 1
        if l[i] < l[i-1] and l[i] < l[i+1]:
            valleys = valleys + 1
    return([hills,valleys])

###################

def leftrotate(m):
    size = len(m)
    rotated_m = []
    for i in range(size):
        rotated_m.append([])
    for c in range(size-1,-1,-1):
        for r in range(size):
            rotated_m[size-(c+1)].append(m[r][c])
    return(rotated_m)

###################

import ast

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "contracting":
  arg = parse(farg)
  print(contracting(arg))

if fname == "counthv":
  arg = parse(farg)
  print(counthv(arg))

if fname == "leftrotate":
  arg = parse(farg)
  savearg = arg
  ans = leftrotate(arg)
  if savearg == arg:
    print(ans)
  else:
    print("Side effect")
