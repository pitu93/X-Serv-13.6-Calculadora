#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys


if len(sys.argv) != 4:
    print
    sys.exit("Tienes que poner bien los argumentos")
else:
    operacion= sys.argv[1];
    if(operacion!= "suma" and operacion!= "resta" and operacion!= "multiplica" and operacion!= "divide"):
        print("Las operaciones posibles son suma, resta, multiplica o divide")

def suma(op1, op2):
    resultado= op1 + op2
    print str(resultado)

def resta(op1, op2):
    resultado= op1 - op2
    print str(resultado)

def multiplica(op1, op2):
    resultado= op1 * op2
    print str(resultado)

def divide(op1, op2):
    try:
        resultado= op1 / op2
        print str(resultado)

    except ZeroDivisionError:
        print("No es posible dividir por 0")

if sys.argv[1] == 'suma':
    suma(int(sys.argv[2]), int(sys.argv[3]))

if sys.argv[1] == 'resta':
    resta(int(sys.argv[2]), int(sys.argv[3]))

if sys.argv[1] == 'multiplica':
    multiplica(int(sys.argv[2]), int(sys.argv[3]))

if sys.argv[1] == 'divide':
    divide(int(sys.argv[2]), int(sys.argv[3]))
