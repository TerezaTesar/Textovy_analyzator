'''
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Tereza Tesar Ruzicka
email: tereza.ruza@gmail.com
discord: Tea #1877
'''

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. 
''',
'''
At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.
''',
'''
The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.
'''
]


#jmeno a heslo
cara = '=' * 60
print(cara)
uzivatele = ('bob', 'ann', 'mike', 'liz')

jmeno = input('Vlozte sve uzivatelske jmeno: ')

if jmeno not in uzivatele:
    print('Neregistrovany uzivatel')
    quit()

else:
    heslo = input('Vlozte heslo: ')

jmena_hesla = {}
jmena_hesla['bob'] = '123'
jmena_hesla['ann'] = 'pass123'
jmena_hesla['mike'] = 'password123'
jmena_hesla['liz'] = 'pass123'

#porovnat jestli uz.jmeno a heslo odpovida dvojici jmeno+heslo
uz_jmeno_heslo = {}
uz_jmeno_heslo[jmeno] = heslo
if uz_jmeno_heslo[jmeno] == jmena_hesla[jmeno]:
    print('Vitej uzivateli', jmeno)

else:
    print('Spatne heslo')
    quit()
print(cara)

#uprava textu na jednotlive sekce
texts1 = TEXTS[0]
texts2 = TEXTS[1]
texts3 = TEXTS[2]

#vyber textu
print('Zvolte blok textu:')
print(texts1, texts2, texts3)
cislo_bloku = {}
cislo_bloku[1] = texts1
cislo_bloku[2] = texts2
cislo_bloku[3] = texts3

print(cara)

blok = input('Cast textu cislo:')

if blok.isnumeric() == False:
    print('Mel jsi napsat cislo')
    quit()
else:
    blok_c = int(blok)
    if 1 <= blok_c <=3 :
        print(cislo_bloku[blok_c])
    else:
        print('Spatne cislo')
        quit()
        
print(cara)

#prace s textem
#pocet slov

vycistena_slova = []

for slovo in (cislo_bloku[blok_c]).split():
    ciste_slovo = slovo.strip('.,?!')
    vycistena_slova.append(ciste_slovo)

print('Pocet slov je:', len(vycistena_slova) )

#pocet slov s velkym pismenem

velka_pismena = []

for velke in vycistena_slova:
     if velke.istitle() == True:
        velka_pismena.append(velke)

print('Pocet slov s velkym pismenem je:', len(velka_pismena))

#pocet slov psany velkymi pismeny

cele_velke = []

for velke in vycistena_slova:
     if velke.isupper() == True:
        cele_velke.append(velke)

print('Pocet slov psanych velkym pismem je:', len(cele_velke))

#pocet slov psanych malymi pismeny

cele_male = []

for velke in vycistena_slova:
     if velke.islower() == True:
        cele_male.append(velke)

print('Pocet slov psanych jen malymi pismeny:', len(cele_male))

#pocet cifer

cifry = []

for velke in vycistena_slova:
     if velke.isnumeric() == True:
        cifry.append(velke)

print('Pocet pocet cisel je:', len(cifry))

#soucet cisel v textu
s = 0
for cislo in cifry:
    cislo_c = int(cislo)
    s = s + cislo_c

print('Soucet cisel v textu je:', s)

print(cara)

#sloupcovy graf delek slov
#spocitani  delky slov a serazeni slov
max_delka = 1
for slovo in vycistena_slova:
    delka = len(slovo)
    if delka > max_delka:
        max_delka = delka
       
delky_slov = []
for i in range(max_delka):
    delky_slov.append(0)

for delka in vycistena_slova:
    delka = len(delka)
    delky_slov[delka - 1] = delky_slov[delka - 1] + 1
       
    
#vypis do grafu

print('Graf cetnosti slov podle poctu pismen')
print(cara)
l='{len:<3}'.format(len='LEN')
o='{oc:^25}'.format(oc='OCCURENCES')
n='{nr:>3}'.format(nr='NR')
print(l,'|', o, '|', n)
print(cara)

pocet_hvezd = []

for i in delky_slov:
      x = 1
      for n in range(delky_slov[x]):
        pocet_hvezd.append('*')
        x = x + 1 
p = 1
while p <= max_delka:
        final1 = '{len:<3}'.format(len=p)
        final2 = '{oc:^25}'.format(oc='*' * (delky_slov[p -1]))
        final3 = '{nr:>3}'.format(nr=delky_slov[p -1])
        print(final1,'|', final2,'|', final3)
        p = p + 1



