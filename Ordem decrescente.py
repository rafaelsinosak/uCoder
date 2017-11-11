a,b,c = map(int, raw_input().split(" "))
x=[]
x.append(a)
x.append(b)
x.append(c)
x.sort()
x.reverse()
for y in range(3):
    print x[y]
