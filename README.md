
# Algorithme de César - Déchiffrement par Brute Force

Ce projet Python déchiffre un message chiffré avec l'algorithme de César en essayant toutes les clés possibles (1 à 25) et en validant le résultat à l'aide d'un dictionnaire de mots. Cela permet de découvrir la clé de déchiffrement correcte en se basant sur les mots reconnus.

## Fonctionnalités

- **Chiffrement de César** : Une fonction `encryptcesar` permet de chiffrer un texte en appliquant un décalage de clé donné.
- **Déchiffrement par brute force** : Une fonction `bruteforcecesar` essaie toutes les clés possibles et valide le résultat en comparant les mots déchiffrés avec un dictionnaire fourni.
- **Validation par dictionnaire** : Le script vérifie le texte déchiffré en comptant le nombre de mots valides trouvés dans un fichier `mots.txt`.

## Installation

1. Clonez le dépôt GitHub :

   ```bash
   git clone https://github.com/FirasJemaa/cesar.git
   ```

2. Accédez au dossier du projet :

   ```bash
   cd cesar-dechiffrement
   ```

3. Assurez-vous d'avoir un fichier `mots.txt` dans le répertoire du projet, contenant une liste de mots valides (un mot par ligne).

## Utilisation

### Fonction de chiffrement

La fonction `encryptcesar` permet de chiffrer un texte en appliquant un décalage de clé César. 

**Exemple d'utilisation** :

```python
texte = "Bonjour le monde"
cle = 3
texte_chiffre = encryptcesar(texte, cle)
print(texte_chiffre)
```

Cela affichera le texte chiffré avec un décalage de 3.

### Déchiffrement par brute force

La fonction `bruteforcecesar` essaie de déchiffrer un texte chiffré en utilisant toutes les clés possibles et en vérifiant les mots déchiffrés avec un dictionnaire.

**Exemple d'utilisation** :

```python
texte_chiffre = "Egbqd bdmfucgq xq ndgfq radoq mhqo puofuazzmudq"
texte_dechiffre = bruteforcecesar(texte_chiffre)
print(f"Texte déchiffré : {texte_dechiffre}")
```

Cette fonction essaiera toutes les clés (1 à 25) pour déchiffrer le message et trouver la solution la plus plausible en se basant sur le fichier `mots.txt`.

### Fichier `mots.txt`

Le fichier `mots.txt` doit contenir une liste de mots communs. Ces mots seront utilisés pour valider le texte déchiffré. Exemple de contenu de `mots.txt` :

```
bonjour
monde
message
texte
secret
clé
...
```

## Détails Techniques

1. **Chiffrement César** : Le texte est décalé de manière circulaire dans l'alphabet avec la clé spécifiée.
2. **Brute Force** : Le script teste toutes les clés de décalage possibles (1 à 25) et utilise un dictionnaire de mots pour valider le texte déchiffré.
3. **Seuil de validation** : Le script considère qu'une solution est correcte si plus de 3 mots du texte déchiffré sont présents dans le dictionnaire. Ce seuil peut être ajusté selon le texte.

## Gestion des erreurs

- Si le fichier `mots.txt` n'est pas trouvé dans le répertoire, un message d'erreur sera affiché.
