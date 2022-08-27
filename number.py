number = 5
result = ((number * 2) + 12 ) / 2
print ( result)
result = ((number *2) + 12) / 2
print(int(result))
print ("Du hast "+
    str(number) +
    " ausgewählt, das magische Ergebnis ist " +
    str(int(result)) +
    "!")
mail = "willy.wizard@zauberschule.de"
print (mail.split("@"))
print (mail.split("@")[0])    

mail = "info@helena-hexe.com"

print(mail.split("@")[1].split(".")[0])

mail1 = "zarah.zauber@zauberberg.de"
mail2 = "info@trixie-trickser.com"
mail3 = "uwe_unhold@dunkelnetz.de" 

clients = []

# Füge hier deinen Code ein
clients.append(mail1)
clients.append(mail2)
clients.append(mail3)

print(clients)
print(len(clients))

zauberer = ["Buehnenzauberer", "magic.com"]

# Ergänze hier deinen Code
print("@".join(zauberer))