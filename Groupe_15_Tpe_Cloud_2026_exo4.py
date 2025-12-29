def est_palindrome(n):
     s=str(n)
     reverse= s[:: -1]
     if s == reverse:
         return f"{n} est palindrome"
     else:
         return f"{n} n'est pas palindrome"
# demadez a l'utilisateur d'entrer un nombre
n=input("entrez un nombre :")
#appelons la fonction pour determiner si le nombre est palindrome
print(est_palindrome(n))
