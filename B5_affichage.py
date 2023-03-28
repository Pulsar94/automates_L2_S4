"""
Auteurs : Thibaut MENIN - Tao SOLAN – Quentin ADELINE – Marc ROUGAGNOU – Soazic FOURNIER
"""

################## IMPORT ##################

import matplotlib.pyplot as plt
import networkx as nx
import B5_complet as comp
import B5_function as fu

############################################

#Fonction qui lit le fichier et qui renvoie un tableau de transition
def lire_fichier_transition(nom_fichier):
    transitions = []
    with open(nom_fichier, 'r') as f:
        for ligne in f:
            ligne = ligne.strip()           #ici on enlève les espaces
            elems = ligne.split()           #ici on sépare les éléments
            etat_type = elems[3]            #ici on récupère le type d'état
            etat_actuel = elems[0]          #ici on récupère l'état actuel
            symbole = elems[1]              #ici on récupère le symbole
            etat_cible = elems[2]           #ici on récupère l'état cible
            transitions.append([etat_actuel, symbole, etat_cible, etat_type])
    return transitions

#Fonction qui affiche le tableau de transition sous forme souhaitée
def afficher_table_transition(transitions):
    # Création des entêtes
    entetes = ['\033[92m' +'I'+ '\033[0m'+'/'+'\033[91m'+'O'+'\033[0m'+'   ', 'Etat']
    symboles = sorted(list(set([t[1] for t in transitions if t[1] != '-']))) #ici on récupère les symboles
    entetes.extend(symboles) #ici on ajoute les symboles à la liste des entêtes
    entete_str = '{:<6}{:<9}'.format(*entetes[:2]) #ici on crée la première ligne du tableau
    for symbole in entetes[2:]:
        entete_str += '{:<6}'.format(symbole) #ici on crée la deuxième ligne du tableau
    #affichage de la première ligne du tableau en bleu
    print(entete_str)


    # Création des lignes pour chaque état 
    etats = sorted(list(set([t[0] for t in transitions]))) 
    for etat in etats: 
        ligne = ['-'] * len(entetes) 
        for t in transitions:
            if t[0] == etat:
                # Indication d'entrée ou de sortie
                if t[3] == 'I':
                    ligne[0] = 'I'
                if t[3] == 'IO' :
                    ligne[0] = 'IO'
                elif t[3] == 'O':
                    ligne[0] = 'O'
                # État initial
                ligne[1] = etat
                # États cibles pour chaque symbole de transition
                if t[1] != '-':
                    index = entetes.index(t[1])
                    if ligne[index] == '-':
                        ligne[index] = t[2]
                    else:
                        ligne[index] += '/' + t[2]
        ligne_str = '{:<6}{:<9}'.format(*ligne[:2])
        for i in range(2, len(ligne)):
            ligne_str += '{:<6}'.format(ligne[i])
        # Affichage de la ligne en vert si c'est un état d'entrée
        if ligne[0] == 'I':
            print('\033[92m' + ligne_str + '\033[0m')
        # Affichage de la ligne en rouge si c'est un état de sortie
        elif ligne[0] == 'O':
            print('\033[91m' + ligne_str + '\033[0m')
        # Affichage de la ligne en jaune si c'est un état d'entrée et de sortie en bleu       
        elif ligne[0] == 'IO':
            print('\033[93m' + ligne_str + '\033[0m') 
        # # Affichage de la ligne en normal sinon
        else:
            print(ligne_str)

#Fonction qui transforme le tableau de transition en graphe orienté 
def tableau_to_graphe(tableau):
    G = nx.DiGraph()
    for t in tableau:
        if t[1] != '-':
            G.add_edge(t[0], t[2], label=t[1])
        if t[3] == 'I':
            G.nodes[t[0]]['color'] = 'green'
        elif t[3] == 'O':
            G.nodes[t[0]]['color'] = 'red'
        elif t[3] == 'IO':
            G.nodes[t[0]]['color'] = 'orange'

    return G

#Fonction qui affiche le graphe comme un automate 
def affichage_automate_graphe(G):
    pos = nx.spring_layout(G)
    # Affichage des états
    nx.draw_networkx_nodes(G, pos, node_color=[G.nodes[n].get('color', 'grey') for n in G.nodes])
    # Affichage des transitions
    nx.draw_networkx_edges(G, pos)
    # Affichage des étiquettes des transitions
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'label'))
    # Affichage des étiquettes des états
    nx.draw_networkx_labels(G, pos)
    plt.show()



#Fonction qui affiche le tableau de transition sous forme souhaitée dans un fichier texte et dans le terminal
def ecriture_tableau(transitions, file_name, title):
    # Création des entêtes Sans couleur pour le fichier texte
    entetes2 = ['I'+'/'+'O'+'   ', 'Etat']
    symboles = sorted(list(set([t[1] for t in transitions if t[1] != '-']))) #ici on récupère les symboles

    entetes2.extend(symboles)

    entete_str2 = '{:<6}{:<9}'.format(*entetes2[:2])
    for symbole in entetes2[2:]:
        entete_str2 += '{:<6}'.format(symbole)


    # ecriture dans le fichier texte
    file = open(file_name, "w")
    #ajout du titre en sorant une ligne vide
    file.write(title + "\n")
    file.write(entete_str2 + "\n")
    # Création des lignes pour chaque état
    etats = sorted(list(set([t[0] for t in transitions])))
    for etat in etats:
        ligne = ['-'] * len(entetes2)
        for t in transitions:
            if t[0] == etat:
                # Indication d'entrée ou de sortie
                if t[3] == 'I':
                    ligne[0] = 'I'
                if t[3] == 'IO' :
                    ligne[0] = 'IO'
                elif t[3] == 'O':
                    ligne[0] = 'O'
                # État initial
                ligne[1] = etat
                # États cibles pour chaque symbole de transition
                if t[1] != '-':
                    index = entetes2.index(t[1])
                    if ligne[index] == '-':
                        ligne[index] = t[2]
                    else:
                        ligne[index] += '/' + t[2]
        ligne_str = '{:<6}{:<9}'.format(*ligne[:2])
        for i in range(2, len(ligne)):
            ligne_str += '{:<6}'.format(ligne[i])

        #ecriture dans le fichier texte
        file.write(ligne_str+ "\n")

    #fermeture du fichier texte
    file.close()

