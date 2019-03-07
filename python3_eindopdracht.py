#overhoor progamma
import random
import time
def print_schermbreedte():
    print("="* 50)

def print_header():
    print_schermbreedte()
    print("Welkom bij het overhoor progamma!")
    print("bekijk lijst, toets b")
    print("nieuwe lijst, toets n")
    print("wijzig lijst, toets w")
    print("overhoor lijst, toets o")
    print("Om te stoppen, toets q")
    print_schermbreedte()

def main():
    print_header()
    keuze = input("Wat zou u willen doen?") #vraagt keuze input
    woorden = {}
    while keuze != 'q': #zolang de keuze geen 's' is blijft de loopen
        if (keuze == 'b'):
            bekijk_lijst(woorden)
        if (keuze == 'n'):
            woorden = nieuwe_lijst(woorden)
        if (keuze == 'w'):
            wijzig_lijst(woorden)
        if (keuze == 'o'):
            overhoren_lijst(woorden)
        print_schermbreedte()
        keuze = input("Wat zou u willen doen?")


def bekijk_lijst(woorden):
    print_schermbreedte()
    print("NL : EN") #key == NL, value == EN
    for key in woorden: #voor elke key in de dict woorden, voer deze loop uit
        print("{key} : {value}".format(key=key, value=woorden[key])) #print 'key : value'

def nieuwe_lijst(woorden):
    print_schermbreedte()
    print("'s' om te stoppenn")
    print("Laten we beginnen!")
    woorden = {}

    key = input("ne:")
    while key != "s": #loopt zolang w gelijk is aan 50
        value = input("en:") #input engelse vertaling
        woorden[key] = value #slaat key en value op in dict
        key = input("ne:")
    f = open('woorden.txt', 'w')
    for key in woorden: #loopt het x keer x = aantal keys
        f.write(key + ':' + value)
    f.close()
    print("Je bent klaar met je lijst!")
    print("Als je nog meer woorden wilt wijzigen, kan dat in het menu")
    return woorden

def opslaan(woorden):
    print_schermbreedte()
    f = open('woorden.txt', 'w')
    for key, value in woorden:
        f.write(key + ':' + value)
    f.close()
    print("Woorden als .txt bestand opgelagen")

def wijzig_lijst(woorden):
    bekijk_lijst(woorden)
    print_schermbreedte()
    key = input("Woord (NL) dat je wilt veranderen:") #input van de key die veranderd wilt worden
    newkey = input("Nieuw woord:") #nieuwe key woord
    newvalue = input("Nieuwe vertaling:") #veranderd oude value voor de nieuwe value
    woorden[newkey] = newvalue
    del woorden[key]
    print("De nieuwe wijziging is aangebracht in je woorden lijst!")
    return woorden

def verwijder_woord(woorden):
    bekijk_lijst(woorden)
    print_schermbreedte()
    key = input("Woord (NL) die je wilt verwijderen:") #input van de key die verwijderdt wilt worden
    vraag = input("Weet je zeker dat je dit woord wilt verwijderen?(ja/nee)")
    if (vraag == 'ja'):
        del woorden[key]
    return woorden

def overhoren_lijst(woorden):
    punten = 0
    while punten < len(woorden.keys())*2:
        print_schermbreedte()
        nlwoord = random.choice(list(woorden)) #geeft een random key, in dit geval een nederlands woord
        print("Wat is de vertaling van dit woord?")
        enwoord = input(nlwoord + ":") #vraagt de engelse vertaling van het gevraagde nederlandse woord
        if (enwoord == woorden[nlwoord]): #kijkt of de gegeven value bij de random key hoort
            print("GOED!!")
            punten += 1
        elif (enwoord == 's'): #kijkt of de input 's' is
            break #RECURSIE
        else:
            print("Dat is niet correct!") #als er een andere input is die niet gecontroleerd wordt, wordt het fout gerekend
            print("Het goede antwoord:",woorden[nlwoord]) #print het goede antwoord
            punten -= 1
    print("Je bent klaar!!", "Aantal punten:", punten)

main()
