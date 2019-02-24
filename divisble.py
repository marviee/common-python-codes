'''for i in range(0,111):
    if i%7==0 and i%3 != 0 and i %5 !=0:
        print(str(i))
        '''

alist = []

def det(m):
    if len(m) > 2:
        for i in range(len(m)):
            new_m = deepcopy(m)
            minor(new_m,i)
            multiplier = m[i][0] * math.pow(-1,i)
            recursive = det(new_m)
            alist.append(multiplier * recursive)
    else:
        return (m[0][0]*m[1][1] - m[0][1]*m[1][0])

def minor(matrix,row):
    length = len(matrix)
    for i in range(length):
        matrix[i].pop(0)
    matrix.pop(row)
    return matrix
for i  in range (20):
    print (i)

det(3)
