def fatorial(num):
    if num==0:
        return 0
    if num==1:
        return 1
    if num>1:
        return fatorial(num-1)*num
num = input()
print fatorial(num)
