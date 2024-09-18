# Fonction recursive qui additione un nombre 'n' avec lui meme en faisant des sauts de -1
# en gardant la valeur de 'n' dans un dictionnaire pour eviter la repetition de computation
def add_recursive_mem(n, memo={}):
    # Si le nombre arrive a valoir 1, on arrête la fonction recursive
    if n == 1:
        # print("iteration is equal 1, stopped")
        return 1
    # Si le nombre 'n' a deja ete calculer, on retourne sa valeur stocker dans le dictionnaire
    elif n in memo:
        return memo[n]

    # Appel de la fonction elle même avec son paramètre 'n' diminué de 1, ceci en
    # additionnant un deuxième appel de la fonction et les meme parametres, stocker dans le dictionnaire memo
    memo[n] = add_recursive_mem(n - 1) + add_recursive_mem(n - 1)
    # print(memo)

    # Retourne la valeur de la cle 'n' dans le dictionnaire memo
    return memo[n]

# On demande à l'utilisateur un nombre
n = int(input("Veuillez donner un nombre: "))

# Appel de la fonction
print(f"La réponse est: {add_recursive_mem(n)}")
