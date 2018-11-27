#overhoor progamma
import random
woorden = {"hallo":"hello", "auto":"car", "wiskunde":"math"}

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
    print("Om te stoppen, toets q")
    print_schermbreedte()
    keuze = input("Wat zou u willen doen?") #vraagt keuze input

    while keuze != 'q': #zolang de keuze geen 's' is blijft de loopen
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
    print("NL : EN") #key == NL, value == EN
    for key in woorden: #voor elke key in de dict woorden, voer deze loop uit
        print("{key} : {value}".format(key=key, value=woorden[key])) #print 'key : value'

def nieuwe_lijst():
    print_schermbreedte()
    print("'s' om te stoppenn")
    print("Laten we beginnen!")

    while w == 50: #loopt zolang w gelijk is aan 50
        key = input("ne:") #input nederlands woord
        if key == 's': #als input s
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
    key = input("Woord (key) dat je wilt veranderen:") #input van de key die veranderd wilt worden
    newkey = input("Nieuw woord:") #nieuwe key woord
    woorden[newkey] = woorden[key] #veranderd de oude key door de nieuwe key
    print_schermbreedte()
    print(woorden[newkey])  #print de value die veranderd wilt worden
    newvalue = input("Nieuwe vertaling:") #veranderd oude value voor de nieuwe value
    woorden[newkey] = newvalue
    del woorden[key]
    print("De nieuwe wijziging is aangebracht in je woorden lijst!")

def overhoren_lijst():
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
            main() #returnt als de input 's' is
        else:
            print("Dat is niet correct!") #als er een andere input is die niet gecontroleerd wordt, wordt het fout gerekend
            print("Het goede antwoord:",woorden[nlwoord]) #print het goede antwoord
            punten -= 1
    print("Je bent klaar voor je toets!!")

main()
