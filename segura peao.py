while (True):
    try:
        velvaca, velboy, distanciadeles, distanciap = map(int, raw_input().split(" "))
        if (velboy*(distanciadeles/(velvaca-velboy))<=distanciap):
            print "x("
        else:
            print ":)"
    except ValueError:
        break
