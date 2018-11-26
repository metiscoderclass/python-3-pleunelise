#overhoor progamma
import random
woorden = {} #INLEZEN ALS .TXT BESTAND!!!!!!

w = 50
def print_schermbreedte():
    print("="* w)

def main():
    print_schermbreedte()
    print("Welkom bij het overhoor progamma!")
    print("bekijk lijst, toets b")
    print("nieuwe lijst, toets n")
    print("wijzig lijst, toets w")
    print("overhoor lijst, toets o")
    print("Om te stoppen, toets s")
    print_schermbreedte()
    keuze = input("Wat zou u willen doen?")

    while keuze != 's':
        if (keuze == 'b'):
            bekijk_lijst()
        if (keuze == 'n'):
            nieuwe_lijst()
        if (keuze == 'w'):
            wijzig_lijst()
        if (keuze == 'o'):
            overhoren_lijst()
        print_schermbreedte()
        keuze = input("Wat zou u willen doen?")

def bekijk_lijst():
    print_schermbreedte()
    print("NL : EN")
    for key in woorden:
        print("{key} : {value}".format(key=key, value=woorden[key])) #print 'key : value'

def nieuwe_lijst():
    print_schermbreedte()
    print("Laten we beginnen!")

    while w == 50:
        key = input("ne:") #input nederlands woord
        if key == 's':
            print("Je lijst is klaar!")
            opslaan()
            main()
        value = input("en:") #input engelse vertaling
        woorden[key] = value #slaat key en value op in dict
    opslaan()
    print("Je bent klaar met je lijst!")
    print("Als je nog meer woorden wilt toevoegen, kan dat in het menu")

def opslaan():
    print_schermbreedte()
    f = open('woorden.txt', 'w')
    f.write(str(woorden)) #schrijft de woorden als string weg
    f.close()
    print("Woorden als .txt bestand opgelagen")

def wijzig_lijst():
    bekijk_lijst()
    print_schermbreedte()
    ant = input("'Key' of 'value' veranderen:")
    if ant == 'key':
        print_schermbreedte()
        key = input("Woord dat je wilt veranderen:") #input van de key die veranderd wilt worden
        newkey = input("Nieuw woord:") #nieuwe key woord
        woorden[newkey] = woorden.pop(key) #veranderd de oude key door de nieuwe key
    elif ant == 'value':
        print_schermbreedte()
        value = input("Woord dat je wilt veranderen:") #input van de value die veranderd wilt worden
        newvalue = input("Nieuw woord:") #veranderd oude value voor de nieuwe value
        woorden[newvalue] = woorden.pop(value) #KeyError: value oude woord
    else:
        print_schermbreedte()
        print("Geen geldige key/value.") #print... als er geen geldige input gegeven wordt != 'key' or 'value'

def overhoren_lijst():
    punten = 0
    while punten < woorden.keys()*2:
        print_schermbreedte()
        nlwoord = random.choice(list(woorden)) #geeft een random key, in dit geval een nederlands woord
        print("Wat is de vertaling van dit woord?")
        enwoord = input(nlwoord + ":") #vraagt de engelse vertaling van het gevraagde nederlandse woord
        if (enwoord == woorden[nlwoord]): #kijkt of de gegeven value bij de random key hoort
            print("GOED!!")
            punten += 1
        elif (enwoord == 's'): #kijkt of de input 's' is
            main() #returnt als de input 's' is
        else:
            print("Dat is niet correct!") #als er een andere input is die niet gecontroleerd wordt, wordt het fout gerekend
            print("Het goede antwoord:",woorden[nlwoord]) #print het goede antwoord
            punten -= 1

main()
'''
   - nieuwe woordenlijst maken
   - veranderen van woordenlijst
   - woorden toevoegen aan een woordenlijst
   - woordenlijsten overhoren
   - stoppen met het programma
'''
