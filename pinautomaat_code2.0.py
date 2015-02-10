# pinautomaat-shizzle
#als hij hier een error geeft: verrander de hoofdletter T naar een kleine t
from Tkinter import *

#maakt de functie main aan, deze kan je aanroepen door main()
def main():
    #zorgt ervoor dat de hiervoor gedefineerde variabelen exists en Bedragen in deze functie beschikbaar zijn
    global exists
    global Bedragen
    global popup
    while(0==0):
        #roept de functie kies_speler aan en maakt speler gelijk aan wat de functie retourneert
        speler=kies_speler()
        #als de speler niet in de lijst exists voorkomt wordt hij eraan toegevoegd en wordt zijn bedrag gelijk aan 2500 gesteld
        if speler not in exists:
            #maakt het bedrag van de ingevulde speler 2500
            Bedragen[speler]=2500
            Uitgaven[speler]=[]
            #voegt de speler toe aan de lijst exists
            exists+=[speler]
            popup=Tk()
            Label(popup, text='{0} is born now'.format(speler)).pack()
            Button(popup, text='got it', command=destroy_popup).pack()
            popup.mainloop()
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
    global vraag
    vraag=Tk()
    inputt=StringVar()
    #dit is wel duidelijk denk ik
    Label(vraag, text="Naam? ").pack()
    #vraagt om input en maakt van de input een string
    Entry(vraag, textvariable=inputt, fg='green').pack()
    Button(vraag, text='ok', command=destroy_vraag).pack()
    vraag.mainloop()
    Speler=inputt.get()
    #retourneerd de waarde Speler
    return Speler.lower()

def kies_bedrag():
    global besteding
    besteding=Tk()
    bedrag=IntVar()
    #probeert dit stukje code uit
    try:
        Label(besteding, text="Aankoopbedrag? ").pack()
        Entry(besteding, textvariable=bedrag, fg='red').pack()
        Button(besteding, text='done', command=destroy_besteding).pack()
        besteding.mainloop()
        Aankoop=int(bedrag.get())
        return Aankoop
    #als de error valueError optreed (het converteren van een string naar een int) springt hij eruit en
    #accepteerd de error en print dat het geen nummer is
    except ValueError:
        global error
        error=Tk()
        Label(error, text='kies een nummer').pack()
        Button(error, text='Het spijt me!', command=destroy_error).pack()
        error.mainloop()
        #retouneerd een 0 anders komt er een error
        return 0
    
#defineerd de functie error en geeft de parameter speler mee
def error(speler):
    global error
    error=Tk()
    #print dat de specefieke speler meer probeerde uit te geven dan hij heeft
    Label(error, text="{0} heeft meer uit proberen te geven dan hij bezit".format(speler)).pack()
    Button(error, text="WTF DAT KAN HELEMAAL NIET", command=destroy_error).pack()
    error.mainloop()
    
#defineerd de functie  reken_bedrag_af en geeft de parameters Speler en bedrag mee in de functie
def reken_bedrag_af(Speler, bedrag):
    global popup
    popup=Tk()
    #haalt het bedrag van de spelers persoonlijke bedrag af
    Bedragen[Speler] -= bedrag
    Uitgaven[Speler].append(bedrag)
    #zegt wat de speler heeft uitgegeven, hoeveel hij nog over heeft en dat de transactie voltooid is
    Label(text="{0} heeft {1} uitgegeven.".format(Speler, bedrag)).pack()
    Label(text="{0} heeft nog {1} over.".format(Speler, Bedragen[Speler])).pack()
    Label(text="").pack()
    Label(text="----- Transactie voltooid! -----").pack()
    Label(text="").pack()
    Button(text='done', command=destroy_popup).pack()
    popup.mainloop()
    #retouneerd de dictionary Bedragen
    return Bedragen

def destroy_besteding():
    besteding.destroy()
def destroy_error():
    error.destroy()
def destroy_vraag():
    vraag.destroy()
def destroy_popup():
    popup.destroy()

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
Uitgaven={}
#maakt een infinite loop
#(dit valt niet aan te raden)
#roept de functie main aan
main()
