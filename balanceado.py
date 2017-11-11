num=input()
parenteses={"(": ")","[": "]","{": "}"}
def checar(txt):
    pilha=[]
    for x in txt:
        tem = parenteses.get(x)
        if tem:
            pilha.append(tem)
        elif not pilha or (pilha.pop()!=x):
            return False
    return not pilha

for x in range (num):
    txt=raw_input()
    if (checar(txt)==True):
        print ("YES")
    else:
        print ("NO")
