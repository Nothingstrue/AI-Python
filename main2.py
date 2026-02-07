users = []
moneyspent = []
exitcheck = bool(True)
selection = int(0)
while exitcheck:
    while selection<1 or selection>6 :
        selection = int(input(""">> Benvenuto al resort 'La Sfera'. Inserire l'azione che si vuole svolgere:
        >> 1. Inserire utente nel piano vacanze
        >> 2. Controllare il piano vacanze
        >> 3. Decidere la vacanza
        >> 4. Controllare le opzioni disponibili
        >> 5. Uscire dal programma"""))