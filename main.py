import matplotlib.pyplot as plt
import networkx as nx

#lire l'automates et retourner un tableau 
def lire_automate(nom_fichier):
    """
    Lit un fichier texte décrivant un automate et renvoie un graphe NetworkX.
    """
    with open(nom_fichier, 'r') as f:
        lines = f.readlines()

    # Création du graphe
    G = nx.DiGraph()

    # Ajout des nœuds et des transitions
    for line in lines:
        src, label, dst, io = line.split()
        G.add_edge(src, dst, label=label)

        if io == "I":
            G.nodes[src]['color'] = 'green'
        elif io == "O":
            G.nodes[dst]['color'] = 'red'

    return G

#afficher l'automate sous forme de tableau de transition avec les etiquettes en colonnes et les étates de transition en lignes exemple :
#          a         b         
#    0         1         2
#    1         2         -
#    2         0         1

def affichage_automate_tableau(G):
    """
    Affiche un graphe NetworkX sous forme de tableau de transition.
    """
    # Récupération des états et des symboles
    states = sorted(G.nodes())
    symbols = sorted({d['label'] for u, v, d in G.edges(data=True)})

    # Affichage du tableau
    print(" " * 10, end="")
    for symbol in symbols:
        print(f"{symbol:10}", end="")
    print()
    for state in states:
        print(f"{state:10}", end="")
        for symbol in symbols:
            try:
                dst = next(v for u, v, d in G.edges(data=True) if u == state and d['label'] == symbol)
                print(f"{dst:10}", end="")
            except StopIteration:
                print(f"{'-':10}", end="")
        print()

#afficher l'automate sous forme de graphe
def affichage_automate_graphe(G):
    """
    Affiche un graphe NetworkX avec des couleurs différentes pour les nœuds d'entrée, de sortie et normaux.
    """
    # Définition des positions des nœuds
    pos = nx.spring_layout(G)

    # Définition des couleurs des nœuds
    node_colors = [G.nodes[n].get('color', 'blue') for n in G.nodes()]

    # Dessin du graphe
    nx.draw_networkx_nodes(G, pos, node_color=node_colors)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['label'] for u, v, d in G.edges(data=True)})

    # Affichage du graphe
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    G = lire_automate("automate.txt")
    affichage_automate_tableau(G)
    affichage_automate_graphe(G)
    