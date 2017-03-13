R = 10000
x = []
inside = []
for i in range(R):
    point = [rand(), rand()]
    x.append(point)
    test = in_circle(point, (0, 0))
    if test:
	inside.append(1)
    else:
	inside.append(0)

sum_inside = sum(inside)
print(sum_inside / R)
