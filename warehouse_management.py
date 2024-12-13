
warehouse = { "Elettronica": {"Laptop": 10, "Smartphone": 20}, "Abbigliamento": {"Maglietta": 50, "Jeans": 30}, "Cibo": {"Mela": 30, "Pane": 25}}
categorie = ["Elettronica", "Abbigliamento", "Cibo"]
prodotti = {"Laptop": 10, "Smartphone": 20}
quantita = { 10, 20}

def visualizza_prodotti():
    for categorie, prodotti in warehouse.items():
        print(f"Categoria: {categorie}")
    for prodotti, quantita in categorie.items():
        print(f" {prodotti}: {quantita}")

def aggiungi_prodotto():
    warehouse[categorie] = (prodotti)
    print("nuovo prodotto {prodotti} = {categiore}")

def rimuovi_prodotto():
    print(f"Inserisci il prodotto {prodotti()} da cancellare")
    del warehouse[categorie][prodotti]
    print(f"{prodotti} rimosso con successo")

def aggiungi_quantita():


    def menu_managment():
        print("\n- Scegli l'operaziona da eseguire")
        print("1- Visualizza prodotti")
        print("2- Aggiungi prodotti")
        print("3- Aggiungi quantità")
        print("4- Rimuovere prodotto")
        print("5- Accedi alla gestione degli ordini")
        print("6- Esci")


    while True:
        menu_managment()
        scelta = input("Inserisci il numero relativo all'operazione da eseguire: ")

        if scelta == "6":
            break

        elif scelta == "1":
            print (visualizza_prodotti())

        elif scelta == "2":
            print (aggiungi_prodotto())
        
        elif scelta == "3":
            print (aggiungi_quantita())
        
        elif scelta == "4":
            print (rimuovi_prodotto())

        elif scelta == "5":
            print ()
        else:
            print("Scelta non valida")  