Membres du Groupe
ABI MIRABEL TEMBELE(23B506FS) Participation(exo4, exo8, ex022)
TEMWA HABMO MAXIME(22A578FS)  Participation(exo4, exo8, ex022)
MOHAMADOU AWALOU(21A286FS)    Participation(exo4, exo8)
PADEMONA STEPHANE(21A282FS)   Participation(exo4, exo8)

           exercice 4: Reversibilité de nombres
Problème: une fonction qui prend une liste et retourne ceux qui sont les memes quand on les lit droite à gauche
           Explication de la solution:
la fonction prend en entrée un nombre (n)
 n_str=str(n) convertir les nombres en chaine
return n_str == n_str[:: -1] compare la chaine à son inverse 
def nombres_palindromes(l): prend en entrée une liste de nombres et retourne ceux qui sont palindromes
return[n for n in l if est_palindrome(n)] comprehension de liste pour trouver les nombres palindromes
s=input("entrez une liste de nombres : ") permet à l'utilisateur d'entrée une liste de nombres
N=[int(x) for x in s.split()] converti les nombres en entiers et les stocke dans une liste
print("les nombres palindromes sont:", palindrome) affiche la liste de tout les palindrome trouvés

            exercice 8: Générateur de nombres premiers jusqu'à n
Problème: créez une fonction qui génère tous les nombres premiers inférieurs ou égaux un nombre donné sans utiliser la ,éthode du crible d'Eratosthène
            Explication de la solution:
la fonction prend en entrée un nombre (n)
if n < 2 vérifie si le nombre est inférieur à 2
for i in range(2, int(n**0.5)+1): teste les diviseur jusqu'à la racine carré de n 
if n % i== 0: vérifie si n est divisible par i si oui alors la fonction retourne False sinon la fonction retourne True
N=[i for i in range(2, n+1) if est_premiers(i)] permet de créer une liste N qui contient tout les nombres premiers entre 2 et n
print(f"nombres premiers <={n} : {N}") affiche tout les nombres premiers entre 2 et n

            exercice 22: Afficher le calendrier du mois
Problème: Ecrire un programme qui genère un calendrier respectant la syntaxe suivante
>>>Entrez le nombres de jours dans le mois
>>>30
>>>entrez le premier jour du mois : 1 pour lundi, 7 pour dimanche
>>>3
            Explication de la solution
nb_jours=int(input("veuillez entrer le nombre de jours du mois :")) demande à l'utilisateur d'entrer le nombre de jours du mois
while nb_jours < 1 or nb_jours > 31:
    nb_jours=int(input("Veuillez entre un nombre entre 1 et 31:")) tantque l'utilisateur n'entre pas un nombre entre 1 et 31, la fonction lui demande d'entrer le nombre de jours
premier_jour=int(input("veuillez entrer le premier jour du mois (1=Lundi, 7=Dimache) :")) demande a l'utilisateur d'entrer le premier jour du mois
jours_semaine= ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"] affiche les jours de la semaine
print(" ".join(jours_semaine))
print("  " * (premier_jour -1), end="")   affiche des espaces entre les jours de la semaine
for jour in range(1, nb_jours + 1):
    print(f"{jour:4}", end=" ") affiche le calandrier
 if(jour + premier_jour -1) %7== 0:
       print()      permet d'aller à la ligne à chaque fin de semaine          
              
