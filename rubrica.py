rubrica_dizionario = {" Antonio " : "33478902345"," Roberto " : "33478002345", "Anna " : "33478962345"," Francesca" : "3347863457"}
print(rubrica_dizionario)

def cerca(nome):
    if nome in rubrica_dizionario:
        print(f"Il numero di {nome} è {rubrica_dizionario{nome} }")
    else:
        print(f"{nome} non è in rubrica.")

def nuova_voce(nome, numero):
    rubrica_dizionario[nome]= numero
    print(f"nuova voce {nome} = {numero}")


def rubrica():
    print(rubrica_dizionario())
    return

#Menu

print("\n")
    