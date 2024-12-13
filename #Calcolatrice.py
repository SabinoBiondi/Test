#Calcolatrice

def somma():
    print("somma\n")
    # inserisce il valore di a 
    a = int(input("Inserisci il valore di a: "))
    # inserisce il valore di b
    b = int(input("Inserisci il valore di b: "))
    # prende i risultati della somma e li scrive
    risultato = a+b
    return (f"Risultato della somma: {risultato}")
   
def differenza():
    print("differenza\n")
    # inserisce il valore di a 
    a = int(input("Inserisci il valore di a: "))
    # inserisce il valore di b
    b = int(input("Inserisci il valore di b: "))
    risultato = a-b
    return (f"Risultato della somma: {risultato}")

def moltiplicazione():
    print("moltiplicazione\n")
    # inserisce il valore di a 
    a = int(input("Inserisci il valore di a: "))
    # inserisce il valore di b
    b = int(input("Inserisci il valore di b: "))
    risultato = a*b
    return (f"Risultato della somma: {risultato}")

def quoziente():
    print("quoziente\n")
    # inserisce il valore di a 
    a = int(input("Inserisci il valore di a: "))
    # inserisce il valore di b
    b = int(input("Inserisci il valore di b: "))
    if (a==0):
       # o si stma errore o si chiede all'utente di inserire di nuovo il valore
        return(f"Errore, impossibile dividere il numero per zero")
    if (b==0):
       # o si stma errore o si chiede all'utente di inserire di nuovo il valore
        return(f"Errore, impossibile dividere il numero per zero")
    else:
        risultato = a/b
        return(f"Risultato della quoziente {risultato}")

def menu():
    print("\n- Scegli l'operaziona da seguire")
    print("1- Somma")
    print("2- Differenza")
    print("3- Moltiplicazione")
    print("4- Quoziente")
    print("5- Esci")


while True:
    menu()
    scelta = input("Inserisci il numero relativo all'operazione: ")

    if scelta == "5":
        break

    elif scelta == "1":
        print (somma())

    elif scelta == "2":
        print (differenza())
        
    elif scelta == "3":
        print (moltiplicazione())
        
    elif scelta == "4":
        print (quoziente())
