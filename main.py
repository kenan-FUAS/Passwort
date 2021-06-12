
from getpass import getpass
import os
import time
import os.path
import random
import string
from tkinter import Tk
import threading
import sys

current_user = os.getlogin()
current_harddisk = os.get
count = 0
passw = ""
options = ["d: Titel löschen", "t: Titel anzeigen", "a: Titel hinzufügen", "c: Master-Passwort ändern", "z: Zeitlimit Anwendung", "e: Programm beenden"]
os.chdir(r"C:\Users\\"+current_user+"\Desktop")
pfad = os.getcwd()      #Pfad, in dem die Ordner gespeichert werden


#Anzeigen der Optionen:
def optionen():



        print("\nWas möchten Sie tun?\t")
        print("")
        for option in options:      #Anzeigen der Optionen
            print(option)

        Q =input().lower()          #Input-Eingabe des Users

        #Aussuchen der Optionen:

        #Titel löschen
        if Q == "d":
            Delete()        #Aufrufen der Funktion Delete()


        #Alle Titel auflisten:

        elif Q == "t":
           ShowTitel()      #Aufrufen der Funktion ShowTitel()

        #Hinzufügen von Titeln:
        elif Q == "a":
            AddTitel()      #Aufrufen der Funktion AddTitel()
            optionen()      #Aufrufen der Funktion optionen()

        #Programm beenden:
        elif Q == "e":
            print("Das Programm wird beendet.")
            os.execl(sys.executable, sys.executable, *sys.argv)     #Beendigung des Programms

        #Ändern des MWP
        elif Q == "c":
            chMPW()     #Aufrufen der Funktion chMPW()

        #Ändern des Zeitlimits:
        elif Q =="z":
            Zeitlimit()     #Aufrufen der Funktion Zeitlimit()
        else:
            print("Eingabe stimmt mit keiner Option überein.")
            time.sleep(2.5)     #Unterbrechung des Programms für 2.5 Sekunden
            optionen()      #Aufrufen der Funktion optionen()



def First_Use():    #Erstellen von Ordner, in dem die Text-Dateien gespeichert sind

        os.makedirs("PManager")     #erstellt Ordner 'PManager'
        os.chdir(pfad +"\\PManager")    #ändert Dateien-Pfad
        os.makedirs("MasterPW")     #erstellt Ordner 'MasterPW' in Ordner 'PManager'
        os.makedirs("passwords")    #erstellt Ordner 'passwords' in Ordner 'PManager'
        os.makedirs("Zeitlimit")    #erstellt Ordner 'Zeitlimit' in Ordner 'PManager'



def Pass(passw,count,newpassw):     #Masterpasswort Abfrage


        if passw==newpassw:     #wenn das eingegebene Passwort mit dem MasterPW übereinstimmt --> Return value = True

            return True
        else:

            if count < 2 :      #zählt, wie oft schon versucht wurde, sich einzuloggen
                print("Falsches Passwort. Sie haben noch",2 - count,"Versuch(e).")
                passw=getpass("Bitte erneut eingeben:\t")   #erneute Abfrage des MasterPW
                count += 1      #count +1, um die Versuche zu zählen
                if Pass(passw,count,newpassw) == True:      #erneuter Aufruf der Funktion
                    return True
            else :
                print("Zu viele Versuche! Das Programm wird beendet.")  #mehr als 3 Versuche --> Programm wird beendet
                                                                        #Return value = False
                return False


def countdown():        #Timer für Zwischenablage

        timer = 30      #Timer auf 30 Sekunden festgelegt
        for x in range(30):
            timer -= 1     #for-Schleife, jede Sekunde wird dem Integer timer 1 abgezogen --> nach 30 Sekunden bei 0
            time.sleep(1)
        if timer == 0:
            r = Tk()                    #nach 30 Sekunden wird die Zwischenablage mit einem leeren String aktualisiert,
            r.withdraw()                #sodass das Passwort wieder aus der Zwischenablage gelöscht wird
            r.clipboard_clear()
            r.clipboard_append("")
            r.update()



def countdown2():               #Timer für das automatische Abmelden nach x Minuten

        m = open(pfad+"\\PManager\\Zeitlimit\\Zeitlimit.txt","r")   #Aufrufen der Datei, in der die selbstgewählte
        min = int(m.read())                                         #Minutenanzahl gespeichert ist
        timer = min*60      #Umwandlung der Minuten in Sekunden


        for x in range(int(timer)):     #Analog wie countdown()
            timer -= 1
            time.sleep(1)
        if timer == 0:

            print("\nAutomatisch abgemeldet, da Zeitlimit von "+str(min)+" Minuten erreicht.")
            os.execl(sys.executable, sys.executable, *sys.argv)     #System wird beendet, wenn timer = 0






