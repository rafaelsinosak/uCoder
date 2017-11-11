numvezes= input()
cont=0
while (cont<numvezes):
    produtos= input()
    cont2=0
    preco=0
    qnt=0
    valor=0
    while (cont2<produtos):
        quant, valor = map(int, raw_input().split(" "))
        preco=preco+quant*valor
        cont2=cont2+1
    dinheiro= int(input())
    if (dinheiro<preco):
        print ("DINHEIRO INSUFICIENTE")
    else:
        print dinheiro-preco
    cont=cont+1
