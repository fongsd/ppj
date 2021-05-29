#!/usr/bin/python3

import os
import re
import sys

if len(sys.argv) <= 1:
    exit("len argv <= 1")
    
regexp = r'<marka>\s*(\w+)\s*</marka>'
model = r'<model\s*>\s*(\w+)\s*</model>'
godina = r'<godina\s*>\s*(\w+)\s*</godina>'
diag = r'<diag\s*>\s*(\d+)</diag>'
kol = r'<kolicina>\s*(\d+)</kolicina>'
panel = r'<panel>\s*(VA|IPS|TN|LED)\-(UHD|HD)</panel>'
cena = r'<cena>\s*(\d+)\s*</cena>'

try:
    f = open("klk.txt", "r")
    content = f.read()
except:
    exit("fajl ne postoji")
    

s1 = re.compile(regexp)
s2 = re.compile(model)
s3 = re.compile(godina)
s4 = re.compile(diag)
s5 = re.compile(kol)
s6 = re.compile(panel)
s7 = re.compile(cena)


#print(content)
marke = []
marke = s1.findall(content)
modeli = s2.findall(content)
godine = s3.findall(content)
diagonale = s4.findall(content)
kolicine = s5.findall(content)
paneli = s6.findall(content)
cene = s7.findall(content)

#print(marke)
#print(modeli)
#print(godine)
#print(diagonale)
#print(kolicine)
#print(paneli)
#print(cene)
mapa = {}
lista = []
liste = []
#print(paneli)
for i in range(0, len(marke)-1):
    lista = []
    lista.append(modeli[i])
    lista.append(marke[i])
    lista.append(godine[i])
    lista.append(diagonale[i])
    lista.append(kolicine[i])
    lista.append(paneli[i])
    lista.append(cene[i])
    liste.append(lista)
    mapa[modeli[i]] = lista
    #print(len(godine))
#print(mapa)
#print(mapa)



#print(liste)
#a.sort(key = f)
#print(a)
#lista.sort(key = )
#liste.sort(key = liste[0])
#print(liste[0][2])
#liste = sorted(liste, key = f)
#print(liste)
#print(liste)
def f(x):
    if x != 0:
        return str(x) + " komada na stanju"
    else:
        return " nema na stanju"

#print(liste)
if sys.argv[1] == "-r":
    for i,j  in mapa.items():
        #print(j[1])
        if j[1] == sys.argv[2]:
                print(j[1], j[0], i, j[2] + "in", j[4],  j[5][0], j[5][1], f(int(j[3])))
            

