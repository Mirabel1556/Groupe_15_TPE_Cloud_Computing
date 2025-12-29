def est_palindrome(n):
  #convertir les nombres en chaine pour permettre l'inversion  
     n_str=str(n)
   #comparaison de la chaine avec son inverse
     return n_str == n_str[:: -1]
""" la fonction prend en entre une liste de nombres et retourne uniquement une liste de nombres palindrome"""
def nombres_palindromes(l):
    #comprehension de liste pour trouver les palindromes
    return[n for n in l if est_palindrome(n)]
#demande a l'utilisateur d'entrer une liste de nombres
s=input("entrez une liste de nombres : ")
""" convertir les nombres en entiers et les garde dans une liste"""
N=[int(x) for x in s.split()]
palindrome= nombres_palindromes(N)
"""affiches la liste de nombres palindromes trouvés """
print("les nombres palindromes sont:", palindrome)
       
