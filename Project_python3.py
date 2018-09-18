def main():
  print("Welkom bij het overhorings progamma!")
  print("Typ 'k' om een lijst te kiezen")
  print("Typ 'n' om een nieuwe lijst te maken")
  print("Typ 'l' om een lijst te lezen")
  print("Typ 't' om iets aan een lijst toe tevoegen")
  print("Typ 'q' om te stoppen")
  print("Typ 'o' om te overhoren")
  print("Typ 'd' om een lijst te verwijderen")
  keuze = input("Wat zou je willen doen?")

  if (keuze == 'k'):
    kies_lijst()
  if (keuze == 'n'):
    print("Veel plezier met het maken van je nieuwe lijst!")
    nieuwe_lijst()
  if (keuze == 'l'):
    lees_lijst()
  if (keuze == 't'):
    toevoegen_lijst()
  if (keuze == 'q'):
    antw = print("Weet je zeker dat je wilt stoppen?")
    if (antw == 'ja'):
      print("Tot de volgende keer!")
      #stop
  if (keuze == 'o'):
    print("Veel succes met oefenen!")
    overhoren_lijst()
  if (keuze == 'd'):
    print("Weet je zeker dat je deze lijst wilt verwijderen?")
    verwijderen_lijst()
