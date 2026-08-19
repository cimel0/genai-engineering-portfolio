-- 2.1: Joins
SELECT m.name, a.name
FROM mitarbeiter AS m
JOIN abteilung AS a ON m.abteilungs_id = a.id;

SELECT m.name, p.titel
FROM mitarbeiter AS m
JOIN projekt AS p ON m.id = p.mitarbeiter_id;

SELECT m.name, p.titel
FROM mitarbeiter AS m
LEFT JOIN projekt AS p ON m.id = p.mitarbeiter_id;

-- 2.2: CTEs
WITH abteilungsdurchschnitt AS (
    SELECT abteilungs_id, AVG(gehalt) AS durchschnittsgehalt
    FROM mitarbeiter
    GROUP BY abteilungs_id
)
SELECT m.name, m.gehalt
FROM mitarbeiter AS m
JOIN abteilungsdurchschnitt AS a ON m.abteilungs_id = a.abteilungs_id
WHERE m.gehalt > a.durchschnittsgehalt;

-- 2.3: Window Functions
SELECT abteilungs_id, AVG(gehalt) AS durchschnitt
FROM mitarbeiter
GROUP BY abteilungs_id;

SELECT name, gehalt, abteilungs_id,
       AVG(gehalt) OVER (PARTITION BY abteilungs_id) AS abteilungsdurchschnitt
FROM mitarbeiter;

SELECT name, gehalt, abteilungs_id,
       MAX(gehalt) OVER (PARTITION BY abteilungs_id) AS abteilungsmaximum
FROM mitarbeiter;

SELECT name, abteilungs_id, gehalt,
       ROW_NUMBER() OVER (PARTITION BY abteilungs_id ORDER BY gehalt DESC) AS rang
FROM mitarbeiter;

-- 2.4: Aggregation, WHERE + HAVING
SELECT abteilungs_id, COUNT(*) AS anzahl, AVG(gehalt) AS durchschnitt
FROM mitarbeiter
WHERE gehalt > 4000
GROUP BY abteilungs_id
HAVING COUNT(*) >= 2;