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
            sublistFound = True
            break
    return sublistFound


def lista_offerte():
    lista = []

    altre_offerte = True
    while altre_offerte:
        offerta = get_input("Inserisci l'offerta pervenuta (0 per terminare): ")

        if not offerta_check(offerta):
            print("Formato non valido")
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

        # se la mail non è già presente in lista aggiungo la coppia in lista
        if not search_email_in_list(lista, email):
            lista.append(([email, offerta]))
        else:
            print("Questo utente ha già una sua unica offerta... respinto!")

    return lista


def mediaOfferte(lista):
    somma = 0.0
    for offerta in lista:
        somma += offerta[1]
    return somma / len(lista)


def minimo(lista):
    min = lista[0]
    for offerta in lista[1:]:
        if offerta[1] < min[1]:
            min = offerta

    return min


def massimo(lista):
    max = lista[0]
    for offerta in lista[1:]:
        if offerta[1] > max[1]:
            max = offerta

    return max


def simula_inserimento_offerte():
    return [("donant@gmail.com", 100), ("lucapicci@gmail.com", 30), ("marifu@gmail.com", 60),
            ("donant@outlook.com", 50)]

# Mia versione iniziale
# def minimo(lista):
#
#     new_lista = []
#     for offerta in lista:
#         new_lista.append(offerta[1])
#     return min(new_lista)
# def massimo(lista):
#     new_lista = []
#     for offerta in lista:
#         new_lista.append(offerta[1])
#     return max(new_lista)
