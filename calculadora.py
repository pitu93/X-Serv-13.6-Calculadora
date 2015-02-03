#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys


if len(sys.argv) != 4:
    print
    sys.exit("Tienes que poner bien los argumentos")

def suma(op1, op2):
    resultado= op1 + op2
    print str(resultado)

if sys.argv[1] == 'suma':
    suma(int(sys.argv[2]), int(sys.argv[3]))


