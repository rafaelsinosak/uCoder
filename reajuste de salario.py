salario = float(input())
reajuste=0
porcent=0
aumento=0
novosal=0
print ("{0:.2f}".format(salario))
if (salario<280.99):
    porcent=20
elif (salario>=281 and salario<=700.99):
    porcent=15
elif (salario>=701 and salario<=1500.99):
    porcent=10
elif (salario>=1501):
    porcent=5
print str(porcent)+"%"
aumento=(salario*porcent)/100
print ("{0:.2f}".format(aumento))
novosal=salario+aumento
print ("{0:.2f}".format(novosal))
