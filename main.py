import matplotlib.pyplot as plt
import networkx as nx


def lire_fichier_transition(nom_fichier):
    transitions = []
    with open(nom_fichier, 'r') as f:
        for ligne in f:
            ligne = ligne.strip()
            elems = ligne.split()
            etat_type = elems[0]
            etat_actuel = elems[1]
            symbole = elems[2]
            etat_cible = elems[3]
            transitions.append([etat_type, etat_actuel, symbole, etat_cible])
    return transitions

def afficher_tableau_transition(tableau_transition):
    print("Etat\tSymbole\tEtat cible")
    for transition in tableau_transition:
        print(transition[0], "\t", transition[1], "\t", transition[2], "\t", transition[3])

def afficher_table_transition(transitions):
    # Création des entêtes
    entetes = ['I/O', 'Etat']
    symboles = sorted(list(set([t[2] for t in transitions if t[2] != '-'])))
    entetes.extend(symboles)
    entete_str = '{:<6}{:<9}'.format(*entetes[:2])
    for symbole in entetes[2:]:
        entete_str += '{:<6}'.format(symbole)
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



# Transforme un tableau de transition de la fonction lire_fichier_transition("automate.txt") en graphe NetworkX 
# On change aussi la couleur des nœuds d'entrée(I) en vert,de sortie (O) en rouge et normaux(-) en gris
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


# Affiche un graphe NetworkX avec matplotlib 
def affichage_automate_graphe(G):
    # On récupère la liste des couleurs des nœuds
    node_colors = [G.nodes[node]['color'] for node in G.nodes]
    # On récupère la liste des étiquettes des arcs
    edge_labels = {(u, v): d['label'] for u, v, d in G.edges(data=True)}
    # On récupère la liste des positions des nœuds
    pos = nx.spring_layout(G)
    # On affiche le graphe
    nx.draw(G, pos, with_labels=True, node_color=node_colors)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()





if __name__ == "__main__":
    tableau = lire_fichier_transition("automate.txt")  # on lit l'automate
    afficher_tableau_transition(tableau)  # on affiche le tableau
    print("\n")
    afficher_table_transition(tableau)  # on affiche le tableau
    graphe = tableau_to_graphe(tableau) # on transforme le tableau en graphe 
    affichage_automate_graphe(graphe) # on affiche le graphe
