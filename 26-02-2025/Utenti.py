def table_utenti(database,cursor):
    queryUtenti = "CREATE OR REPLACE TABLE "+ database + ".utenti (id_utente INT AUTO_INCREMENT PRIMARY KEY,nome VARCHAR(50) NOT NULL,cognome VARCHAR(50) NOT NULL,telefono VARCHAR(15));"
    cursor.execute(queryUtenti)
    
def aggiungi_utente(database,cursor):
    nome = input("Digita il nome: ")
    cognome = input("Digita il cognome: ")
    telefono = input("Digita il numero di telefono: ")
    
    query = "INSERT INTO "+ database + ".utenti (nome, cognome, telefono) VALUES (%s, %s, %s)"
    valori =(nome, cognome, telefono)
    cursor.execute(query, valori)
    