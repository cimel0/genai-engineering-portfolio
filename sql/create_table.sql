CREATE TABLE Kunde (
    kunde_id INTEGER PRIMARY KEY,
    name      VARCHAR(100) NOT NULL,
    email     VARCHAR(150) UNIQUE
);

CREATE TABLE Police (
    police_id INTEGER PRIMARY KEY,
    kunde_id  INTEGER NOT NULL,
    typ       VARCHAR(50) NOT NULL,
    beginn    DATE NOT NULL,
    FOREIGN KEY (kunde_id) REFERENCES Kunde(kunde_id)
);

CREATE TABLE Schadensfall (
    schaden_id INTEGER PRIMARY KEY,
    police_id INTEGER NOT NULL, 
    schadensdatum DATE NOT NULL,
    betrag DECIMAL(10,2) NOT NULL CHECK (betrag >= 0),
    status VARCHAR(100) NOT NULL,
    FOREIGN KEY (police_id) REFERENCES Police(police_id)
);