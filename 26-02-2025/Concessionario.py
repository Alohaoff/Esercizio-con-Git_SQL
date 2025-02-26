import Risorse
import Utenti
import prenotazioni
import mysql.connector

host="localhost"
user="root"
password=""
database="concessionario"

def crea_replace_db():
    try:
        mydb = mysql.connector.connect(
        host = host,
        user = user,
        password = password,
        database = database
        )
    except:
        mydb = mysql.connector.connect(
        host = host,
        user = user,
        password = password
        )
        mycursor = mydb.cursor()
        query = "create database " + database
        mycursor.execute(query)
        Utenti.table_utenti(database,mycursor)
        Risorse.CreazioneTabRisorse(database,mycursor)
        prenotazioni.creazionetabellaprenotazioni(database,mycursor)
        
    return mydb

mydb = crea_replace_db()
mycursor = mydb.cursor()

def menu():
    condizione = True
    while condizione:

        print("\n------| MENU |------")
        print("1. Aggiungi Utente")
        print("2. Aggiungi Risorsa")
        print("3. Aggiungi Prenotazione")
        print("4. Mostra Prenotazioni")
        print("5. Stop")

        scelta = input("Seleziona un'opzione: ")

        if scelta == "1":
            Utenti.aggiungi_utente(database,mycursor)
            mydb.commit()
        elif scelta=="2":
            Risorse.aggiungi_risorsa(database,mycursor)
            mydb.commit()
        elif scelta=="3":
            prenotazioni.aggiuntaPrenotazioni(database,mycursor)
            mydb.commit()
        elif scelta=="4":
            queryMostraPrenotazioni ="SELECT nome,cognome,telefono,marca,modello,prezzo FROM concessionario.prenotazioni JOIN concessionario.risorse on prenotazioni.fk_risorsa = risorse.id JOIN concessionario.utenti on prenotazioni.fk_utente = utenti.id_utente;"
            mycursor.execute(queryMostraPrenotazioni)
            myresult = mycursor.fetchall()
            if len(myresult)>=1:
                for riga in myresult:
                    print(f"Nome: {riga[0]} - Cognome {riga[1]} - Telefono {riga[2]} - Marca {riga[3]} - Modello {riga[4]} - Prezzo {riga[5]}")
            else:
                print("Database vuoto")
        elif scelta=="5":
            condizione = False
            print("Programma terminato.")
        else:
            print("Opzione non valida! Inserisci un numero tra 1 e 5.")
            
crea_replace_db()         
menu()            