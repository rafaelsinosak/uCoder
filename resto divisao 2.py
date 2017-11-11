a, b = map(int, raw_input().split(" "))
if ((0 <= a) and (a <= 1010) and(0 <= b) and (b <= 1010)):
    if (a%b > b%a):
       print a
    else:
        print b
    
