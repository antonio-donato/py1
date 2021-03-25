import re

offerte = []
altre_offerte = True

while altre_offerte:
    offerta = input("Inserisci l'offerta pervenuta (0 per terminare): ")

    try:
        offerta = float(offerta)
    except:
        print("Formato non valido")
        continue
    if not offerta:
        altre_offerte = False
        continue

    email_errata = True

    while email_errata:
        email = input("Inserisci la mail: ")
        if re.match("^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
           break

        print("Email non valida {0}".format(email))
        continue

    offerte.append([email, offerta])

print(offerte)