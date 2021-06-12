from getpass import getpass
import os
import time
import os.path
import random
import string
from tkinter import Tk
import threading
import sys
current_user = os.getlogin()                #um den Namen der aktuellen Benutzer aufzunehmen
count = 0                                   #um Fehlversuche bei der Passworteingabe zu zählen
password = ""
options = ["d: Titel löschen", "t: Titel anzeigen", "a: Titel hinzufügen", "c: Master-Passwort ändern", "e: Programm beenden"]
os.chdir(r"C:\Users\felix\Desktop")
pfad = os.getcwd()


#Anzeigen der Optionen:
def optionen():

        print("\nWas möchten Sie tun?\t"+"\n")


        for option in options:              #Ausgabe der Optionen
            print(option)

        benutzer_Eingabe =input().lower()

        #Aussuchen der Optionen:

        #Titel löschen
        if benutzer_Eingabe == "d":
            Delete()


        #Alle Titel auflisten:

        elif benutzer_Eingabe == "t":
           ShowTitel()

        #Hinzufügen von Titeln:
        elif benutzer_Eingabe == "a":
            AddTitel()
            optionen()

        #Programm beenden:
        elif benutzer_Eingabe == "e":
            print("Das Programm wird beendet.")
            os.execl(sys.executable, sys.executable, *sys.argv)

        #Ändern des MP
        elif benutzer_Eingabe == "c":
            change_Master_Password()

        else:
            print("Eingabe stimmt mit keiner Option überein.")
            time.sleep(1.5)
            optionen()



def make_Direct():                           #Erstellen von Ordner, in dem Passwörter gespeichert sind:

        os.makedirs("PManager") #erstellt Ordner PManager
        os.chdir(pfad +"\\PManager")
        os.makedirs("MasterPW")
        os.makedirs("passwords")



def password_Check(passw,count,newpassw):           #Masterpasswort Abfrage:


        if passw==newpassw:

            return True
        else:

            if count < 2 :
                print("Falsches Passwort. Sie haben noch",2 - count,"Versuch(e).")
                passw=getpass("Bitte erneut eingeben:\t")
                count += 1
                if password_Check(passw,count,newpassw) == True:
                    return True
            else :
                print("Zu viele Versuche! Das Programm wird beendet.")

                return False

    #Timer für Zwischenablage:
def countdown():

        timer = 30
        for x in range(30):
            timer = timer -1
            time.sleep(1)
        if timer == 0:
            r = Tk()
            r.withdraw()
            r.clipboard_clear()
            r.clipboard_append("")
            r.update()
def countdown2():

        timer = 300
        for x in range(300):
            timer = timer -1
            time.sleep(1)
        if timer == 0:
            print("Automatisch abgemeldet.")





    #Titel anzeigen und Passwort in clipboard speichern:
def ShowTitel():
        path = os.chdir(pfad + "\\PManager\\passwords")
        print("")
        print("Titel:")
        for titel in os.listdir(path):
            print(titel)

        inp = input("Möchten Sie ein Passwort kopieren?y/n\t").lower()
        if inp == "y":
            name = input("Welcher Titel?\t")
            Tipa = open(name + ".txt", "r")
            Tipa = Tipa.read().splitlines()

            User=Tipa[0]

            Password=Tipa[1]

            print("Username: " + User + " | Password copied to clipboard.")
            r = Tk()
            r.withdraw()
            r.clipboard_clear()
            r.clipboard_append(Password)
            r.update()
            countdown_thread = threading.Thread(target = countdown)
            countdown_thread.start()
            Back()

        elif inp == "n":
            optionen()
        else:
            print("Eingabe stimmt nicht überein.")
            ShowTitel()



    #Löschen von Titel:
def Delete():

        path = os.listdir(pfad+"\\PManager\\passwords")#-->

        print("")
        print("Titel:")                      #--> Listet alle Titel in PManager auf
        for x in range(len(path)):
            print(path[x])
        print("")
        os.chdir(pfad+"\\PManager\\passwords") #Ändert Dateizugriff, sodass Titel bearbeitet werden können
        delTitel = input("Welcher Titel soll gelöscht werden?('e' zum zurückkehren)\t")+".txt"    #Auswahl des Titels + sparen des .txt
        if delTitel =="e.txt":   #Zurück ins Menü
            optionen()
        elif os.path.exists(delTitel):  #Überprüft, ob Eingabe existiert
            if input("Sind Sie sicher?y/n\t").lower() == "y":
                os.remove(delTitel) #Löscht titel
                print("Titel erfolgreich gelöscht.")
                optionen()
            else:
                optionen()
        else:
            print("Dieser Titel existiert nicht.\n")
            Delete()


def AddTitel():
        name = input("Neuer Titel('e' um zurückzukehren.):\t").lower()
        os.chdir(pfad + "\\PManager\\passwords")
        path = os.getcwd()
        if name == "e":
            optionen()


        elif path.endswith("PManager\\passwords") == False:
            newPath = os.chdir(path + "\\PManager\\passwords")
            newTitel = open(name + ".txt", "w+")
            newTitel.close()
            newTitel = open(name + ".txt", "a")
            newTitel.write(input("Geben Sie den Benutzernamen der Anwendung ein:\t"))
            newTitel.close()
            add_Password(name)
        else:

            newTitel = open(name + ".txt", "w+")
            newTitel.close()
            newTitel = open(name + ".txt", "a")
            newTitel.write(input("Geben Sie den Benutzernamen der Anwendung ein:\t"))
            newTitel.close()
            add_Password(name)
