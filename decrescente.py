x=0
a, b, c= map(int, raw_input().split(" "))
if (a>b):
    x=b
    b=a
    a=x
elif (b>c):
    x=c
    c=b
    b=x
elif (a>c):
    x=c
    c=a
    a=x
print (c)
print (b)
print (a)
