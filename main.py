"""
Nom du projet : Traitement d’automate fini
Auteurs : Thibaut MENIN - Tao SOLAN – Quentin ADELINE – Marc ROUGAGNOU – Soazic FOURNIER
"""
'''
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
'''

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

def safe_input(y, mini1, maxi1, mini2, maxi2):
    while True:
        try:
            x = int(input(y))
            while (x < mini1 or x > maxi1 or (x in (31, 32, 33, 34, 35))):
                if mini2 =="" or maxi2 == "":
                    x = int(input(
                        "\n\n################   Choisir un nombre entier de {} à {} :   ################\n\n".format(mini1, maxi1)))
                else:
                    x = int(input(
                        "\n\n################   Choisir un nombre entier de {} à {} et {} à {} :   ################\n\n".format(mini1, maxi1, mini2, maxi2)))
            break
        except ValueError:
            if mini2 == "" or maxi2 == "":
                x = int(input(
                    "\n\n################   S'il vous plait, entrer un entier situer de {} à {} :   ################\n\n".format(mini1,
                                                                                                                 maxi1)))
            else:
                x = int(input(
                    "\n\n################   S'il vous plait, entrer un entier situer de {} à {} et {} à {} :   ################\n\n".format(
                        mini1, maxi1, mini2, maxi2)))
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


def menu_general():
    # for cle, valeur in menu_dic.items():
    #    print(str(cle) + " : " + str(valeur))

    G = []
    AutomataNb = 5
    choice = 12
    choice2 = 12

    while G == []:
        G = lire_fichier_transition("automates/automate"+str(AutomataNb)+".txt")

    # Dictionnaire du menu principal
    menu_dic_init = {1: "Afficher l'automate sous forme de tableau",
                     2: "Afficher l'automate sous forme graphique",
                     3: "Charger un automate",
                     4: "Informations sur l'automate",
                     5: "Opération sur l'automate",
                     6: "Reconnaissance de mots",
                     0: "Quitter le programme"}

    # Dictionnaire du menu sur les opérations
    menu_dic_ope = {1: "Afficher l'automate sous forme de tableau",
                    2: "Standardisation",
                    3: "Determination",
                    4: "Compléter",
                    5: "Minimisation",
                    6: "Langage complementaire",
                    0: "Retour au menu principal"}

    while choice != 0: # Boucle du menu principal avec ses conditions
        print("\n########################        Menu Principal        ########################\n")
        print("L'automate chargé est l'automate n°{}\n".format(AutomataNb))

        for i in range(7):
            print(str(i) + " : " + menu_dic_init.get(i))
        choice = safe_input("\nChoisir une fonction: ", 0, 6,"","")

        if choice == 1: # Afficher l'automate sous forme de tableau
            print("\n-------------- Table de transition de l'automate n°{} --------------".format(AutomataNb))
            afficher_table_transition(G)
            print("--------------------------------------------------------------------")

        elif choice == 2: # Afficher l'automate sous forme graphique
            Graphe = tableau_to_graphe(G)
            affichage_automate_graphe(Graphe)

        elif choice == 3: # Charger un automate
            G = []

            AutomataNb = safe_input("\nChoisir un automate situer de 1 à 30 et 36 à 44\n", 1, 30, 36, 44)
            G = lire_fichier_transition("automates/automate" + str(AutomataNb) + ".txt")

        elif choice == 4: # Informations sur l'automate
            print("\n--------------------------------------------------------------------")
            if automate_standard(G):
                print("L'automate est standard")
            else:
                print("L'automate n'est pas standard")

            if automate_determine(G):
                print("L'automate est deterministe")
            else:
                print("L'automate n'est pas deterministe")

            if verif_complet(G):
                print("L'automate est complet")
            else:
                print("L'automate n'est pas complet")
            print("--------------------------------------------------------------------")

        elif choice == 5: # Opération sur l'automate

            while choice2 != 0: ################# Boucle du menu secondaire avec ses conditions #################

                print("\n########################    Opération sur les automates     ########################\n")
                print("L'automate chargé est l'automate n°{}\n".format(AutomataNb))

                for i in range(7):
                    print(str(i) + " : " + menu_dic_ope.get(i))
                choice2 = safe_input("\nChoisir une fonction: ", 0, 6, "", "")

                if choice2 == 1: # Afficher l'automate sous forme de tableau
                    print("\n-------------- Table de transition de l'automate n°{} --------------".format(AutomataNb))
                    afficher_table_transition(G)
                    print("--------------------------------------------------------------------")

                elif choice2 == 2: # Standardisation
                    G = lire_fichier_transition("automates/automate" + str(AutomataNb) + ".txt")
                    G = standardiser_automate(G)
                    print("\n--------------------- Automate n°{} standardisé ---------------------".format(AutomataNb))
                    afficher_table_transition(G)
                    print("-----------------------------------------------------------------------")

                elif choice2 == 2: # Determination
                    G = lire_fichier_transition("automates/automate" + str(AutomataNb) + ".txt")
                    G = determiniser_automate(G)
                    print("\n--------------------- Automate n°{} déterministe ---------------------".format(AutomataNb))
                    afficher_table_transition(G)
                    print("------------------------------------------------------------------------")

                elif choice2 == 3: # Compléter
                    G = lire_fichier_transition("automates/automate" + str(AutomataNb) + ".txt")
                    G = complet(G)
                    print("\n--------------------- Automate n°{} complet ---------------------".format(AutomataNb))
                    afficher_table_transition(G)
                    print("-------------------------------------------------------------------")

                elif choice2 == 4: # Minimisation
                    G = lire_fichier_transition("automates/automate" + str(AutomataNb) + ".txt")
                    G = minimiser_automate(G)
                    print("\n--------------------- Automate n°{} minimisé ---------------------".format(AutomataNb))
                    afficher_table_transition(G)
                    print("--------------------------------------------------------------------")

                elif choice2 == 5: # Langage complementaire
                    G = lire_fichier_transition("automates/automate" + str(AutomataNb) + ".txt")
                    G = complementarisation_automate(G)
                    print("\n-------------- Automate complémentaire de l'automate n°{}  --------------".format(AutomataNb))
                    afficher_table_transition(G)
                    print("---------------------------------------------------------------------------")

                elif choice2 == 0: # Retour au menu principal
                    print("Retour au menu principal...")

            #################### Fin du menu secondaire ####################

        elif choice == 6: # Reconnaissance de mots
            print("Opération toujours en cours de développement")

        elif choice == 0: # Quitter le programme
            print("Merci de votre utilisation, à bientôt !")
            return




################## Début du programme ##################

if __name__ == "__main__":

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

    menu_general()