"""
Nom du projet : Traitement d’automate fini
Auteurs : Thibaut MENIN - Tao SOLAN – Quentin ADELINE – Marc ROUGAGNOU – Soazic FOURNIER
Description : Ce projet nous permet de lire des automates fini selon une certaine nomenclature,
et ainsi pouvoir effectuer différentes actions possible sur ces derniers

████████╗██████╗░░█████╗░██╗████████╗███████╗███╗░░░███╗███████╗███╗░░██╗████████╗
╚══██╔══╝██╔══██╗██╔══██╗██║╚══██╔══╝██╔════╝████╗░████║██╔════╝████╗░██║╚══██╔══╝
░░░██║░░░██████╔╝███████║██║░░░██║░░░█████╗░░██╔████╔██║█████╗░░██╔██╗██║░░░██║░░░
░░░██║░░░██╔══██╗██╔══██║██║░░░██║░░░██╔══╝░░██║╚██╔╝██║██╔══╝░░██║╚████║░░░██║░░░
░░░██║░░░██║░░██║██║░░██║██║░░░██║░░░███████╗██║░╚═╝░██║███████╗██║░╚███║░░░██║░░░
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░

██████╗░██╗░█████╗░██╗░░░██╗████████╗░█████╗░███╗░░░███╗░█████╗░████████╗███████╗        ███████╗██╗███╗░░██╗██╗
██╔══██╗╚█║██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗████╗░████║██╔══██╗╚══██╔══╝██╔════╝        ██╔════╝██║████╗░██║██║
██║░░██║░╚╝███████║██║░░░██║░░░██║░░░██║░░██║██╔████╔██║███████║░░░██║░░░█████╗░░        █████╗░░██║██╔██╗██║██║
██║░░██║░░░██╔══██║██║░░░██║░░░██║░░░██║░░██║██║╚██╔╝██║██╔══██║░░░██║░░░██╔══╝░░        ██╔══╝░░██║██║╚████║██║
██████╔╝░░░██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝██║░╚═╝░██║██║░░██║░░░██║░░░███████╗        ██║░░░░░██║██║░╚███║██║
╚═════╝░░░░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝        ╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═╝
"""

################## IMPORT ##################

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

import os
import copy

############################################

def safe_input(y, mini, maxi):
    while True:
        try:
            x = int(input(y))
            while (x < mini or x > maxi):
                x = int(input(
                    "\n\n###############   Choisir un nombre entier entre "+mini+" et "+maxi+":    ################\n\n"))
            break
        except ValueError:
            print("\n\n########  S'il vous plait, entrer un entier entre "+mini+" et "+maxi+"  ########\n")
    return x


def generate_automate(number):
    """
    Va créer tous les fichiers associés à la résolution des actions effectuées sur les automates dans le dossier execution
    :param number: 1
    :return: rien
    """
    auto = lire_fichier_transition("automates/automate" + str(number) + ".txt")

    "----------------------------------------------------------------------------------"
    auto_temp = standardiser_automate(copy.deepcopy(auto))
    ecriture_tableau(auto_temp, 'execution/Automate_' + str(number) + '-Standardise.txt', "Automate Standardise: ")

    "----------------------------------------------------------------------------------"
    auto_temp = determiniser_automate(copy.deepcopy(auto))
    ecriture_tableau(auto_temp, 'execution/Automate_' + str(number) + '-Determinise.txt', "Automate Determinise: ")

    "----------------------------------------------------------------------------------"
    auto_temp = complet(copy.deepcopy(copy.deepcopy(auto)))
    ecriture_tableau(auto_temp, 'execution/Automate_' + str(number) + '-Complet.txt', "Automate Complet: ")

    "----------------------------------------------------------------------------------"
    auto_temp = minimiser_automate(copy.deepcopy(auto))
    ecriture_tableau(auto_temp, 'execution/Automate_' + str(number) + '-Minimise.txt', "Automate Minimise: ")

    "----------------------------------------------------------------------------------"
    auto_temp = complementarisation_automate(copy.deepcopy(auto))
    ecriture_tableau(auto_temp, 'execution/Automate_' + str(number) + '-LanguageComplementaire.txt', "Automate Complémentarise: ")

    """
    debug temporaire
    
    print('############# Automate' + str(number) + '#######################')
    auto = lire_fichier_transition("automates/automate" + str(number) + ".txt")
    afficher_table_transition(auto)

    print('--------------------standard-------------------------------')
    auto_temp = standardiser_automate(copy.deepcopy(auto))
    afficher_table_transition(auto_temp)

    print('--------------------deter-------------------------------')
    auto_temp = determiniser_automate(copy.deepcopy(auto))
    afficher_table_transition(auto_temp)

    print('--------------------complet-------------------------------')
    auto_temp = complet(copy.deepcopy(copy.deepcopy(auto)))
    afficher_table_transition(auto_temp)

    print('--------------------mini-------------------------------')
    auto_temp = minimiser_automate(copy.deepcopy(auto))
    afficher_table_transition(auto_temp)

    print('--------------------complement-------------------------------')
    auto_temp = complementarisation_automate(copy.deepcopy(auto))
    afficher_table_transition(auto_temp)
    """



