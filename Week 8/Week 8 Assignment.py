import sys
input = sys.stdin.readline
first = list(map(int,input().split(" ")))
k = first[2]
d = first[3]
index = [[0,0]]
for i in range(d):
    List_row = list(map(int,input().split(" ")))
    index.append(List_row)
    sorted_index = sorted(index,key= lambda x: (x[0],x[1]))
    DISCT_STORE_find_Distance = dict()
    DISCT_STORE_LIST_MIDDLE = dict()

def find_Distance(j1,j2):
    global DISCT_STORE_find_Distance
    X_move = abs((sorted_index[j1][0])-(sorted_index[j2][0]))
    Y_move = abs((sorted_index[j1][1])-(sorted_index[j2][1]))
    steps = X_move + Y_move
    DISCT_STORE_find_Distance[(f"{j1},{j2}")] = steps
    return DISCT_STORE_find_Distance[(f"{j1},{j2}")]

def LIST_MIDDLE(i,j):
    global DISCT_STORE_find_Distance
    global DISCT_STORE_LIST_MIDDLE
    if i == 1:
        return find_Distance(0,j)
    else:
        find_DistanceList = []
    for x in range(i-1,j):
        if (f"{i-1},{x}") in DISCT_STORE_LIST_MIDDLE:
            if (f"{x},{j}") in DISCT_STORE_find_Distance:
                find_DistanceList.append(DISCT_STORE_LIST_MIDDLE[f"{i-1},{x}"]+DISCT_STORE_find_Distance[f"{x},{j}"])
            else:
                find_DistanceList.append(DISCT_STORE_LIST_MIDDLE[f"{i-1},{x}"]+find_Distance(x,j))

        else:
            DISCT_STORE_LIST_MIDDLE[f"{i-1},{x}"] = LIST_MIDDLE(i-1,x)
            if (f"{x},{j}") in DISCT_STORE_find_Distance:
                find_DistanceList.append(DISCT_STORE_LIST_MIDDLE[f"{i-1},{x}"]+DISCT_STORE_find_Distance[f"{x},{j}"])
            else:
                find_DistanceList.append(DISCT_STORE_LIST_MIDDLE[f"{i-1},{x}"]+find_Distance(x,j))

    return min(find_DistanceList)

ANSWER = []
for g in range((len(sorted_index)-1),k-1,-1):
    ANSWER.append(LIST_MIDDLE(k,g))

print(min(ANSWER))