letra = raw_input()
frase = raw_input()
a = frase.split(" ")
cont=0.0
for x in range (len(a)):
    if letra in a[x]:
        cont=cont+1
porcent=(100*cont)/len(a)
print "{:0.1f}".format(porcent)
