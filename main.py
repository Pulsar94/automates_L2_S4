from function import automate_standard
from function import standardiser_automate
from function import automate_determine
from function import determiniser_automate
from function import minimiser_automate
from function import complementarisation_automate

from complet import verif_complet
from complet import complet

from affichage import lire_fichier_transition
from affichage import afficher_table_transition
from affichage import tableau_to_graphe
from affichage import affichage_automate_graphe
from affichage import ecriture_tableau


def safe_input(y, mini, maxi):
    while True:
        try:
            x = int(input(y))
            while (x < mini or x > maxi):
                x = int(input(
                    "\n\n###############   Choisir un nombre entier entre 1 et 10 correspondant à une fonction du menu :    ################\n\n"))
            break
        except ValueError:
            print("\n\n########  S'il vous plait, entrer un entier entre 1 et 10  ########\n")
    return x


# Début du programme

if __name__ == "__main__":
    G, G = [], []
    menu = 0
    AutomataNb = 1
    while G == []:
        G = lire_fichier_transition("automates/automotates5.txt")

    while (menu != 10):
        print("""\n###################           Menu Principal           #############################
            0. Afficher un automate sous forme de tableau
            1. Afficher un automate sous forme graphique
            2. Charger un automate
            3. Informations sur l'automate
            4. Standardisation
            5. Determination       
            6. Compléter 
            7. Minimisation
            8. Langage complementaire
            9. Tester un mot
            10. Quitter""")
        menu = safe_input("\nChoisir une fonction: \n", 0, 10)

        if menu == 0:
            afficher_table_transition(G)

        elif menu == 1:
            Graphe = tableau_to_graphe(G)
            affichage_automate_graphe(Graphe)

        elif menu == 2:
            G = []
            AutomataNb = safe_input("\nChoisir un automate (1 à 30)\n", 0, 30)
            G = lire_fichier_transition("automates/automotates"+str(AutomataNb)+".txt")

        elif menu == 3:
            if automate_standard(G) :
                print("L'automate est standard")
            else:
                print("L'automate n'est pas standard")

            if automate_determine(G) :
                print("L'automate est deterministe")
            else:
                print("L'automate n'est pas deterministe")

            if verif_complet(G,complet=0) :
                print("L'automate est complet")
            else:
                print("L'automate n'est pas complet")

        elif menu == 4:
            G = standardiser_automate(G)
            ## écriture du résultat dans le fichier txt
            # writeInFile('execution/B5-' + AutomataNb + '-Standardisé.txt', G)
            ecriture_tableau(G, 'execution/B5-' + str(AutomataNb) + '-Standardise.txt', "Automate Standardisé: ")
            # fonction pour reconnaitre un mot

        elif menu == 5:
            G = determiniser_automate(G)
            ## écriture du résultat dans le fichier txt
            # writeInFile('execution/B5-' + AutomataNb + '-Determinisé.txt', G)
            ecriture_tableau(G, 'execution/B5-' + str(AutomataNb) + '-Determinise.txt', "Automate Determinisé: ")
            # fonction pour reconnaitre un mot

        elif menu == 6:
            G = complet(G)
            ## écriture du résultat dans le fichier txt
            # writeInFile('execution/B5-' + AutomataNb + '-Determinisé.txt', G)
            ecriture_tableau(G, 'execution/B5-' + str(AutomataNb) + '-Complet.txt', "Automate Complet: ")
            # fonction pour reconnaitre un mot

        elif menu == 7:
            G = minimiser_automate(G)
            ## écriture du résultat dans le fichier txt
            # writeInFile('execution/B5-' + AutomataNb + '-Minimisé.txt', G)
            ecriture_tableau(G, 'execution/B5-' + str(AutomataNb) + '-Minimise.txt', "Automate Minimisé: ")
            # fonction pour reconnaitre un mot

        elif menu == 8:
            G = complementarisation_automate(G)
            # writeInFile('execution/B5-' + AutomataNb + '-LanguageComplementaire.txt', G)
            ecriture_tableau(G, 'execution/B5-' + str(AutomataNb) + '-LanguageComplementaire.txt', "Automate Complémentarisé: ")
            # fonction pour reconnaitre un mot

        ## elif menu == 9:
            # fonction pour reconnaitre un mot


        else:
            menu = 10
            print("Merci de votre utilisation, à bientôt !")
            break