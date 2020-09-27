def Repeat(x):
    s = len(x)
    repeat = []
    for i in range(s):
        k = i + 1
        for j in range(k, s):
            if x[i] == x[j] and x[i] not in repeat:
                repeat.append(x[i])
    return repeat
l= [1,2,3,4,4,5,5,6]
a=list(set(l))
print (a)
