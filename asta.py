import re


def stampa_lista(lista_offerte):
    for offerta in lista_offerte:
        print(f"Email Offerente: {offerta[0]} - Offerta: {offerta[1]}")
    return None


def get_input(text):
    return input(text)


def offerta_check(offerta):
    try:
        offerta = float(offerta)
    except:
        print("Formato non valido")
        return False
    return True


def email_check(email):
    if re.match("^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
        return True
    return False


def search_email_in_list(lista, email):
    sublistFound = False
    for sublist in lista:
        if sublist[0] == email:
            print("Questo utente ha già una sua unica offerta... respinto!")
            sublistFound = True
            break
    return sublistFound


def lista_offerte():
    lista = []

    altre_offerte = True
    while altre_offerte:
        offerta = get_input("Inserisci l'offerta pervenuta (0 per terminare): ")

        if not offerta_check(offerta):
            continue
        offerta = float(offerta)
        if not offerta:
            altre_offerte = False
            continue

        email_errata = True
        while email_errata:
            email = get_input("Inserisci la mail: ")
            if not email_check(email):
                print("Email non valida {0}".format(email))
                continue
            email_errata = False

    #se la mail non è già presente in lista aggiungo la coppia in lista
        if not search_email_in_list(lista, email):
            lista.append(([email, offerta]))

    print(lista)
