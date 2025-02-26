
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
        # queryUtenti = "create or replace table " + database +".Studenti(id int auto_increment primary key, nome varchar(100), cognome varchar(100), VotoItaliano int, VotoMatematica int, VotoInglese int)"
        # mycursor.execute(queryUtenti)
        # queryRisorse = "create or replace table " + database +".Studenti(id int auto_increment primary key, nome varchar(100), cognome varchar(100), VotoItaliano int, VotoMatematica int, VotoInglese int)"
        # mycursor.execute(queryRisorse)
        # queryPrenotazioni = "create or replace table " + database +".Studenti(id int auto_increment primary key, nome varchar(100), cognome varchar(100), VotoItaliano int, VotoMatematica int, VotoInglese int)"
        # mycursor.execute(queryPrenotazioni)
        
    return mydb

mydb = crea_replace_db()
mycursor = mydb.cursor()

def menu():
    condizione = True
    while condizione:

        print("\n------| MENU |------")
        print("6. Reset DB")
        print("7. Stop")

        scelta = input("Seleziona un'opzione: ")

        if scelta == "6":
            pass
        elif scelta=="7":
            condizione = False
            print("Programma terminato.")
        else:
            print("Opzione non valida! Inserisci un numero tra 1 e 3.")
            
crea_replace_db()
            