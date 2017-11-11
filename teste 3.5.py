lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)
print (len(lines))
for x in range (len(lines)):
    velvaca, velboy, distanciadeles, distanciap = map(input().split(" "))
    aproxima=0
    ms=velvaca-velboy
    aproxima=distanciadeles/ms
    final=0
    final=velboy*aproxima
    if (final<=distanciap):
        print ("X)")
    else:
        print (":)")
