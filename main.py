numnight = int(input("Inserire numero di notti desiderate: "))
pricexnight = int(input("Inserire il numero per notte: "))
name = input("Inserite il vostro nome: ")
totprice = numnight * pricexnight
print(f"""numero di notti: {numnight}
Prezzo per notte: {pricexnight}€
Nome: {name}
Prezzo totale: {totprice}€""")