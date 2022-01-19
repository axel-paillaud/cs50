-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Commande pour avoir la description des crimes ayant eu lieu le même jour, mois, année que le canard volé de CS50. Heure : 10: 15.
SELECT description FROM crime_scene_reports WHERE month = 7 AND day = 28 AND year = 2021;


-- Avoir l'activité de la boulangerie le jour J
SELECT activity, license_plate, hour, minute FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28;


-- Beaucoup de résultat den om avec celle-ci.
SELECT name FROM people WHERE license_plate = "5P2BI95" OR "94KL13X" OR "6P58WS2";


-- Ici, focus sur la première personne à être sorti de la boulangerie après le vol, à 10h 16
SELECT name, phone_number, passport_number FROM people WHERE license_plate = "5P2BI95";


-- TOut les appels ayant eu lieu le jour J. Trop de résultat ...
SELECT caller, receiver, duration FROM phone_calls WHERE year = 2021 AND day = 28 AND month = 7;


-- Un appel de ma première suspect le jour J, Vanessa.
SELECT caller, receiver, duration FROM phone_calls WHERE year = 2021 AND day = 28 AND month = 7 AND caller = "(725) 555-4692";


-- Aucune Interview de Vanessa ne sort, et l'interview de Amanda ne donne rien, elle parle d'un docteur ...
SELECT name, transcript FROM interviews WHERE name = "Vanessa" OR name = "Amanda";


-- Interviews de Bruce, plutôt intéressant :)
SELECT name, transcript FROM interviews WHERE name = "Bruce";