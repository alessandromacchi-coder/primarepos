persone = [("luca", 18), ("antonio", 24), ("gianna", 60), ("andrea", 29), ("barbara", 18), ("fabio", 60), ("giorgia", 24), ("michela", 60), ("lucia", 18), ("angela", 24)]

gruppi= {}

for nome, eta in persone:
    if eta not in gruppi:
        gruppi[eta]= []
    gruppi[eta].append(nome)

print(gruppi)

