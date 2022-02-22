#Test numero valide
def testnum(num):
    if num==7 and num.isalnum:
        return True
    else:
        return False
numero="AAAA001"
print(testnum(numero))

#test prenom
def testprenom(prenom):
    cpt=0
    if prenom[0].isalpha():
        for i in prenom:
            if i.isalpha():
                cpt+=1
        if cpt>=3:
            return True
        else:
            return False
    else:
        return False
Prénom="Moustapha"
Pre_2="a22s"
Pre_3="2aaaa"
print(Pre_2[0])
print(testprenom(Prénom))
print(testprenom(Pre_2))
print(testprenom(Pre_3))

#Test nom
def testnom(nom):
    cpt=0
    if prenom[0].isalpha():
        for i in prenom:
            if i.isalpha():
                cpt+=1
        if cpt>=2:
            return True
        else:
            return False
    else:
        return False

#traitement chaine date
import re
datenaiss="27/12/2020"
def correctdate(date):
    chaine=date.split("/")
    print(chaine)

correctdate(datenaiss)
print(datenaiss)

#Test date
#def testdate(date):
    #import datetime
date_string = '2002-02-14'

try:
    datetime.datetime.strptime(date_string, format)
    print("This is the correct date string format.")
except ValueError:
    print("This is the incorrect date string format. It should be YYYY-MM-DD")
    

#test notes pour extraire notes d'examens
chaine="Math[11;13:06] #Francais[08;17:12] #Anglais[13;13:12] #PC[09;18:07] #SVT[15;10:10] #HG[14;19:17]"
def testnote(notes):
    ne=[]
    notes=notes.split("#")
    for i in range(6):
            notes[i]=notes[i].split(":")
            notes[i]=(notes[i][1].split("]"))
            notes[i]=int(notes[i][0])
            print(notes[i])
            
    return notes
ne=testnote(chaine)
ne

#test notes pour extraire notes devoirs
chaine="Math[11;13:06] #Francais[08;17:12] #Anglais[13;13:12] #PC[09;18:07] #SVT[15;10:10] #HG[14;19:17]"
def testnote(notes):
    import statistics
    notes=notes.split("#")
    for i in range(6):
            notes[i]=notes[i].split(":")
            notes[i]=(notes[i][0].split(";"))
            notes[i][0]=notes[i][0].split("[")
            notes[i][0]=int(notes[i][0][1])
            notes[i][1]=int(notes[i][1])
            print(notes[i][0])
            print(notes[i][1])
            notes[i]=statistics.mean(notes[i])
            #notes[i][0]=notes[i][0].replace()
    return notes
nd=testnote(chaine)
nd

print(ne)
print(nd)
import statistics
moymat=[]

for i in range(6):
    moy=(2*ne[i]+nd[i])/3
    moymat.append(moy)
moymat
—------------------------------------------------------------------------------------------------------------




