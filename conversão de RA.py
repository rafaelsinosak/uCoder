quantidade=int(input())
for x in range (quantidade):
    ra=raw_input()
    fatec="003"
    curso=ra[0:2]
    ano=ra[2:4]
    semestre=ra[4]
    turno=""
    final=ra[5:10]
    if curso=="AD":
        curso="048"
        turno="1"
    elif curso=="AN":
        curso="048"
        turno="3"
    elif curso=="SD":
        curso="061"
        turno="1"
    elif curso=="LT":
        curso="074"
        turno="2"
    elif curso=="PL":
        curso="080"
        turno="2"
    elif curso=="PD":
        curso="099"
        turno="1"
    elif curso=="PN":
        curso="099"
        turno="3"
    elif curso=="OD":
        curso="100"
        turno="1"
    elif curso=="ON":
        curso="100"
        turno="3"
    print fatec+curso+ano+semestre+turno+final
    
    
        
    
    
