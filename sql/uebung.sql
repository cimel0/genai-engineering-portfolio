SELECT m.name, a.name,
FROM mitarbeiter AS m
JOIN abteilung AS a ON m.abteilungs_id = a.id;

SELECT m.name, p.titel 
FROM mitarbeiter as m
JOIN projekt as p ON m.id = p.mitarbeiter_id; 


SELECT all name, all titel 
FROM mitarbeiter as m 
JOIN projekt as p ON m.id = p.mitarbeiter_id; 

WITH abteilungsdurchschnitt AS (
    SELECT abteilungs_id, AVG(gehalt) AS durchschnittsgehalt
    FROM mitarbeiter
    GROUP BY abteilungs_id
)

SELECT m.name, m.gehalt 
FROM mitarbeiter AS m 
JOIN abteilungsdurchschnitt AS a 
ON m.abteilungs_id = a.abteilungs_id
WHERE m.gehalt > a.durchschnittsgehalt; 


-- GROUP BY: 1 Zeile pro Abteilung, einzelne Mitarbeiter verschwinden
SELECT abteilungs_id, AVG(gehalt) AS durchschnitt
FROM mitarbeiter
GROUP BY abteilungs_id;

-- Window Function: 1 Zeile PRO MITARBEITER, Durchschnitt zusätzlich sichtbar
SELECT name, gehalt, abteilungs_id,
       AVG(gehalt) OVER (PARTITION BY abteilungs_id) AS abteilungsdurchschnitt
FROM mitarbeiter;


SELECT name, gehalt, abteilungs_id, MAX(gehalt) OVER (PARTITION BY abteilung_id) AS abteilungsdurchschnitt
FROM mitarbeiter 

SELECT name, abteilungs_id, gehalt, rang, 
ROW_NUMBER() OVER (PARTITION BY abteilungs_id ORDER BY gehalt DESC) AS rang 
FROM mitarbeiter 

SELECT abteilungs_id, COUNT(*) AS anzahl, AVG(gehalt) AS durchschnitt 
FROM mitarbeiter 
WHERE gehalt > 4000
GROUP BY abteilungs_id
HAVING COUNT(*) >= 2 
