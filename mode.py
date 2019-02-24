data=[1,3,4,5,5,5,5,3,3,3,9,8,0,4,33]
lst =[]
hgh=0
for i in range(len(data)):
    lst.append(data.count(data[i]))
m= max(lst)
ml = [x for x in data if data.count(x)==m ] #to find most frequent values
print(ml)
mode = []
for x in ml: #to remove duplicates of mode
        if x not in mode:
            mode.append(x)


def mode(data):               #using function to solve for mode
    lst =[]
    hgh=0
    for i in range(len(data)):
        lst.append(data.count(data[i]))
    m= max(lst)
    ml = [x for x in data if data.count(x)==m ] #to find most frequent values
    print(ml)
    mode = []
    for x in ml: #to remove duplicates of mode
        if x not in mode:
            mode.append(x)
    return mode
#print (mode([1,2,2,2,7,7,7,5,5,5]))
