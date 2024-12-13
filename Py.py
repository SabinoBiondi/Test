a = 4
b = 0


# stamapa la somma tra due variabili
def somma(a, b):
    print(a + b)


somma(a, b)


# stampa la sottrazione tra due variabili
def sottrazione(a, b):
    print(a - b)


sottrazione(a, b)

# stampa la moltiplicazione tra due variabili


def moltiplicazione(a, b):
    print(a * b)


moltiplicazione(a, b)

# stampa la devisione tra due variabili


def divisione(a, b):
    if (b == 0):
        # o si stma errore o si chiede all'utente di inserire di nuovo il valore
        print("Errore, impossibile dividere il numero per zero")

    else:
        print(a / b)


divisione(a, b)
