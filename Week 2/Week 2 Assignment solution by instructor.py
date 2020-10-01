def factors(n):
    factorlist = []
    for i in range(1,n+1):
        if n%i == 0:
            factorlist.append(i)
    return(factorlist)

def isprime(n):
    return(factors(n) == [1,n])

def primeproduct(n):
    for i in range(1,n+1):
        if n%i == 0:
            if isprime(i) and isprime(n//i):
                return(True)
    return(False)

def delchar(s,c):
    if len(c) != 1:
        return(s)
    snew = ""
    for char in s:
        if char != c:
            snew = snew + char
    return(snew)

def shuffle(l1,l2):
    if len(l1) < len(l2):
        minlength = len(l1)
    else:
        minlength = len(l2)
    shuffled = []
    for i in range(minlength):
        shuffled.append(l1[i])
        shuffled.append(l2[i])
    shuffled = shuffled + l1[minlength:] + l2[minlength:]
    return(shuffled)

import ast

def tolist(inp):
  inp = "["+inp+"]"
  inp = ast.literal_eval(inp)
  return (inp[0],inp[1])

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "primeproduct":
   arg = parse(farg)
   print(primeproduct(arg))
elif fname == "delchar":
   (s1,s2) = parse(farg)
   print(delchar(s1,s2))
elif fname == "shuffle":
   (l1,l2) = parse(farg)
   print(shuffle(l1,l2))
else:
   print("Function", fname, "unknown")

