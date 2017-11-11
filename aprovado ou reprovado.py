a, b = map(int, raw_input().split(" "))
media=(a+b)/2
if (media==10):
    print "APROVADO COM DISTINCAO"
else:
    if (media>=6):
        print "APROVADO"
    else:
        print "REPROVADO"
