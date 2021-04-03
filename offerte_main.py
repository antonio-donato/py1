import asta


def stampa_offerta(offerte):
    for elem in offerte:
        print(f"Email offerta: {elem[0]} - Offerta: {elem[1]}")


# offerte = asta.lista_offerte()
offerte = asta.simula_inserimento_offerte()
stampa_offerta(offerte)
print("=" * 40)
offerte.remove(asta.minimo(offerte))
offerte.remove(asta.massimo(offerte))
offerta_media = asta.mediaOfferte(offerte)
tolleranza = offerta_media / 100 * 10
print(f"Tolleranza 10%: {tolleranza}")

offerte_filtrate = [x for x in offerte if abs(x[1] - offerta_media) < tolleranza]
print("=" * 40)

stampa_offerta(offerte_filtrate)
# if len(offerte): print(asta.mediaOfferte(offerte))
