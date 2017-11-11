num=input()
text=str(bin(num))
textfinal=""
for x in range ((len(text))):
    if (x>1):
        if ("1" == text[x]):
            textfinal=textfinal+"0"
        else:
            textfinal=textfinal+"1"
print int (textfinal,2)
        
