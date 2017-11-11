altura, s = map(float, raw_input().split(" "))
if (s==2):
    print ("{0:.2f}".format((72.7*altura) - 58))
else:
    print ("{0:.2f}".format((62.1*altura) - 44.7))
