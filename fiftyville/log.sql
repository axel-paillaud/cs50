-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Commande pour avoir la description des crimes ayant eu lieu le même jour, mois, année que le canard volé de CS50. Heure : 10: 15.
SELECT description FROM crime_scene_reports WHERE month = 7 AND day = 28 AND year = 2021;


-- Avoir l'activité de la boulangerie le jour J
SELECT activity, license_plate, hour, minute FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28;


-- Beaucoup de résultat den om avec celle-ci.
sqlite> SELECT name FROM people WHERE license_plate = "5P2BI95" OR "94KL13X" OR "6P58WS2";