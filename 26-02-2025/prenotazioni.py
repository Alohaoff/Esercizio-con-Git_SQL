

CREATE TABLE IF NOT EXISTS Concessionario.Prenotazioni (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_nome VARCHAR(100) NOT NULL,
    cliente_cognome VARCHAR(100) NOT NULL,
    veicolo_id INT NOT NULL,
    risorsa_id INT NOT NULL,
    FOREIGN KEY (veicolo_id) REFERENCES Concessionario.Veicoli(id) ON DELETE CASCADE,
    FOREIGN KEY (risorsa_id) REFERENCES Concessionario.Risorse(id) ON DELETE CASCADE
);



