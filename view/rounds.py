def get_output():
    print(" 1 victoire du joueur 1  ")
    print(" 2 victoire du joueur 2  ")
    print(" 0 egalité chaque joueur recoit 0,5 points :  ")
    output = input("resultat du match:")
    if output == "1":
        return output
    elif output == "2":
        return output
    elif output == "0":
        return output
    else:
        print("uniquement des valuer numerique 1,2,0")
        get_output()
