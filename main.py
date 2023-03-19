import matplotlib.pyplot as plt
import networkx as nx

#Fonction qui lit le fichier et qui renvoie un tableau de transition
def lire_fichier_transition(nom_fichier):
    transitions = []
    with open(nom_fichier, 'r') as f:
        for ligne in f:
            ligne = ligne.strip()           #ici on enlève les espaces
            elems = ligne.split()           #ici on sépare les éléments
            etat_type = elems[0]            #ici on récupère le type d'état
            etat_actuel = elems[1]          #ici on récupère l'état actuel
            symbole = elems[2]              #ici on récupère le symbole
            etat_cible = elems[3]           #ici on récupère l'état cible
            transitions.append([etat_type, etat_actuel, symbole, etat_cible])
    return transitions

#Fonction qui affiche le tableau de transition
#def afficher_tableau_transition(tableau_transition):
    print("Etat\tSymbole\tEtat cible")
    for transition in tableau_transition:
        print(transition[0], "\t", transition[1], "\t", transition[2], "\t", transition[3])

def afficher_table_transition(transitions):
    # Création des entêtes
    entetes = ['I/O', 'Etat']
    symboles = sorted(list(set([t[2] for t in transitions if t[2] != '-']))) #ici on récupère les symboles
    entetes.extend(symboles) #ici on ajoute les symboles à la liste des entêtes
    entete_str = '{:<6}{:<9}'.format(*entetes[:2]) #ici on crée la première ligne du tableau
    for symbole in entetes[2:]:
        entete_str += '{:<6}'.format(symbole) #ici on crée la deuxième ligne du tableau
    print(entete_str)

    # Création des lignes pour chaque état 
    etats = sorted(list(set([t[1] for t in transitions]))) 
    for etat in etats: 
        ligne = ['-'] * len(entetes) 
        for t in transitions:
            if t[1] == etat:
                # Indication d'entrée ou de sortie
                if t[0] == 'I':
                    ligne[0] = 'I'
                elif t[0] == 'O':
                    ligne[0] = 'O'
                # État initial
                ligne[1] = etat
                # États cibles pour chaque symbole de transition
                if t[2] != '-':
                    index = entetes.index(t[2])
                    if ligne[index] == '-':
                        ligne[index] = t[3]
                    else:
                        ligne[index] += '/' + t[3]
        ligne_str = '{:<6}{:<9}'.format(*ligne[:2])
        for i in range(2, len(ligne)):
            ligne_str += '{:<6}'.format(ligne[i])
        print(ligne_str)

def tableau_to_graphe(tableau):
    G = nx.DiGraph()  # on crée un graphe orienté
    for i in range(len(tableau)): 
        if tableau[i][0] == "I":
            G.add_node(tableau[i][1], color="red")
        elif tableau[i][0] == "O":
            G.add_node(tableau[i][1], color="green")
        else:
            G.add_node(tableau[i][1], color="grey")
        if tableau[i][3] != "-":
            G.add_edge(tableau[i][1], tableau[i][3], label=tableau[i][2])
    return G

def affichage_automate_graphe(G):
    # On récupère la liste des couleurs des nœuds
    node_colors = [G.nodes[node]['color'] for node in G.nodes]
    # On récupère la liste des étiquettes des arcs
    edge_labels = {(u, v): d['label'] for u, v, d in G.edges(data=True)}
    # On récupère la liste des positions des nœuds
    pos = nx.spring_layout(G)
    # On affiche le graphe
    nx.draw(G, pos, with_labels=True, node_color=node_colors)
    # On affiche les étiquettes des arcs
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    # On affiche le graphe
    plt.show()

if __name__ == "__main__":
    tableau = lire_fichier_transition("automate.txt")  # on lit l'automate
    #afficher_tableau_transition(tableau)  # on affiche le tableau
    afficher_table_transition(tableau)  # on affiche le tableau de transition sous forme souhaitée
    graphe = tableau_to_graphe(tableau) # on transforme le tableau en graphe 
    affichage_automate_graphe(graphe) # on affiche le graphe
