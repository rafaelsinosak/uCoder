frase = raw_input()
final=""
for x in range(len(frase)):
    if frase[x]=="p" and frase[x+1]=="p" and frase[x-1]=="p":
        final=final+"p"

    if frase[x]!="p":
        final=final+frase[x]
print final
