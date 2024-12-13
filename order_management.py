from warehouse_management import warehouse

order_history = []

def crea_ordine(warehouse):
    ordine = {}
    
def visuavisualizza_ordini():


    def ordini_menu():
        while True:

            print("\n- Scegli l'operazione da eseguire")
            print("1- Crea un nuovo ordine")
            print("2- Visualizza la cronologia degli ordini")
            print("3- Tornare al menu principale.")
            scelta = input("Seleziona opzione: ")

            if scelta == "1":
                crea_ordine()
            elif scelta == "2":
                visuavisualizza_ordini()
            elif scelta == "3":
                break
            else:
                print("Scelta non valida")

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


def main_menu():
    print("\n Menu Principale ")

    print("1. Gestione Magazzino")
    print("2. Gestione Ordini")
    print("3. Esci")
    scelta = input("Seleziona un'opzione: ")

    if scelta == "1":
            menu_managment()
    elif scelta == "2":
            ordini_menu():
    elif scelta == "3":
        print("Uscita dall'applicazione.")
        break
        
    else:
        print("Scelta non valida.")