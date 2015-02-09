# pinautomaat-shizzle
#maakt de functie main aan, deze kan je aanroepen door main()
def main():
    #zorgt ervoor dat de hiervoor gedefineerde variabelen exists en Bedragen in deze functie beschikbaar zijn
    global exists
    global Bedragen
    #roept de functie kies_speler aan en maakt speler gelijk aan wat de functie retourneert
    speler=kies_speler()
    #als de speler niet in de lijst exists voorkomt wordt hij eraan toegevoegd en wordt zijn bedrag gelijk aan 2500 gesteld
    if speler not in exists:
        #maakt het bedrag van de ingevulde speler 2500
        Bedragen[speler]=2500
        #voegt de speler toe aan de lijst exists
        exists+=[speler]
    #roept de functie kies_bedrag aan en zet bedrag gelijk aan de waarde die wordt geretourneerd
    bedrag=kies_bedrag()
    #als het bedrag groter is dan het bedrag dat de speler bezit wordt de functie error aangeroepen
    if bedrag>Bedragen[speler]:
        error(speler)
    #als het bedrag niet groter is dan het bedrag dat de speler heeft wordt het bedrag afgerekend door de functie
    #reken_bedrag_af aan te roepen en de parameters speler en bedrag mee te geven
    else:
        #maakt de dictionary Bedragen gelijk aan de dictionary die aan het eind van deze functie over is
        Bedragen=reken_bedrag_af(speler, bedrag)
#defineerd de functie kies_speler
def kies_speler():
    #dit is wel duidelijk denk ik
    print("Naam? ")
    #vraagt om input en maakt van de input een string
    Speler = str(input())
    #retourneerd de waarde Speler
    return Speler

def kies_bedrag():
    #probeert dit stukje code uit
    try:
        print("Aankoopbedrag? (bijvoorbeeld: 50, 100, etc.)")
        Aankoop = int(input())
        return Aankoop
    #als de error valueError optreed (het converteren van een string naar een int) springt hij eruit en
    #accepteerd de error en print dat het geen nummer is
    except ValueError:
        print('kies een nummer')
        #retouneerd een 0 anders komt er een error
        return 0
#defineerd de functie error en geeft de parameter speler mee
def error(speler):
    #print dat de specefieke speler meer probeerde uit te geven dan hij heeft
    print("{0} heeft meer uit proberen te geven dan hij bezit".format(speler))
    print("WTF DAT KAN HELEMAAL NIET")
#defineerd de functie  reken_bedrag_af en geeft de parameters Speler en bedrag mee in de functie
def reken_bedrag_af(Speler, bedrag):
    #haalt het bedrag van de spelers persoonlijke bedrag af
    Bedragen[Speler] -= bedrag
    #zegt wat de speler heeft uitgegeven, hoeveel hij nog over heeft en dat de transactie voltooid is
    print("Speler " + str(Speler) + " heeft " + str(bedrag) + " uitgegeven.")
    print("Speler " + str(Speler) + " heeft nog " + str(Bedragen[Speler]) + " over.")
    print("")
    print("----- Transactie voltooid! -----")
    print("")
    #retouneerd de dictionary Bedragen
    return Bedragen

#maakt de lijst exists, deze wordt gebruikt om bestaande spelers op te slaan zodat zij in het vervolg
#hun eigen saldo kunnen blijven gebruiken
exists=[]
#dit maakt een dictionary genaamd Bedragen
#voorbeeld van opgeslagen data in een dictionary:
#{'Tjeerd':2450)
#deze string (of stukje tekst) Tjeerd heeft als waarde 2450
#om deze waarde op te halen gebruik je:
#Bedragen['Tjeerd']
Bedragen={}
#maakt een infinite loop
#(dit valt niet aan te raden)
while(0==0):
    #roept de functie main aan
    main()
