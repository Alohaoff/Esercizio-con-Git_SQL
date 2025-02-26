def CreazioneTabRisorse(database, mycursor):
    queryRisorse = "CREATE OR REPLACE TABLE " + database +".risorse(id int auto_increment primary key, marca varchar(100), modello varchar(100), prezzo int)"
    mycursor.execute(queryRisorse) 
    
def aggiungi_risorsa(database, mycursor):
    marca = input("Inserisci la Marca del veicolo: ")
    modello = input("Inserisci il Modello del veicolo: ")
    prezzo = input("Inserisci il Prezzo del veicolo: ")

    queryInsRisorsa = "INSERT INTO "+ database + ".risorse (marca, modello, prezzo) VALUES (%s, %s, %s);"
    valori =(marca, modello, prezzo)
    mycursor.execute(queryInsRisorsa, valori)