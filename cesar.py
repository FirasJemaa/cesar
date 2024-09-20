'''
Déchiffrer un message chiffré par un algorithme de César en essayant toutes les clés possibles et en validant le résultat en comparant les mots déchiffrés avec un dictionnaire.
'''

# Fonction de chiffrement César
def encryptcesar(texte, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chiffrement = ""
    for lettre in texte:
        if lettre != " ":
            lettreMaj = lettre.isupper()  # Vérifie si la lettre est en majuscule
            index = alphabet.index(lettre.upper())  # Trouve l'index de la lettre dans l'alphabet
            index = (index + key) % 26  # Applique le décalage
            nouvelle_lettre = alphabet[index]
            chiffrement += nouvelle_lettre if lettreMaj else nouvelle_lettre.lower()
        else:
            chiffrement += " "  # Conserve les espaces
    return chiffrement

# Fonction de bruteforce pour le déchiffrement
def bruteforcecesar(ciphertext):
    try:
        # Charger le dictionnaire de mots dans une liste
        with open("mots.txt", "r") as dictionnaire:
            # Convertit chaque mot en minuscule et supprime les sauts de ligne
            mots_dictionnaire = {line.strip().lower() for line in dictionnaire}

        # Tester toutes les clés de décalage possibles (de 1 à 25)
        for key in range(1, 26):
            dechiffrement = encryptcesar(ciphertext, key)
            mots_dechiffres = dechiffrement.split()

            # Compter combien de mots du texte déchiffré sont dans le dictionnaire
            compteur = 0
            for mot in mots_dechiffres:
                if mot.lower() in mots_dictionnaire:
                    compteur += 1

            # Si un certain nombre de mots sont trouvés dans le dictionnaire, on suppose que la clé est correcte
            if compteur > 3:  # Ce seuil peut être ajusté en fonction du texte
                print(f"Clé possible : {key}")
                return dechiffrement  # On retourne la solution dès qu'on a trouvé un texte plausible

        print("Aucune solution possible trouvée.")
    except FileNotFoundError:
        print("Le fichier 'mots.txt' est introuvable. Assurez-vous qu'il existe dans le répertoire.")

# Appel de la fonction bruteforce sur le texte chiffré
print(f"Texte déchiffré : {bruteforcecesar("Egbqd bdmfucgq xq ndgfq radoq mhqo puofuazzmudq")}")