def Zeitlimit():                #Wählen des Zeitlimits, bis automatisch beendet werden soll
    Zeitoptionen=["a: 1 Minute","b: 5 Minuten","c: 10 Minuten","d: 30 Minuten","e: 1 Stunde","f: 2 Stunden"]
    R = open(pfad + "\\PManager\\Zeitlimit\\Zeitlimit.txt", "r")    #Aufrufen der Datei, in der das Zeitlimit gespeichert ist
    print("\nAktuelles Zeitlimit: "+R.read()+" Minute(n).")   #Anzeigen des aktuellen Zeitlimits
    R.close()
    n = input("Möchten Sie ein neues Zeitlimit festlegen?y/n\t").lower()

    def Limit_return(limit):        #Zeitlimit-Optionen
        if limit == "a":
            return '1'
        elif limit == "b":
            return '5'
        elif limit == "c":
            return '10'
        elif limit == "d":
            return '30'
        elif limit == "e":
            return '60'
        elif limit == "f":
            return '120'
        else:
            print("Eingabe stimmt nicht überein.")
            Zeitlimit()     #ernueter Aufruf der Funktion Zeitlimit(), wenn Eingabe nicht mit den Oben angegebenen Optionen übereinstimmt


    if n == "y":
        print("")
        for options in Zeitoptionen:            #Anzeigen aller Zeitoptionen
            print(options)

        limit = input("Wählen Sie ein Zeitlimit.\t")        #Wählen des Zeitlimits



        Z = open(pfad + "\\PManager\\Zeitlimit\\Zeitlimit.txt", "w")    #öffnen der Datei, in der das Zeitlimit gespeichert wird
        Z.write(Limit_return(limit))    #Die gewählte Option wird in die Datei geschrieben
        Z.close()
        Z = open(pfad + "\\PManager\\Zeitlimit\\Zeitlimit.txt", "r")
        print("Das Zeitlimit beträgt ab dem nächsten Start der Anwendung "+Z.read()+" Minute(n).")      #Das aktualisierte Zeitlimit wird angegeben
        Z.close()
        time.sleep(2.5)   #2.5 Sekunden Verzögerung, damit der User Zeit zum Lesen hat
        optionen()      #Rückkehr zu Optionen
    elif n == "n":

        optionen()      #Rückkehr zu Optionen
    else:
        print("Eingabe stimmt nicht überein.")
        Zeitlimit()         #erneuter Aufruf der Funktion Zeitlimit(), wenn Eingabe nicht mit den Optionen übereinstimmt




def ShowTitel():                #Titel anzeigen und Passwort in Zwischenablage speichern
        path = os.chdir(pfad + "\\PManager\\passwords") #ändern des Dateipfads in den Ordner 'passwords'
        print("")
        print("Titel:")
        for titel in os.listdir(path):      #Anzeigen aller Titel
            print(titel.removesuffix(".txt"))

        print("")

        inp = input("Möchten Sie ein Passwort kopieren?y/n\t").lower()      #Abfrage Passwort kopieren
        if inp == "y":
            name = input("Welcher Titel?\t")
            Tipa = open(name + ".txt", "r")         #Titel muss ohne '.txt' eingegeben werden
            Tipa = Tipa.read().splitlines()         #Benutzername und Passwort werden Zeilenweise getrennt

            User=Tipa[0]        #Speichern des Benutzernamens in 'User'

            Password=Tipa[1]        #Speichern des Passworts in 'Password'

            print("Username: " + User + " | Password copied to clipboard.")     #Ausgeben des Benutzernamens
            r = Tk()
            r.withdraw()
            r.clipboard_clear()
            r.clipboard_append(Password)                #Speichern des Passworts in der Zwischenablage
            r.update()
            countdown_thread = threading.Thread(target = countdown)
            countdown_thread.start()                                   #Starten des threads 'countdown' (nach 30 Sekunden wird das Passwort aus
            Back()   #Rückkehr zu Optionen                             #der Zwischenablage gelöscht

        elif inp == "n":
            optionen()      #Rückkehr zu Optionen
        else:
            print("Eingabe stimmt nicht überein.")
            ShowTitel()     #erneutes Aufrufen der Funktion 'ShowTitel'




