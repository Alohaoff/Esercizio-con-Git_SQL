def CreazioneTabRisorse(database, mycursor):
    queryRisorse = "create or replace table " + database +".Concessionaria(id int auto_increment primary key, Marca varchar(100), Modello varchar(100), Prezzo int)"
    mycursor.execute(queryRisorse) 
    
def aggiungi_risorsa(database, mycursor):
    marca = input("Inserisci la Marca del veicolo: ")
    modello = input("Inserisci il Modello del veicolo: ")
    prezzo = input("Inserisci il Prezzo del veicolo: ")

    queryInsRisorsa = f"INSERT INTO Concessionaria (Marca, Modello, Prezzo) VALUES ('{marca}', '{modello}', {prezzo});"

    print("Risorsa aggiunta")
    return queryInsRisorsa