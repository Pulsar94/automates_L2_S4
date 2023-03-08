#On vérifie que l'automate est standard ou non
# Rappel:
#   - Il est unitaire (un seul état initial)
#   - Il n'existe pas de transitions allant sur cet état initial

def automate_standard(G): # Vérifie si l'automate d'entrée est standard
    count, countindex = 0, None
    for input in G:
        
        if input[3] == 'I': # On compte le nombre d'entrée en indexifiant la dernière vue
            count += 1
            countindex = input[0]
        if count>1: # Si le compte est supérieur a 1 l'automate n'est pas standard
            return False

        if countindex and input[2] == countindex: # On inspecte que aucune noeud se dirige vers l'entrée
            return False

    return True

def standardiser_automate(G): # Fonction pour standardiser l'automate
    if automate_standard(G):
        return G
    
    Idest, dicInput, first = [], [], True # Idest : ID destination || dicInput : dictionary input || first : premier
    for input in G:
        if input[3] == 'I': #On collecte toute les entrées I pour les mettre dans notre dictionnaire a input
            dicInput.append(input[0])
            input[3] = '-'
        
        if input[0] in dicInput: # On collecte toute les destinations de nos entrées
            Idest.append({input[2]:input[1]})

    for addition in Idest: # A partir de notre liste de destination on crées notre noeud I qui va tous les servirs
        for k in addition:
            G.append(['i', addition[k], k, (first and 'I') or '-'])
            first = False # On ne veut créer qu'un seul paramètre i input
    
    return G
