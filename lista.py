def mostra_menu():
    print("\nMenu:")
    print("1. Aggiungi un elemento alla lista")
    print("2. Rimuovi un elemento dalla lista")
    print("3. Visualizza la lista")
    print("4. Esci")
    return input("Scegli un'opzione (1-4): ")

def aggiungi_elemento(lista):
    elemento = input("Inserisci l'elemento da aggiungere: ").strip()
    if elemento:
        lista.append(elemento)
        print(f"'{elemento}' è stato aggiunto alla lista!")
    else:
        print("Non è stato inserito alcun elemento valido.")

def rimuovi_elemento(lista):
    elemento = input("Inserisci l'elemento da rimuovere: ").strip()
    if elemento in lista:
        lista.remove(elemento)
        print(f"'{elemento}' è stato rimosso dalla lista!")
    else:
        print(f"'{elemento}' non è presente nella lista.")

def visualizza_lista(lista):
    if lista:
        print("\nLa tua lista della spesa contiene:")
        for i, elemento in enumerate(lista, start=1):
            print(f"{i}. {elemento}")
    else:
        print("\nLa lista della spesa è vuota.")

def main():
    lista_della_spesa = []
    while True:
        scelta = mostra_menu()
        if scelta == "1":
            aggiungi_elemento(lista_della_spesa)
        elif scelta == "2":
            rimuovi_elemento(lista_della_spesa)
        elif scelta == "3":
            visualizza_lista(lista_della_spesa)
        elif scelta == "4":
            print("Grazie per aver utilizzato l'app! A presto!")
            break
        else:
            print("Scelta non valida. Per favore, inserisci un numero tra 1 e 4.")

if __name__ == "__main__":
    main()
