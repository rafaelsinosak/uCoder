frase = raw_input()
palavra = frase.split(" ")
data=palavra[1].split("/")
mes=data[1]
if (data[1]in"02" or data[1] in "06" or data[1] in "08" or data[1] in "09" or data[1] in "11") and data[0]=="01":
    datafinal="31"
    mes=int(data[1])-1
elif (data[1] in "05" or data[1] in "07" or data[1] in "09" or data[1] in "12") and data[0]=="01":
    datafinal="30"
    mes=int(data[1])-1
elif data[1]=="03" and data[0]=="01":
    datafinal="28"
    mes="02"
else:
    datafinal = int(data[0])-1
data[1]=str(mes)
data[0]=str(datafinal)
if data[1]=="1":
    data[1]="01"
if data[0]=="1":
    data[0]="01"
print "/".join(data)
