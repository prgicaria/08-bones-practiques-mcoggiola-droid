#!/usr/bin/env python
''' Divisió. Divisió entre dos nombres enters
Institut Icària
Programació - 1r Batxillerat - Curs 2023-24
Càlcul aritmètic que consisteix a efectuar la divisió entre dos nombres del
conjunt dels enters.Dividir dos nombres. Quocient, Divisió i Residu
'''
__author__ = "Martín Coggiola"
__email__ = "mcoggiola@instituticaria.cat"
__date__ = "2025/10/20"

Dividend = int(input("ingresar dividend"))
Divisor = int(input("ingresar divisor"))
Quocient = (Dividend)//(Divisor)
Residu = (Dividend) % (Divisor)
print(f"Divisió: {Dividend}/{Divisor}")
print(f"Quocient: {Quocient}")
print(f"Residu: {Residu}")