def Back():
        print("")
        inp = input("Geben Sie 'e' ein, um zurückzukehren.\t")
        if inp == "e":
            optionen()
        else:
            print("Eingabe stimmt nicht überein.")
            Back()


def add_Password(name):

        benutzer_Eingabe = input("Neues Passwort anlegen? y/n\t")

        if benutzer_Eingabe == "y":                 #Benutzer Bestätigung um ein neues Passwort anzulegen
            password_File = open(name +".txt", "a")
            password_File.write("\r"+passwortErstellung())
            print("Neues Passwort angelegt.")

        elif benutzer_Eingabe == "n":               #Benutzer will doch kein neues passwort anlegen
            optionen()
        else:                                       #im Falle von falscher Benutzer Eingabe
            print("Eingabe stimmt nicht überein.")
            add_Password(name)

def change_Master_Password():
        benutzer_Eingabe = input("Wollen Sie wirklich ihr Master-Passwort ändern?y/n\t").lower()

        if benutzer_Eingabe == "y":                      #Benutzer Bestätigung um das Master Password zu ändern
            input_Password = input("Neues Passwort:\t")
            second_Input_Password = input("Neues Passwort wiederholen:\t")

            if input_Password == second_Input_Password:          # Vergleiche die beiden eingegebenen Passwörter
                os.chdir(pfad+"\\PManager\\MasterPW")
                w = open("MasterPW.txt", "w")
                w.write(input_Password)
                print("Master-Passwort erfolgreich geändert.")
                optionen()
            else:                                                #im Falle nicht übereinstimmender Benuztereingaben
                                                                 # von inoput_Password und second_Input_Password
                print("Eingaben stimmen nicht überein.")
                change_Master_Password()


        elif benutzer_Eingabe == "n":                     #Benutzer will doch das Master Passwort nicht ändern
            optionen()
        else:                                             #im Falle von falscher Benutzer Eingabe
            print("Eingabe stimmt nicht überein.")
            change_Master_Password()


def passwortErstellung():

        def scanner_PW_Length():  # um die Länge des Passwords aufzunehmen

            length = 0
            for_ever = True
            try:                    #um ausschließlich intger Werte aufnehmen zu können und
                                    # das Programm vor Abstürtz aufgund falscher Eingabe zu schützen
                length = int(input("Wie lange soll das Password sein?\t"))
                return length
            except Exception:
                print("Error!\nBitte nur Zahlen eingeben!")
                scanner_PW_Length()

        password_Length = scanner_PW_Length()  #um die vom Benutzer eingegebene Werte in die jeweilige Variable zu speichern

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

        boolean_Number = scanner_Number_Check()  #um die vom Benutzer eingegebene Werte in die jeweilige Variable zu speichern

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

        boolean_GroßLetter = scanner_Uppercase_Check()  #um die vom Benutzer eingegebene Werte in die jeweilige Variable zu speichern

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

        boolean_Sonderzeichen = scanner_Signs_Check()  #um die vom Benutzer eingegebene Werte in die jeweilige Variable zu speichern

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
            else:  # Überprüfen Falls keine Numbers erwünscht sind__

                if boolean_GroßLetter and boolean_Sonderzeichen:
                    for i in range(length):
                        str += random.choice(string.ascii_uppercase + string.punctuation)

                else:
                    if boolean_GroßLetter and boolean_Sonderzeichen != True:
                        for i in range(length):
                            str += random.choice(string.ascii_uppercase)

                    elif boolean_Sonderzeichen and boolean_GroßLetter != True:
                        for i in range(length):
                            str += random.choice(string.ascii_lowercase + string.punctuation)
                    else:
                        for i in range(length):
                            str += random.choice(string.ascii_lowercase)


            return str

        return password(password_Length, boolean_Number, boolean_GroßLetter, boolean_Sonderzeichen)

    #Anmeldung:
def anmeldung():



        if os.path.exists("PManager") != True:  #Überprüft, ob Ordner PManager existiert. Wenn nicht --> erstmaliges Starten --> Masterpw Eingabe

                print("Willkommen.")
                make_Direct()
                benutzer_Eingabe = input("Geben Sie ihr Masterpasswort ein:\t")
                password_file = open (pfad+"\\PManager\\MasterPW\\MasterPW.txt","w+")
                password_file.write(benutzer_Eingabe) #das vom benutzer eingegebene Password wird in die Datei password_file eingespeichert
                thread()
                optionen()
        else:   #Normale Anmeldung ab 2. Starten des Programms

                Master_Password_File = open(pfad + "\\PManager\\MasterPW\\MasterPW.txt", "r")   #öffnet Datei mit Mpw
                password_file = Master_Password_File.read()    #Liest das Mpw aus der Datei
                eingegebeneMasterPassword = getpass("Bitte geben Sie ihr Passwort ein:\t")

                if password_Check(eingegebeneMasterPassword,count,password_file):

                    print("Willkommen.")
                    thread()
                    optionen()
                else:

                    exit()

def thread():
        countdown_thread = threading.Thread(target=countdown2)
        countdown_thread.start()





anmeldung()