y = [ i for i in range(1, 11)]
Y = []
for i in range(10):
    Y.append(y)
    
ranges = []
for i in range(len(Y)):
    x2 = Y[2]
    y = Y[i]
    diff = []
    for j in range(len(x2)):
        diff.append(abs(y[j] - x2[j]))
    ranges.append(diff)
print(ranges)
