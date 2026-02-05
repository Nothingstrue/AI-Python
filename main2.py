users = []
moneyspent = []
exitcheck = bool(True)
selection = int(0)
while exitcheck:
    while selection<1 or selection>6 :
        selection = int(input(""">> Benvenuto al resort 'La Sfera'. Inserire l'azione che si vuole svolgere:
        d"""))