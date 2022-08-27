user_aktiv = True
pi = float(3.1415)

while user_aktiv == True:
    r = float(input("Geben sie den Radius in cm an: "))

    d = float(r * 2)
    u = float(2 * pi * r)
    f = float(pi * (r * r))

    print("Der Durchmesser beträgt: ", "%.2f" % d, " cm")
    print("Der Umfang beträgt: ", "%.2f" % u, " cm")
    print("Der Flächeninhalt beträgt: ", "%.2f" % f ," cm²")

    wahl = str(input("Möchten sie einen weiteren Kreis berechnen? <j/n>: ")).lower
    if wahl == ("j") or ("J"):
        user_aktiv == True
    elif wahl == ("n") or ("N"):
        user_aktiv == False
    else:
        print("Falsche Eingabe")

print("Bis zum nächsten Mal!")