def Delete():            #Löschen von Titeln

        path = os.listdir(pfad+"\\PManager\\passwords")

        print("")
        print("Titel:")                      #--> Listet alle Titel im Ordner 'passwords' auf
        for x in range(len(path)):
            print(path[x].removesuffix(".txt"))
        print("")
        os.chdir(pfad+"\\PManager\\passwords") #Ändert Dateizugriff, sodass Titel bearbeitet werden können
        delTitel = input("Welcher Titel soll gelöscht werden?('e' zum zurückkehren)\t")+".txt"    #Auswahl des Titels + sparen des .txt
        if delTitel =="e.txt":   #Zurück ins Menü
            optionen()
        elif os.path.exists(delTitel):              #Überprüft, ob Eingabe existiert
            if input("Sind Sie sicher?y/n\t").lower() == "y":
                os.remove(delTitel)                 #Löscht titel
                print("Titel erfolgreich gelöscht.")
                optionen()
            else:
                optionen()
        else:
            print("Dieser Titel existiert nicht.\n")
            Delete()            #erneutes Aufrufen der Funktion 'Delete()'


def AddTitel():         #Titel hinzufügen und neues Passwort erstellen
        name = input("Neuer Titel('e' um zurückzukehren.):\t").lower()
        os.chdir(pfad + "\\PManager\\passwords")        #ändern des Dateipfads in den Ordner 'passwords'
        path = os.getcwd()
        if name == "e":
            optionen()      #Rückkehr zu Optionen

        else:

            newTitel = open(name + ".txt", "w+")        #Erstellen der neuen Datei
            newTitel.close()
            newTitel = open(name + ".txt", "a")         #öffnen der Datei
            newTitel.write(input("Geben Sie den Benutzernamen der Anwendung ein:\t"))       #Hinzufügen des Benutzernamens
            newTitel.close()
            addPass(name)       #Hinzufügen eines neuen Passworts durch die Funktion addPass(name)



def Back():
        print("")
        inp = input("Geben Sie 'e' ein, um zurückzukehren.\t")      #Funktion, um den User zurück zu den Optionen zu bringen
        if inp == "e":                                              #sobald 'e' einegegeben
            optionen()
        else:
            print("Eingabe stimmt nicht überein.")
            Back()


def addPass(name):

        Tipa = open(name +".txt", "a")              #Öffnen der Datei, für welche das Passwort erstellt werden soll
        Tipa.write("\r"+PasswortErstellung())       #Erstellen des Passworts durch die Funktion PasswortErstellung()
        print("Neues Passwort angelegt.")


def chMPW():
        inp = input("Wollen Sie wirklich ihr Master-Passwort ändern?y/n\t").lower() #erneute Bestätigung des Users
        if inp == "y":
            neu = input("Neues Passwort:\t")
            neu2 = input("Neues Passwort wiederholen:\t")       #doppelte Eingabe des neuen Passworts, um Schreibfehler vorzubeugen
            if neu == neu2:     #Überprüfung, ob beide Eingaben identisch sind
                if neu.__contains__(" "):
                    print("Passwort darf nicht ausbsjh")
                    time.sleep(1.5)
                    optionen()

                os.chdir(pfad+"\\PManager\\MasterPW")   #ändern des Datei-Pfads in den Ordner 'MasterPW'
                w = open("MasterPW.txt", "w")       #öffnen der Text-Datei, in welcher das MasterPW gespeichert ist
                w.write(neu)        #Überschreiben des alten MasterPW mit dem neuen MasterPW
                w.close()
                print("Master-Passwort erfolgreich geändert.")
                optionen()      #Rückkehr Optionen
            else:
                print("Eingaben stimmen nicht überein.")
                chMPW()     #Erneuter Aufruf der Funktion chMWP()


        elif inp == "n":
            optionen()      #Rückkehr Optionen
        else:
            print("Eingabe stimmt nicht überein.")
            chMPW()     #Erneuter Aufruf der Funktion chMWP()


