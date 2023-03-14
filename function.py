#On vérifie que l'automate est standard ou non
# Rappel:
#   - Il est unitaire (un seul état initial)
#   - Il n'existe pas de transitions allant sur cet état initial

def automate_standard(G): # Vérifie si l'automate d'entrée est standard
    count, countindex = 0, None
    for input in G:
        
        if input[3] == 'I' or input[3] == 'IO': # On compte le nombre d'entrée en indexifiant la dernière vue
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
    
    Idest, dicInput, first, in_out = [], [], True, False # Idest : ID destination || dicInput : dictionary input || first : premier
    for input in G:
        if input[3] == 'I' or input[3] == 'IO': #On collecte toute les entrées I pour les mettre dans notre dictionnaire a input
            if input[3] == 'IO':
                in_out = True
            dicInput.append(input[0])
            input[3] = '-'
        
        if input[0] in dicInput: # On collecte toute les destinations de nos entrées
            Idest.append({input[2]:input[1]})

    for addition in Idest: # A partir de notre liste de destination on crées notre noeud I qui va tous les servirs
        for k in addition:
            G.append(['i', addition[k], k, (first and in_out and 'IO') or (first and 'I') or '-'])
            first = False # On ne veut créer qu'un seul paramètre i input
    
    return G

#On vérifie que l'automate est determine ou non
# Rappel:
#   - Il est unitaire (un seul état initial)
#   - Il n'existe pas de transitions d'indice identique sur un noeud

def automate_determine(G):
    count = 0 # On reprend le code de vérification de l'automate standard
    indiceDic = {}
    for input in G:
        
        if input[3] == 'I' or input[3] == 'IO': # On compte le nombre d'entrée
            count += 1
        if count>1: # Si le compte est supérieur a 1 l'automate n'est pas determinée
            return False
        
        if not input[0] in indiceDic:
            indiceDic[input[0]] = []
        
        for indice in indiceDic[input[0]]:
            if indice == input[1]:
                return False
        
        indiceDic[input[0]].append(input[1])

    return True

def concateniser_automate_IO(G, ID): # Input ID des noeud, tableau général; permet de retourner toute les sortie regroupé d'un groupe d'indice et si ce groupe d'indice est une sortie
    sortie = {}
    sort = False
    for i in G:
        for j in ID.split("/"):
            if i[0] == "q"+j:

                if not i[1] in sortie:
                    sortie[i[1]] = []

                if i[3] == "O" or i[3] == "IO":
                    sort = True

                sortie[i[1]].append(i[2].split("q")[1])

    return sortie, sort
        

def determiniser_automate(G):
    if automate_determine(G):
        return G
    
    inputID = ""
    newG = [] # Notre nouvelle automate
    recursiveTable = []
    outputTable = []
    
    for input in G: # on identifie toute les entrées
        if input[3] == 'I' or i[3] == "IO":
            inputID = inputID + input[0].split("q")[1] + "/" # On ajoute a notre string la valeur de l'entrée (en retirant le q initial pour simplifier le processus)
    
    recursiveTable.append(inputID) # On créee une table qui va périodiquement s'aggrandir dans sa propre boucle pour s'assurer que tout les cas de notre nouvel automate soit pris en compte

    for i in recursiveTable: # On boucle notre table
        tempTable, output = concateniser_automate_IO(G, i) #On lance une fonction qui nous donne tout les indices de sortie rassemblée (+ si leurs noeud est une sortie)

        for j in tempTable: # On boucle dans nos indices de sortie rassemblée

            joined = ""
            alreadyjoined = []
            for join in tempTable[j]: # Fonction similaire à "/".join(tempTable[j]) sauf que l'on s'assure qu'il n'y ait pas de doublon de jointure (ex: q0 a 1 et q1 a 1 donnerais q01 a 11 sans notre sécurité)
                if not join in alreadyjoined:
                    joined = joined + join + "/"
                    alreadyjoined.append(join)

            if not joined in recursiveTable: # Si l'on crée un nouveau noeud on s'assure de l'ajouter à notre Table de boucle qui traite tout les noeud présent et futur
                recursiveTable.append(joined)
            
            if output: # Verification pour s'assurer qu'il y ait qu'un seul "O" assigné a la première instance du noeud
                if i in outputTable:
                    output = False
                else:
                    outputTable.append(i)
            
            newG.append(["q"+"".join(i.split("/")),j,"q"+"".join(joined.split("/")),(output and "O") or "-"]) #On ajoute a notre nouvel automate les nouveau noeud/lien

    if newG[0][3] == 'O':# La première entrée est forcément l'unique entrée dans un automate determinisé
        newG[0][3] = "I" 
    else:
        newG[0][3] = "IO" 
    
    return newG