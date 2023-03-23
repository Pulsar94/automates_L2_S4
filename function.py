from copy import deepcopy
import complet as comp
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
            if i[0] == j:

                if not i[1] in sortie:
                    sortie[i[1]] = []

                if i[3] == "O" or i[3] == "IO":
                    sort = True

                sortie[i[1]].append(i[2])

    return sortie, sort
        

def determiniser_automate(G):
    if automate_determine(G):
        return G
    
    inputID = ""
    newG = [] # Notre nouvelle automate
    recursiveTable = []
    outputTable = []
    
    for input in G: # on identifie toute les entrées
        if input[3] == 'I' or input[3] == "IO":
            inputID = inputID + input[0] + "/" # On ajoute a notre string la valeur de l'entrée (en retirant le q initial pour simplifier le processus)
    
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
            
            newG.append(["".join(i.split("/")),j,"".join(joined.split("/")),(output and "O") or "-"]) #On ajoute a notre nouvel automate les nouveau noeud/lien

    if newG[0][3] == 'O':# La première entrée est forcément l'unique entrée dans un automate determinisé
        newG[0][3] = "I" 
    else:
        newG[0][3] = "IO" 
    
    return newG

def complementarisation_automate(G):
    comp.complet(G)
    complet = []
    for i in G:
        if not i[0] in complet:
            if i[3] == 'O':
                i[3] == '-'
            elif i[3] == 'IO':
                i[3] == 'I'
            else:
                i[3] == 'O'
            complet.append(i[0])
    return G

def get_group_adc(G,num): #Retourne le groupe auquel le num pointe
    for i in G:
        for j in G[i]:
            if num == j:
                return i
    return "P"

def rassembler_automate(G):
    transG = deepcopy(G)
    """
    #On traite un dic de type:

     {
        P:{
            P:[P,P,P]
        },
        I:{
            0:[4,5,1],
            1:[5,4,0]
        },
        II:{
            2:[0,P,3],
            3:[1,P,6],
            6:[O,P,3]
        },
        III:{
            4:[0,3,5],
            5:[1,2,4]
        }
     }
    """
    for i in G: #On remplace dans notre second dic les valeurs par leurs groupe équivalent
        for j in G[i]:
            for g in range(len(G[i][j])):
                transG[i][j][g] = get_group_adc(G,G[i][j][g])
    
    """
    # Désormais on traite un dic de type:

     {
        P:{
            P:[P,P,P]
        },
        I:{
            0:[III,III,I],
            1:[III,III,I]
        },
        II:{
            2:[I,P,II],
            3:[I,P,II],
            6:[I,P,II]
        },
        III:{
            4:[I,II,III],
            5:[I,II,III]
        }
     }
    """
    transG2 = {}
    state = "O/I/II/III/IV/V/VI/VII/VIII/IX/X/XI/XII/XIII/XIV/XV".split("/")
    count = -1
    toPop = []
    change = False
    for i in transG:
        for j in transG[i]:
            
            if not j in toPop:
                count = count + 1
                if not state[count] in transG2:
                    transG2[state[count]] = {}
                    
                for g in transG[i]:
                    if not j==g and not j in toPop and not g in toPop:
                        identical = True
                        for index in range(len(transG[i][j])):
                            #print(f'{transG[i][j]}||||{transG[i][g]}')
                            if transG[i][j][index] != transG[i][g][index]:
                                identical = False
                                change = True
                        
                        if identical:
                            transG2[state[count]][g] = G[i][g]
                            toPop.append(g)
                        
                transG2[state[count]][j] = G[i][j]
                toPop.append(j)

    return transG2, change

def minimiser_automate(G):
    tempG, newG = {}, []
    needMinimized = True
    transIndex = []
    # Pour minimiser il faut s'assurer que l'automate est bien determiné
    G = determiniser_automate(G)

    # Pour minimiser il faut s'assurer que l'automate est bien complet
    G = comp.complet(G)

    # On récupère tout les indices de transition pour la restoration
    for i in G:
        if i[0] == G[0][0]:
            transIndex.append(i[1])

    # Et il faut s'assurer que l'automate est bien complété
    tempG["N"]={}
    tempG["NT"]={}
    for i in G: #On recupère tout les noeuds donnant un T
        if i[3] == 'O' or i[3] == 'IO':
            tempG["N"][i[0]] = [j[2] for j in G if i[0]==j[0] and j[1] != '-']
        else:
            tempG["NT"][i[0]] = [j[2] for j in G if i[0]==j[0] and j[1] != '-']
    while needMinimized: #On minimise jusqu'a qu'on ne le puisse plus
        tempG, needMinimized = rassembler_automate(tempG)

    alreadyOutput = []
    # Restoration
    for i in tempG:
        value = 0
        for j in tempG[i][list(tempG[i].keys())[0]]:
            output = '-'
            for g in G:
                if (g[3] == 'I' or g[3] == 'IO') and g[0] not in alreadyOutput:
                    for j2 in tempG[i]:
                        for g2 in tempG[i][j2]:
                            if g[0] in g2:
                                output = 'I'
                                alreadyOutput.append(g[0])
                if g[3] == 'O' and g[0] not in alreadyOutput:
                    for j2 in tempG[i]:
                        for g2 in tempG[i][j2]:
                            if g[0] in g2:
                                if output == 'I':
                                    output = 'IO'
                                else:
                                    output = 'O'
                                alreadyOutput.append(g[0])
            newG.append([i,transIndex[value],get_group_adc(tempG, j),output])
            value = value + 1


    return newG