def PasswortErstellung():

        def scanner_PW_Length():  # um die Länge des Passwords aufzunehmen

            length = 0
            for_ever = True
            try:
                length = int(input("Wie lange soll das Password sein?\t"))
                return length
            except Exception:
                print("Error!\nBitte nur Zahlen eingeben!")
                scanner_PW_Length()

        password_Length = scanner_PW_Length()

        def scanner_Number_Check():  # um zu erfahren ob der Benutzer Zahlen im Password haben möchte
            str = ""
            str = input("Möchten Sie Zahlen im PW haben?y/n\t").lower()
            for_ever = True
            while for_ever:
                if str == 'y':
                    for_ever = False
                    return True
                elif str == 'n':
                    for_ever = False
                    return False
                else:
                    print("Falsche Eingabe!")
                    str = input("Möchten Sie Zahlen im PW haben(Bitte richtige Eingabe)?y/n\t").lower()

        boolean_Number = scanner_Number_Check()

        def scanner_Uppercase_Check():  # um zu erfahren ob der Benutzer große Buchstaben im Password haben möchte
            str = ""
            str = input("Möchten Sie große Buchstaben im PW haben?y/n\t").lower()
            for_ever = True
            while for_ever:
                if str == 'y':
                    for_ever = False
                    return True
                elif str == 'n':
                    for_ever = False
                    return False
                else:
                    print("Falsche Eingabe!")
                    str = input("Möchten Sie große Buchstabe im PW haben(Bitte richtige Eingabe)?y/n\t").lower()

        boolean_GroßLetter = scanner_Uppercase_Check()

        def scanner_Signs_Check():  # um zu erfahren ob der Benutzer Sonderzeichen im Password haben möchte
            str = ""
            str = input("Möchten Sie Sonderzeichen im PW haben?y/n\t").lower()
            for_ever = True
            while for_ever:
                if str == 'y':
                    for_ever = False
                    return True
                elif str == 'n':
                    for_ever = False
                    return False
                else:
                    print("Falsche Eingabe!")
                    str = input("Möchten Sie Sonderzeichen im PW haben(Bitte richtige Eingabe)?y/n\t").lower()

        boolean_Sonderzeichen = scanner_Signs_Check()

        def password(length, boolean_Number, boolean_GroßLetter, boolean_Sonderzeichen):
            str = ""
            if boolean_Number:  # Überprüfung ob der Benutzer zahlen im PW haben möchte
                if boolean_GroßLetter:  # Überprüfung ob der Benutzer große oder kleine Buchstaben im PW haben möchte
                    if boolean_Sonderzeichen:  # Überprüfung ob der Benutzer Sonderzeichen im PW haben möchte
                        for i in range(length):
                            str += random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
                    else:
                        for i in range(length):
                            str += random.choice(string.ascii_letters + string.digits)

                else:
                    for i in range(length):
                        str += random.choice(string.ascii_lowercase + string.digits)
            else:  # Überprüfen Falls keine Numbers erwünscht sind____

                if boolean_GroßLetter and boolean_Sonderzeichen:
                    for i in range(length):
                        str += random.choice(string.ascii_letters + string.punctuation)

                else:
                    if boolean_GroßLetter and boolean_Sonderzeichen != True:
                        for i in range(length):
                            str += random.choice(string.ascii_letters)

                    elif boolean_Sonderzeichen and boolean_GroßLetter != True:
                        for i in range(length):
                            str += random.choice(string.ascii_lowercase + string.punctuation)
                    else:
                        for i in range(length):
                            str += random.choice(string.ascii_lowercase)

            # print(str)
            return str

        return password(password_Length, boolean_Number, boolean_GroßLetter, boolean_Sonderzeichen)

    #Anmeldung:
def Anmeldung():



        if os.path.exists("PManager") != True:  #Überprüft, ob Ordner PManager existiert. Wenn nicht --> erstmaliges Starten --> Masterpw Eingabe

                print("Willkommen.")
                First_Use()     #Funktion zur Erstellung von den notwendigen Ordnern und Datei-Pfaden
                pw = input("Geben Sie ihr Masterpasswort ein:\t")   #Eingabe des MasterPW
                newpassw = open(pfad+"\\PManager\\MasterPW\\MasterPW.txt","w+")     #Erstellen der Textdatei, in welcher das MasterPW gespeichert wird
                newpassw.write(pw)      #MasterPW wird in Textdatei gespeichert
                newpassw.close()
                default_Zeit = open(pfad+"\\PManager\\Zeitlimit\\Zeitlimit.txt","w+")   #default Zeitlimit wird gespeichert
                default_Zeit.write("5")
                default_Zeit.close()
                thread()            #Funktion, welche countdown2() startet --> Zeitlimit
                optionen()      #Rückkehr zu Optionen



        else:   #Normale Anmeldung ab 2. Starten des Programms

            np = open(pfad + "\\PManager\\MasterPW\\MasterPW.txt", "r")   #öffnet Datei mit Mpw
            newpassw = np.read()    #Liest das Mpw aus der Datei
            passw = getpass("Bitte geben Sie ihr Passwort ein:\t")

            if Pass(passw,count,newpassw) == True:          #Abfrage des MasterPW

                print("Willkommen.")
                thread()        #Funktion, welche countdown2() startet --> Zeitlimit
                optionen()      #Rückkehr zu Optionen
            else:

                exit()

def thread():
        countdown_thread = threading.Thread(target=countdown2)      #starten des threads 'countdown2()'
        countdown_thread.start()



#Main-Programm

Anmeldung()     #Aufrufen der Funktion Anmeldung()