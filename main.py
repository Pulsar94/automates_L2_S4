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

#Fonction qui affiche le tableau de transition sous forme souhaitée
def afficher_table_transition(transitions):
    # Création des entêtes
    entetes = ['\033[92m' +'I'+ '\033[0m'+'/'+'\033[91m'+'O'+'\033[0m'+'   ', 'Etat']
    symboles = sorted(list(set([t[2] for t in transitions if t[2] != '-']))) #ici on récupère les symboles
    entetes.extend(symboles) #ici on ajoute les symboles à la liste des entêtes
    entete_str = '{:<6}{:<9}'.format(*entetes[:2]) #ici on crée la première ligne du tableau
    for symbole in entetes[2:]:
        entete_str += '{:<6}'.format(symbole) #ici on crée la deuxième ligne du tableau
    #affichage de la première ligne du tableau en bleu
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
        # Affichage de la ligne en vert si c'est un état d'entrée
        if ligne[0] == 'I':
            print('\033[92m' + ligne_str + '\033[0m')
        # Affichage de la ligne en rouge si c'est un état de sortie
        elif ligne[0] == 'O':
            print('\033[91m' + ligne_str + '\033[0m')
        # Affichage de la ligne en normal sinon
        else:
            print(ligne_str)

#Fonction qui transforme le tableau de transition en graphe orienté 
def tableau_to_graphe(tableau):
    # Création du graphe
    G = nx.DiGraph()
    # Ajout des nœuds
    for transition in tableau:
        G.add_node(transition[1])
        G.add_node(transition[3])
    # Ajout des arcs
    for transition in tableau:
        G.add_edge(transition[1], transition[3], label=transition[2])
    # Ajout des couleurs
    for node in G.nodes:
        if node == 'E':
            G.nodes[node]['color'] = 'green'
        elif node == 'S':
            G.nodes[node]['color'] = 'red'
        else:
            G.nodes[node]['color'] = 'blue'
    return G

#Fonction qui affiche le graphe comme un automate 
def affichage_automate_graphe(G):
    # Création de la figure
    fig, ax = plt.subplots(figsize=(10, 10))
    # Création de la position des nœuds
    pos = nx.spring_layout(G)
    # Création des nœuds
    nx.draw_networkx_nodes(G, pos, node_color=[G.nodes[node]['color'] for node in G.nodes])
    # Création des étiquettes des nœuds
    nx.draw_networkx_labels(G, pos)
    # Création des arcs
    nx.draw_networkx_edges(G, pos)
    # Création des étiquettes des arcs
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'label'))
    # Affichage de la figure
    plt.show()


if __name__ == "__main__":
    tableau = lire_fichier_transition("automate.txt")  # on lit l'automate
    #afficher_tableau_transition(tableau)  # on affiche le tableau
    afficher_table_transition(tableau)  # on affiche le tableau de transition sous forme souhaitée
    graphe = tableau_to_graphe(tableau) # on transforme le tableau en graphe 
    affichage_automate_graphe(graphe) # on affiche le graphe
