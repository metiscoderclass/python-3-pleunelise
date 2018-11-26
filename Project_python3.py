def print_schermbreedte():
    schermbreedte = 50
    print("="* schermbreedte)

def main():
    print_schermbreedte()
    print("Welkom bij het overhoor progamma!")
    print("'k' = kies lijst")
    print("'n' = nieuwe lijst")
    print("'l' = lees lijst")
    print("'o' = lijst overhoren")
    print("'d' = delete lijst")
    print_schermbreedte()
    keuze = input("Wat zou u willen doen?")

    if (keuze == 'k'):
        keuze_lijst()
    if (keuze == 'n'):
        print("Veel plezier met het maken van je nieuwe lijst!")
        nieuwe_lijst()
    if (keuze == 'l'):
        lees_lijst()
    if (keuze == 'o'):
        print("Veel succes met oefenen!")
        overhoren_lijst()
    if (keuze == 'd'):
        verwijder_lijst()
    if (keuze == 'q'):
        antw = input("Weet je zeker dat je wilt stoppen?")
        if (antw == 'ja'):
          stop()
          #break/return
        else:
             main() #los op met een while true loop

def lees_bestandsnamen():
    print(lijst_namen)
    return lijst_namen

def lees_lijst():
    #lijst = {}
    lees_bestandsnamen()
    bestandsnaam = input("Welk van deze bestanden wil je lezen?")
    with open(bestandsnaam) as f:
        for line in f:
          woord1, woord2 = line.strip(' ').split('=')
          bestandsnaam[woord1] = woord2
        print(bestandsnaam)
        return bestandsnaam
        f.close()
        print_schermbreedte()

def keuze_lijst():
    lijst = {}
    #lees_bestandsnamen()
    #bestandsnaam = input("Welk van deze bestanden wil je lezen?")
    f = open('woorden.txt')
    for line in f:
        woorden = line.strip(',')
        #woord1 = woorden.split(':')
        x = woorden.split(" ")
        woord1 = x[0]
        woord2 = x[1]
        lijst[woord1] = woord2
    print(lijst)
    return lijst
    f.close()
    '''
    input("Wat wil je doen met deze lijst?")
    keus = print("Kies uit: lezen, woord verwijderen, woorden toevoegen")
    if (keus == 'lezen'):
      lees_lijst()
    if (keus == 'verwijderen'):
      verwijder_woord()
    if (keus == 'toevoegen'):
      toevoegen_lijst()
    print_schermbreedte()
'''

def stop():
    print("Veel succes met je toets(en)!")


lijst_namen = []
def nieuwe_lijst():
    nieuwe_bestandsnaam = input("Wat wil je als naam voor je nieuwe bestand?")
    lijst_namen.append(nieuwe_bestandsnaam)
    nb = open(nieuwe_bestandsnaam, 'w') #'w' zorgt ervoor dat het bestand overschreven wordt
    print("Typ je woord in met een ' ' er tussen")
    print("Druk op enter om het op te slaan & typ 's' om te stoppen")
    print("Laten we beginnen!")

    max = 0
    while max < 50:
      line = input("ne eng:")
      if line == 's':
        nb.close()
        print("Je lijst is klaar!")
        main()
        woord1, woord2 = line.split(' ')
        woorden = [woord1, woord2]
        resultaat = "=".join(woorden)
        nb.write(resultaat)
        nb.write("/n")
        max +=1
    nb.close()
    print("Je bent klaar met je lijst!")
    print("Als je nog meer woorden wilt toevoegen kan dat in het menu")
    print_schermbreedte()

import os
def verwijder_lijst():
    lees_bestandsnamen()
    bestandsnaam = input("Welk bestand wil je verwijderen?")
    os.remove(bestandsnaam)
    print("Het bestand", bestandsnaam,"is verwijderd")
    print(bestandsnaam)
    lijst_namen.remove(bestandsnaam)
    print_schermbreedte()

keuze_lijst()
'''
MAX_WOORD_LENGTE = 14



def vertalen():
    woord = "vlieger"
    print_schermbreedte()
    vertaling = input("Wat is de vertaling van dit woord?" + ":" + " " + woord)
    print_schermbreedte()
    print(" Woord: {:14} Vertaling: {:13} ".format(woord, vertaling))

#keuze lijst
#inlezen lijst

#while punten < aantal woorden
#vraag vertaling woord (random)
#check input
# if goed punten +=1
# if fout punten -=1
# if input == 's' quit

def overhoren():
  lees_bestandsnamen()
  bestand = input("Welk bestand wil je overhoren?")
  bestand.read()
  return bestand

  for line in bestand:
    woord1, woord2 = line.strip(' ').split('=')
  punten = 0
  aantal = 0
  while bestand != "s":
    print("Geef de vertaling van het woord:")
    woord = input(woord1, ":")
    if woord == woord2:
      punten += 1
      aantal += 1
    if woord != woord2:
      aantal += 1
    if woord == "s":
      main()




print(vertalen())
d = ["a" , "b" , "c" , "d"]
resultaat = "-".join(d)
print (resultaat)

#count elementen in lijst
a = []
len(a)
if a is None:
#del lijst
'''
