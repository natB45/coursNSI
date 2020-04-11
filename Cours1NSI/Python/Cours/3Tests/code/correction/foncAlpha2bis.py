def alpha(n):
    """ Cette fonction renvoie la nieme lettre de l'alphabet,
    n etant un entier compris entre 1 et 26"""
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert type(n) == int, "n n'est pas un entier !"
    assert (n >= 1) and (n <= 26)," l'entier n'est pas compris entre 1 et 26 !"
    return a[n-1]

# Debut des tests
assert(alpha(1) == "A")
assert(alpha(9) == "I")
assert(alpha(26) == "Z")
