-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Commande pour avoir la description des crimes ayant eu lieu le même jour, mois, année que le canard volé de CS50
SELECT description FROM crime_scene_reports WHERE month = 7 AND day = 28 AND year = 2021;

