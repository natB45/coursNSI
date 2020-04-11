def alpha(n):
    """ Cette fonction renvoie la nieme lettre de l'alphabet,
    n etant un entier compris entre 1 et 26"""
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return a[n]

# Debut des tests
assert(alpha(1) == "A")
assert(alpha(9) == "I")
assert(alpha(26) == "Z")
#assert(alpha(30) == "")