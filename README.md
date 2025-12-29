<p align="center">
<u><b>Membres du Groupe</b></u> <br>
</p>
<ul>
<li>ABI MIRABEL TEMBELE(23B506FS)   Participation(exo4, exo8, ex022)</li>  <br>
<li>TEMWA HABMO MAXIME(22A578FS)    Participation(exo4, exo8, ex022)</li>   <br>
<li>MOHAMADOU AWALOU(21A286FS)      Participation(exo4, exo8)</li>   <br>
<li>PADEMONA STEPHANE(21A282FS)     Participation(exo4, exo8)</li> <br>
</ul>

            exercice 4: Reversibilité de nombres
<b>Problème: une fonction qui prend une liste et retourne ceux qui sont les memes quand on les lit droite à gauche</b> <br>
<p align="center">
           <b>Explication de la solution:</b> <br>
</p>
<ul>
<li>la fonction prend en entrée un nombre (n)</li>  <br>
<li>n_str=str(n) convertir les nombres en chaine</li>  <br>
<li>return n_str == n_str[:: -1] compare la chaine à son inverse</li>  <br>
<li>def nombres_palindromes(l): prend en entrée une liste de nombres et retourne ceux qui sont palindromes</li>  <br>
<li>return[n for n in l if est_palindrome(n)] comprehension de liste pour trouver les nombres palindromes</li>  <br>
<li>s=input("entrez une liste de nombres : ") permet à l'utilisateur d'entrée une liste de nombres</li>  <br>
<li>N=[int(x) for x in s.split()] converti les nombres en entiers et les stocke dans une liste</li>  <br>
<li>print("les nombres palindromes sont:", palindrome) affiche la liste de tout les palindrome trouvés</li>  <br>
</ul>

            exercice 8: Générateur de nombres premiers jusqu'à
<b><u>Problème:</u> créez une fonction qui génère tous les nombres premiers inférieurs ou égaux un nombre donné sans utiliser la ,éthode du crible   d'Eratosthène</b>  <br>
<p align="center">
           <b>Explication de la solution:</b>  <br>
</p>
<ul>
<li>la fonction prend en entrée un nombre (n)</li>  <br>
<li>if n < 2 vérifie si le nombre est inférieur à 2</  <br>
<li>for i in range(2, int(n**0.5)+1): teste les diviseur jusqu'à la racine carré de n </li> <br>
<li>if n % i== 0: vérifie si n est divisible par i si oui alors la fonction retourne False sinon la fonction retourne True</li>  <br>
<li>N=[i for i in range(2, n+1) if est_premiers(i)] permet de créer une liste N qui contient tout les nombres premiers entre 2 et n</li>  <br>
<li>print(f"nombres premiers <={n} : {N}") affiche tout les nombres premiers entre 2 et n  <br>
</u>
            
           <b> exercice 22: Afficher le calendrier du mois</b>
<b><u>Problème:</u> Ecrire un programme qui genère un calendrier respectant la syntaxe suivante</b>  <br>
>>>Entrez le nombres de jours dans le mois  <br>
>>>30  <br>
>>>entrez le premier jour du mois : 1 pour lundi, 7 pour dimanche  <br>
>>>3 <br>
<p align="center">
            <b>Explication de la solution:</b> <br>
</p>
<ul>
<li>nb_jours=int(input("veuillez entrer le nombre de jours du mois :")) demande à l'utilisateur d'entrer le nombre de jours du mois</li>  <br>
<li>while nb_jours < 1 or nb_jours > 31: </  <br>
 <li> nb_jours=int(input("Veuillez entre un nombre entre 1 et 31:")) tantque l'utilisateur n'entre pas un nombre entre 1 et 31, la fonction lui -demande d'entrer le nombre de jours</li>  <br>
<li>premier_jour=int(input("veuillez entrer le premier jour du mois (1=Lundi, 7=Dimache) :")) demande a l'utilisateur d'entrer le premier jour du mois</li>  <br>
<li>jours_semaine= ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"] affiche les jours de la semaine</li>  <br>
<li>print(" ".join(jours_semaine))</li>  <br>
<li>print("  " * (premier_jour -1), end="")   affiche des espaces entre les jours de la semaine</li>  <br>
<li>for jour in range(1, nb_jours + 1): </li> <br>
  <li>print(f"{jour:4}", end=" ") affiche le calandrier </li>  <br>
 <li>if(jour + premier_jour -1) %7== 0:</li> <br>
   <li>print()      permet d'aller à la ligne à chaque fin de semaine</li>          
</ul>         
