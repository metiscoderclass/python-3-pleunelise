FUNCTIONS
    def kies_lijst():
​       lijst_naam = input("Kies de woorden lijst die je wilt zien:")
       return lijst_naam

    def lees_woordenlijst():
        bestandsnaam = input("Wat is de bestandsnaam?")
        with open(bestandsnaam) as b:
         bestandsdata = b.read()

        print(bestandsdata)

        Gebruikt: SCHEIDER
        Parameter: naam van het bestand waar de woordenlijst in staat
        Returnwaarde: een dictionary met woordparen

    def STANDAARD_LIJST():
        tekstbestand = input("Wat wil je als naam voor je nieuwe tekst bestand?")
        with open(tekstbestand) as b:
            bestandsdata = b.read().split('\n')

        for item in bestandsdata:
             if not item == '': # Sla lege regels over
                # Hieronder zie je hoe je de inhoud van een lijst met twee elementen aan twee variabelen kunt toekennen
                woord1, woord2 = item.split("=")

    def main():
        Laat een keuzemenu zien

         STANDAARD_LIJST()
         KIES_LIJST()
         TOEVOEGEN()
         OVERHOREN()
         STOPPEN()

        De gebruiker kan vervolgens steeds nieuwe keuzes blijven maken.

        Gebruikt: STANDAARD_LIJST, KIES_LIJST, TOEVOEGEN, OVERHOREN, STOPPEN, EXTENSIE
        Parameters: Geen
        Returnwaarde: Geen
​
    nieuwe_lijst_naam()

        Gebruikt: -
        Parameters: -
        Returnwaarde: de lijst_naam van de nieuw gekozen lijst
​
    overhoren(woordenlijst)
        Blijf woorden overhoren totdat de gebruiker aangeeft te willen stoppen.
​
        Gebruikt: STOPPEN
        Parameters: de woordenlijst die overhoord moet worden
        Returnwaarde: -
​
​
        Gebruikt: SCHERMBREEDTE
        Parameters: -
        Returnwaarde: -
​
    print_menu(lijst_naam)
        Print het (keuze)menu inclusief de geselecteerde lijst
​
        Gebruikt: SCHERMHOOGTE, SCHERMBREEDTE
        Parameters: De naam van de geselecteerde woordenlijst
        Returnwaarde: -
​
    schrijf_woordenlijst(bestandsnaam, woordenlijst)
        Schrijft de woordparen weg naar het bestand genaamd 'bestandsnaam'.
        De oude inhoud van het bestand wordt overschreven!
​
        Gebruikt: SCHEIDER
        Parameter: naam van het bestand waar de woordenlijst in geschreven wordt, woordenlijst die weggeschreven wordt
        Returnwaarde: -
​
    verwijder_woord(woord, woordenlijst)
        Vraagt of gebruiker zeker weet of er verwijderd moet worden.
        Verwijdert het woord en de vertaling uit de lijst als dit zo is.
​
        Gebruikt: -
        Parameters: het woord dat verwijderd moet worden, de woordenlijst waaruit verwijderd moet worden
        Returnwaarde: -
​
    voeg_woorden_toe(woordenlijst, lijst_naam)
        Vraag de gebruiker steeds om woordenparen en voeg ze toe aan de lijst.
        Stop als de gebruiker aangeeft te willen stoppen.
​
        Gebruikt: SCHEIDER, STOPPEN
        Parameters: de woordenlijst waarin toegevoegd moet worden, de lijst_naam van deze woordenlijst
        Returnwaarde: -
​
DATA
    DELETE = 'd'
    EXTENSIE = '.wrd'
    KIES_LIJST = 'k'
    MAX_WOORDLENGTE = 20
    NIEUWE_LIJST = 'n'
    OPSLAAN = 'w'
    OVERHOREN = 'o'
    SCHEIDER = '='
    SCHERMBREEDTE = 80
    SCHERMHOOGTE = 40
    STANDAARD_LIJST = 'NED-EN'
    STOPPEN = 'q'
    TOEVOEGEN = 't'