# Début du programme

if __name__ == "__main__":
    G = []
    menu = 0
    AutomataNb = 5

    """
    Création du dossier 'execution' s'il n'existe pas pour stocker les fichiers des opération effectué sur l'automate
    """
    if not (os.path.exists(str(os.path.dirname(os.path.abspath(__file__))) + '\execution')): # vérification si le chemin du dossier n'existe pas
        # Nom du fichier à créer
        directory = "execution"

        # Chemin du répertoire actuel
        parent_dir = str(os.path.dirname(os.path.abspath(__file__)))

        # combinaison et création
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)

    """
    Permet de générer la trace de l'exécution de toutes les opérations sur les automates
    """
    for i in range(1, 45):
        if i in (31,32,33,34,35): # ici, on ne fait pas ces états car automates avec epsilon
            continue
        generate_automate(i)

    while G == []:
        G = lire_fichier_transition("automates/automate"+str(AutomataNb)+".txt")

    while (menu != 10):
        print("""\n###################           Menu Principal           ###################
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
            AutomataNb = safe_input("\nChoisir un automate (1 à 30)\n", 1, 39)
            G = lire_fichier_transition("automates/automate"+str(AutomataNb)+".txt")

        elif menu == 3:
            if automate_standard(G) :
                print("L'automate est standard")
            else:
                print("L'automate n'est pas standard")

            if automate_determine(G) :
                print("L'automate est deterministe")
            else:
                print("L'automate n'est pas deterministe")

            if verif_complet(G) :
                print("L'automate est complet")
            else:
                print("L'automate n'est pas complet")

        elif menu == 4:
            G = standardiser_automate(G)
            ## écriture du résultat dans le fichier txt
            ecriture_tableau(G, 'execution/Automate_' + str(AutomataNb) + '-Standardise.txt', "Automate Standardise: ")
            afficher_table_transition(G)
            # fonction pour reconnaitre un mot

        elif menu == 5:
            G = determiniser_automate(G)
            ## écriture du résultat dans le fichier txt
            ecriture_tableau(G, 'execution/Automate_' + str(AutomataNb) + '-Determinise.txt', "Automate Determinise: ")
            afficher_table_transition(G)
            # fonction pour reconnaitre un mot

        elif menu == 6:
            G = complet(G)
            ## écriture du résultat dans le fichier txt
            ecriture_tableau(G, 'execution/Automate_' + str(AutomataNb) + '-Complet.txt', "Automate Complet: ")
            afficher_table_transition(G)
            # fonction pour reconnaitre un mot

        elif menu == 7:
            G = minimiser_automate(G)
            ## écriture du résultat dans le fichier txt
            ecriture_tableau(G, 'execution/Automate_' + str(AutomataNb) + '-Minimise.txt', "Automate Minimise: ")
            afficher_table_transition(G)
            # fonction pour reconnaitre un mot

        elif menu == 8:
            G = complementarisation_automate(G)
            # écriture du résultat dans le fichier txt
            ecriture_tableau(G, 'execution/Automate_' + str(AutomataNb) + '-LanguageComplementaire.txt', "Automate Complémentarise: ")
            afficher_table_transition(G)
            # fonction pour reconnaitre un mot

        ## elif menu == 9:
            # fonction pour reconnaitre un mot


        else:
            menu = 10
            print("Merci de votre utilisation, à bientôt !")
            break