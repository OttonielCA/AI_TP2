# Fonction recursive qui additione un nombre 'n' avec lui meme en faisant des sauts de -1
def add_recursive(n):
    # Si le nombre arrive a valoir 1, on arrête la fonction recursive
    if n == 1:
        # print("iteration is equal 1, stopped")
        return 1

    # Retourne un appel de la fonction elle même avec son paramètre 'n' diminué de 1, ceci en
    # additionnant un deuxième appel de la fonction elle même avec son paramètre 'n' diminué de 1
    return add_recursive(n - 1) + add_recursive(n - 1)
