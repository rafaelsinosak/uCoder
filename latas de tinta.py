tamanho = input()
litros=tamanho/3
if (tamanho%50==0):
	latas = tamanho/54
else: 
	latas = int(tamanho/54)+1
preco=latas*80
print latas, ("{0:.0f}".format(preco))
