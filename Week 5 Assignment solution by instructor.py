# Convert letter grade to grade point
def gradetonum(grade):
    if grade == 'A':
        return(10)
    elif grade == 'AB':
        return(9)
    elif grade == 'B':
        return(8)
    elif grade == 'BC':
        return(7)
    elif grade == 'C':
        return(6)
    elif grade == 'CD':
        return(5)
    elif grade == 'D':
        return(4)
    else:
        return(0)
                   
# Set up three dictionaries to store data
rollname = {}    # Key: roll number, Value: Name
gradepoint = {}  # Key: roll number, Value: Cumulative grade points
coursecount = {} # Key: roll number, Value: Number of courses taken

nextline = input().strip()
while nextline.find("Courses") < 0:
    nextline = input().strip()

# Read course data
while nextline.find("Students") < 0:
    nextline = input().strip()
    # Course data is irrelevant for this problem!

# Read students data
nextline = input().strip()
while nextline.find("Grades") < 0:
    fields = nextline.split('~')
    roll=fields[0]
    name=fields[1]
    rollname[roll] = name   # Initialize
    gradepoint[roll] = 0    # Initialize
    coursecount[roll] = 0   # Initialize
    nextline = input().strip()

# Read grades data
nextline = input().strip()
while nextline.find("EndOfInput") < 0:
    fields = nextline.split('~')
    roll=fields[3]
    grade=fields[4]
    gradepoint[roll] += gradetonum(grade)  # Update
    coursecount[roll] += 1                 # Update
    nextline = input().strip()

# Print output
for roll in sorted(rollname.keys()):
    if coursecount[roll] > 0:
        gpa = round(gradepoint[roll]/coursecount[roll],2)
    else:
        gpa = 0
    print(roll,rollname[roll],gpa,sep='~',end='\n' )