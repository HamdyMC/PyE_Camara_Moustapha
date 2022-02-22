import csv
liste=[]
base=csv.DictReader(open('Données Projet.xlsx - Feuil2.csv'))
print(base.fieldnames)
print(base)
for row in base:
    liste.append(row)
liste_v=[]#liste valide
liste_i_nu=[]#num inv
liste_i_p=[]#prenom inv
liste_i_n=[]#nom inv
liste_i_d=[]#date inv
liste_i_c=[]#class inv
for i in range(len(liste)):
    if len(liste[i]['Numero'])==7 and (liste[i]['Numero']).isalnum:
        liste_v.append(liste[i])
    else:
        liste_i_nu.append(liste[i])

#test prenom
for i in range(len(liste_v)):
    if len(liste_v[i]['PrÃ©nom'])<3 or type(liste[i]['PrÃ©nom'][1])!=str:
        liste_i_p.append(liste_v[i])
        del(liste_v[i])    
#test nom
for i in range(len(liste_v)):
    if len(liste_v[i]['Nom'])<2 or type(liste[i]['Nom'][0])!=str:
        liste_i_n.append(liste_v[i])
        del(liste_v[i])
#test date
for i in range(len(liste_v)):
    liste_v[i]['Date de naissance']=re.sub("\!|\-'|\?","",liste_v[i]['Date de naissance'])
    print(liste_v[i]['Date de naissance'])