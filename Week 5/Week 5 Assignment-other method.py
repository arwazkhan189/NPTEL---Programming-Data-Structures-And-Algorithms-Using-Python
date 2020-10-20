import operator

input('')

class Stu:
    def __init__(self, name, fname):
        self.name = name
        self.fname = fname
        self.num = 0
        self.total = 0

    def add(self, gr):
        self.num +=1
        if gr=="A":
            self.total +=10
        elif gr=="AB":
            self.total+=9
        elif gr=="B":
            self.total+=8
        elif gr=="BC":
            self.total+=7
        elif gr=="C":
            self.total+=6
        elif gr=="CD":
            self.total+=5
        elif gr=="D":
            self.total+=4

class Marks:
    def __init__(self, sub, scode, grade):
        self.sub = sub
        self.scode = scode
        self.grade = grade

ss=[]
mm=[]

flag = True

z= input('')
while True:
    z= input('')
    xxx = z.split('~')
    if len(xxx)==1 or len(xxx)==0:
        break
    if len(z)==0:
        break

z= input('')
while True:
    xxx = z.split('~')
    if len(xxx)==1 or len(xxx)==0:
        break
    a,b = xxx
    x= Stu(a,b)
    ss.append(x)
    z= input('')
    if len(z)==0:
        break

z= input('')

while True:
    xxx = z.split('~')
    if len(xxx)==1:
        break
    a,b,c,d,e = xxx
    x= Marks(a,d,e)
    mm.append(x)
    z= input('')
    if len(z)==0:
        break

def ser(ss,tos):
    for s in ss:
        if s.name==tos:
            return s

for m in mm:
    ser(ss,m.scode).add(m.grade)

ss.sort(key=operator.attrgetter('name'))

for s in ss:
    if s.num == 0:
        fff=0
        print(s.name + "~"+s.fname +"~"+str(fff))
    else:
        fff =float(s.total) /float(s.num)
        print(s.name + "~"+ s.fname+ "~" + str(round(fff,2)))