"""entrez le nombre de jours du mois"""
nb_jours=int(input("veuillez entrer le nombre de jours du mois :"))
while nb_jours < 1 or nb_jours > 31:
    nb_jours=int(input("Veuillez entre un nombre entre 1 et 31:"))
"""le premier jour du mois"""
premier_jour=int(input("veuillez entrer le premier jour du mois (1=Lundi, 7=Dimache) :"))
#Affichage des jours du mois
jours_semaine= ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"]
"""affichage des espaces entre les jours"""
print(" ".join(jours_semaine))
print("  " * (premier_jour -1), end="")
"""affichage des jours du mois"""
for jour in range(1, nb_jours + 1):
    print(f"{jour:4}", end=" ")
    #aller a la ligne a chaque fin de semaine
    if(jour + premier_jour -1) %7== 0:
       print()                
                       
