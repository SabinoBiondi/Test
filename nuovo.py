# con utilizzo di variabile e la keyword input().



def somma():
    print("Somma\n")
    # chiede ad un utente di inserire il valore di a
    print ("inserisci il valore di a")
    # prende in input un valore inserito dell'utente e lo trasforma (int) tramite cast in intero. 
    a = int(input())
    # chiede ad un utente ddi in serire il valore di b
    print ("inserisci il valore di b")
    # chiede ad un utente di insaeire il valore di b
    b = int(input())
    # prende in input un valore dall'utente e lo trasforma (int) tramite cast in intero.
    print(f"Risultato della somma:\t {a+b}")

somma()

def sottrazione():
    print("sottrazione\n")
    # chiede ad un utente di inserire il valore di a
    print ("inserisci il valore di a")
    # prende in input un valore inserito dell'utente e lo trasforma (int) tramite cast in intero. 
    a = int(input())
    # chiede ad un utente ddi in serire il valore di b
    print ("inserisci il valore di b")
    # chiede ad un utente di insaeire il valore di b
    b = int(input())
    # prende in input un valore dall'utente e lo trasforma (int) tramite cast in intero.
    print(f"Risultato della sottrazione:\t {a-b}")

sottrazione()

def moltiplicazione():
    print("Moltiplicazione\n")
    # chiede ad un utente di inserire il valore di a
    print ("inserisci il valore di a")
    # prende in input un valore inserito dell'utente e lo trasforma (int) tramite cast in intero. 
    a = int(input())
    # chiede ad un utente ddi in serire il valore di b
    print ("inserisci il valore di b")
    # chiede ad un utente di insaeire il valore di b
    b = int(input())
    # prende in input un valore dall'utente e lo trasforma (int) tramite cast in intero.
    print(f"Risultato della Moltiplicazione:\t {a*b}")

moltiplicazione()

def divisione():
    print("divisione\n")
    # chiede ad un utente di inserire il valore di a
    print ("inserisci il valore di a")
    # prende in input un valore inserito dell'utente e lo trasforma (int) tramite cast in intero. 
    a = int(input())
    # chiede ad un utente ddi in serire il valore di b
    print ("inserisci il valore di b")
    # chiede ad un utente di insaeire il valore di b
    b = int(input())
    if (a==0):
       # o si stma errore o si chiede all'utente di inserire di nuovo il valore
        print("Errore, impossibile dividere il numero per zero")
    if (b==0):
       # o si stma errore o si chiede all'utente di inserire di nuovo il valore
        print("Errore, impossibile dividere il numero per zero")
    else:
        print(f"Risultato della Divisione:\t {a/b}")
    # prende in input un valore dall'utente e lo trasforma (int) tramite cast in intero.
    print(f"Risultato della Divisione:\t {a/b}")

divisione()

def menu():
    print("Scegli ")