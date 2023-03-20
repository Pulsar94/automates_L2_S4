import matplotlib.pyplot as plt
import networkx as nx
import function as fu


#lire un fichier texte et renvoie un double tableau de la forme :
def extraction_tableau(nom_fichier):
    with open(nom_fichier, 'r') as f:
        lines = f.readlines() # on lit le fichier

    # Création du tableau vide
    tab = [] 

    # Ajout des nœuds et des transitions
    for line in lines:
        src, label, dst, io = line.split() # on récupère les informations de la ligne
        tab.append([src, label, dst, io]) # on ajoute la transition

    return tab

# Affiche un tableau de transition avec en paramètre un double tableau de la forme :
def affichage_automate_tableau(tab):
    # Affichage du tableau
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            print(tab[i][j], end="\t") # on affiche la transition
        print()

#transforme un tableau de transition en graphe NetworkX
def tableau_to_graphe(tab):
    # Création du graphe
    G = nx.DiGraph()

    # Ajout des nœuds et des transitions
    for i in range(len(tab)):
        src, label, dst, io = tab[i] # on récupère les informations de la ligne
        G.add_edge(src, dst, label=label, io=io) # on ajoute la transition

    # Définition des couleurs des nœuds si le nœud est d'entrée (=I) mettre en vert, si le nœud est de sortie (=O) mettre en rouge, sinon mettre en bleu
    for n in G.nodes():
        if n == "O":
            G.nodes[n]['color'] = 'red' # on définit la couleur du nœud d'entrée
        elif n == "I":
            G.nodes[n]['color'] = 'green' # on définit la couleur du nœud de sortie
        else:
            G.nodes[n]['color'] = 'blue' # on définit la couleur des autres nœuds

    return G

#Affiche un graphe NetworkX avec des couleurs différentes pour les nœuds d'entrée, de sortie et normaux.
def affichage_automate_graphe(G):
    # Définition des couleurs des nœuds
    color_map = []
    for n in G.nodes():
        color_map.append(G.nodes[n]['color'])

    # Affichage du graphe
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color=color_map, edge_color='black', width=1, alpha=0.7)
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()

def ecriture_tableau(table, file_name, title):
    done, index, writing = [], [], f'{title} :\n\n'
    with open(f'resultat/{file_name}.txt','w') as f:
        for i in table:
            if not i[1] in index:
                index.append(i[1])
        print("IO|Name| ",end="")
        writing = writing + "IO|Name| "
        for i in index:
            print(i,end="  | ")
            writing = writing + f'{i}  | '
        print()
        writing = writing + "\n"
        for i in table:
            if not i[0] in done:
                done.append(i[0])
                print(f'{i[3]} | {i[0]}',end=' | ')
                writing = writing + f'{i[3]} | {i[0]} | '
                for g in table:
                    if g[0] == i[0]:
                        print(i[2],end=' | ')
                        writing = writing + f'{i[2]} | '
                print()
                writing = writing + "\n"
        f.write(writing)

if __name__ == "__main__":
    tableau = extraction_tableau("automate.txt") # on lit l'automate
    #affichage_automate_tableau(tableau) # on affiche le tableau
    #tableau = fu.minimiser_automate(tableau)
    #tableau2 = fu.determiniser_automate(tableau) # on déterminise l'automate

    ecriture_tableau(tableau, "test1", "Table determinee")

    #fu.rassembler_automate(table)

    #graphe = tableau_to_graphe(tableau) # on transforme le tableau en graphe
    #affichage_automate_graphe(graphe) # on affiche le graphe

    #graphe2 = tableau_to_graphe(tableau2) # on transforme le tableau en graphe
    #affichage_automate_graphe(graphe2) # on affiche le graphe


