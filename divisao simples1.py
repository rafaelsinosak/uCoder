a, b = map(float, raw_input().split(" "))
if ((0 <= a) and (a <= 1000) and(0 <= b) and (b <= 1000)):
    print "{:0.2f}".format(a/b)
