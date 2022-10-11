#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def square_root(a: float) -> float:
    #Calculer la racine carré
    racine_car = math.sqrt(a)
    return racine_car

def square(a: float) -> float:
    #Calculer le carré d'un nombre
    carre = a ** 2
    return carre


def average(a: float, b: float, c: float) -> float:
    # Calculer la moyenne de 3 nombres donnés
    moy = (a+b+c) / 3
    return moy

def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    # Convertir en radians un angle fourni au départ en degrés
    deg_rad = 0.017453292519943
    min_rad = 0.00029088820866572
    sec_rad = 0.0000048481368110954
    rad = (angle_degs * deg_rad) + (angle_mins*min_rad) + (angle_secs*sec_rad)
    return rad


def to_degrees(angle_rads: float) -> tuple:
    #convertir en degrés, minutes, secondes un angles fourni au départ en raidans
    degres = angle_rads * 180 / math.pi
    min = (degres - math.pi)
    seconde = degres
    return (degres, min, )


def to_celsius(temperature: float) -> float:
    # Convertir en degrés Celsius une température exprimée au départ en degrés Fahrenheit

    return (temperature - 32 ) / 1.8


def to_farenheit(temperature: float) -> float:
    # convertir en f une température exprimée en c

    return (temperature - 32) * 1.8


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 180 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")

    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
