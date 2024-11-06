import sys
# Verifier si deux arguments sont fournis
if len(sys.argv)!= 3:
print(" Erreur : Deux arguments sont n ece s s a i r e s .")
sys.exit (1)
# Interprter les arguments
try:
arg1 = float(sys.argv [1])
arg2 = float(sys.argv [2])
except ValueError :
print(" Erreur :Les arguments doivent etre des nombres .")
sys.exit (1)
# Calculer la somme
resultat=arg1 + arg2
# Afficher le resultat
print(resultat)
