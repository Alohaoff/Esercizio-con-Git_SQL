
def creazionetabellaprenotazioni(database, mycursor):
        queryPrenotazioni = """create or replace table """ + database + """.Concessionario.Prenotazioni(
            id int auto_increment primary key,
            cliente_nome varchar(100) not null,
            cliente_cognome varchar(100) not null,
            veicolo_id int not null,
            risorsa_id int not null,
            foreign key (veicolo_id) references Veicoli(id) on delete cascade,
            foreign key (risorsa_id) references Risorse(id) on delete cascade
        )"""
        mycursor.execute(queryPrenotazioni)
        
def aggiuntaPrenotazioni(database, mycursor, mydb):
    # Recupera e mostra i veicoli disponibili
    mycursor.execute(f"SELECT id, modello, marca FROM {database}.Risorse")
    veicoli = mycursor.fetchall()
    print("\nVeicoli disponibili:")
    for v in veicoli:
        print(f"ID: {v[0]} | Modello: {v[1]} | Marca: {v[2]}")

    veicolo_id = input("\nInserisci l'ID del veicolo scelto: ")

    # Recupera e mostra le risorse disponibili
    mycursor.execute(f"SELECT id, nome FROM {database}.Utenti")
    risorse = mycursor.fetchall()
    print("\nRisorse disponibili:")
    for r in risorse:
        print(f"ID: {r[0]} | Nome: {r[1]}")

    risorsa_id = input("\nInserisci l'ID della risorsa scelta: ")

    # Inserimento dati cliente e prenotazione
    cliente_nome = input("\nInserisci nome cliente: ")
    cliente_cognome = input("Inserisci cognome cliente: ")
   
    # Query per inserire la nuova prenotazione
    query_aggiunta_prenotazioni = f"""
    INSERT INTO {database}.Prenotazioni 
    (cliente_nome, cliente_cognome, veicolo_id, risorsa_id)
    VALUES (%s, %s, %s, %s);
    """

    valori = (cliente_nome, cliente_cognome, veicolo_id, risorsa_id)

    try:
        mycursor.execute(query_aggiunta_prenotazioni, valori)
        mydb.commit()
        print("\n Prenotazione aggiunta con successo!")
    except Exception as e:
        print("\n Errore durante l'inserimento della prenotazione:", e)



