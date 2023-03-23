
def alphabet_complet(automate):#récupérer l'alphabet de l'automate
    alphabet=[]
    i,j=0,0
    for i in range (len(automate)):
        lettre=automate[i][1]
        if lettre not in alphabet:
            alphabet.append(lettre)
    #alphabet sous forme ['b', 'a', 'd'] / soit les lettres correspondantes aux transitions
    fin=max(alphabet)
    let=97 #caractère ascii de 'a'
    while (let!=ord(fin)): #jusqu'à la dernière lettre de l'alphabet de transitions
        if chr(let) not in alphabet:
            alphabet.append(chr(let))
        let+=1
    return sorted(alphabet)  #obtention de l'aphabet dans l'odre jusqu'à la dernière lettre (meilleur lecture)

def recup_etat(automate): #récupération des états de l'automate sous forme de tableau
    etat=[]
    for i in range(len(automate)):
        if automate[i][0] not in etat: #on prend les états de départ de transition s'ils ne sont pas déjà ajoutés
            etat.append(automate[i][0])
        if automate[i][2] not in etat: #on prend les états de fin de transition s'ils ne sont pas déjà ajoutés
            etat.append(automate[i][2])
    return sorted(etat) #on ordonne les états (meilleur lecture)


def verif_complet(automate,complet=0): # vérifie si un automate donné en paramètre est complet
    alphabet=alphabet_complet(automate) #récupération de l'alphabet
    etat=recup_etat(automate) #récupération des différents états
    dic_alphabet={}
    i,j=0,0
    for i in range (len(alphabet)):
        dic_alphabet[alphabet[i]]='' #obtention du dictionnaire avec les lettres de l'alphabet
    for j in range (len(automate)):
        if automate[j][0] not in dic_alphabet[automate[j][1]]:
            dic_alphabet[automate[j][1]]+=automate[j][0] #remplissage du dictionnaire
    for k in etat:
        for m in alphabet:
            if k not in dic_alphabet[m]:
                if complet==0:
                    return False
                else:
                    return dic_alphabet,etat,alphabet #renvoie le dictionnaire si pas complet (sert pour complet(automate))
    return True


def complet(automate):#permet de compléter un automate
    if verif_complet(automate) ==True: # on vérifie s'il ne l'ai pas déjà
        return automate
    dic_alphabet,etat,alphabet=verif_complet(automate,1)#récupération des informations sur l'automate
    etat.append('P')
    for i in etat:
        for j in alphabet:
            if i not in dic_alphabet[j]:
                automate.append([i,j,'P','-']) #ajout des transitions à l'état 'poubelle' à l'automate
    TBD = []
    for i in range(len(automate)):
        if automate[i][0] == '-':
            TBD.append(i)
    
    removed = 0
    for i in TBD:
        del automate[i-removed]
        removed += 1
    return sorted(automate) #on retourne le tableau du nouvel automate