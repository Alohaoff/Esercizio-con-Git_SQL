
def creazionetabellaprenotazioni(database, mycursor):
        queryPrenotazioni = """CREATE TABLE """+database+""".prenotazioni ( id INT AUTO_INCREMENT PRIMARY KEY, 
        fk_risorsa INT NOT NULL,
        fk_utente INT NOT NULL,
        FOREIGN KEY (fk_risorsa) REFERENCES risorse(id),
        FOREIGN KEY (fk_utente) REFERENCES utenti(id_utente)
        );"""
        print(queryPrenotazioni)
        mycursor.execute(queryPrenotazioni)
        
def aggiuntaPrenotazioni(database, mycursor):
    queryMostraUtenti ="select * from utenti"
    mycursor.execute(queryMostraUtenti)
    myresult = mycursor.fetchall()
    if len(myresult)>=1:
        for riga in myresult:
            print(f"ID: {riga[0]} - Nome {riga[1]} - Cognome {riga[2]}")
    else:
        print("Database vuoto")
        
    queryMostraRisorse ="select * from risorse"
    mycursor.execute(queryMostraRisorse)
    myresult = mycursor.fetchall()
    if len(myresult)>=1:
        for riga in myresult:
            print(f"ID: {riga[0]} - Marca {riga[1]} - Modello {riga[2]} - Prezzo {riga[2]}")
    else:
        print("Database vuoto")
    idUtente = input("Inserisci id dell' utente: ")
    idRisorsa = input("Inserisci id della risorsa: ")

    queryInsRisorsa = "INSERT INTO "+ database + ".prenotazioni (fk_risorsa, fk_utente) VALUES (%s, %s);"
    valori =(idUtente, idRisorsa)
    mycursor.execute(queryInsRisorsa, valori)

#da provare 
def cancellaPrenotazione(database, mycursor):
    queryMostraPrenotazioni = "SELECT * FROM " + database + ".prenotazioni"
    mycursor.execute(queryMostraPrenotazioni)
    myresult = mycursor.fetchall()
    
    if len(myresult) >= 1:
        for riga in myresult:
            print(f"ID Prenotazione: {riga[0]} - ID Risorsa: {riga[1]} - ID Utente: {riga[2]}")
    else:
        print("Nessuna prenotazione presente nel database.")
        return
    
    idPrenotazione = input("Inserisci l'ID della prenotazione da cancellare: ")
    
    queryCancella = "DELETE FROM " + database + ".prenotazioni WHERE id = %s;"
    mycursor.execute(queryCancella, (idPrenotazione,))
    
    print(f"Prenotazione con ID {idPrenotazione} cancellata con successo.")


