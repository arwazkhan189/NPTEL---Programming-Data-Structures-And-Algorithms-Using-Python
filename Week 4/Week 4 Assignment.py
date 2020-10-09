def frequency(l):
    d={}
    for i in l:
        if i not in d.keys():
            d[i]=1
        else:
            d[i]+=1
    keys_list=list(d.keys())
    values_list=list(d.values())
    minfreqlist=[keys_list[i] for i in range(len(values_list)) if values_list[i]==min(values_list)]
    maxfreqlist=[keys_list[i] for i in range(len(values_list)) if values_list[i]==max(values_list)]
    return(sorted(minfreqlist),sorted(maxfreqlist))
def onehop(l):
    res = []
    for i in l:            
        x1, y1 = i          
        for j in l:   
            if i != j:  
                x2, y2 = j
                if y1 == x2 and x1 != y2 and (x1,y2) not in res:
                    res.append((x1,y2))
    res.sort()
    return res
