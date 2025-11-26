
figura = input("Inserisci la figura geometrica (quadrato, rettangolo, triangolo, cerchio o rombo): ")

if figura == "quadrato":
    lato = float(input("dimmi la lunghezza del lato: "))
    area = lato ** 2
    print("questa è l'area del quadrato:", area)
elif figura == "rettangolo":
    base = float(input("dimmi la lunghezza della base: "))
    altezza = float(input("dimmi l'altezza: "))
    area = base * altezza
    print("questa è l'area del rettangolo:", area)
elif figura == "triangolo":
    base = float(input("dimmi la lunghezza della base: "))
    altezza = float(input("dimmi l'altezza: "))
    area = (base * altezza) / 2
    print("questa è l'area del triangolo:", area)
elif figura == "cerchio":
    raggio = float(input("dimmi il raggio: "))
    area = 3.14 * raggio ** 2
    print("questa è l'area del cercgio", area)
elif figura == "rombo":
    diagonale_maggiore = float(input("dimmi la lunghezza della diagonale maggiore: "))
    diagonale_minore = float(input("dimmi la lunghezza della diagonale minore: "))
    area =( diagonale_maggiore * diagonale_minore)/2
    print("questa è l'area del rombo", area)
else:
    print("non so calcolare questa figura")