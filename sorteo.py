# -*- coding: utf-8 -*-
# (C) D.R. CECONTEC, S.C. - 2016
# Sorteo para intercambio godinezzzz v.1.0
# ----------------------------------------
#
# Instrucciones:
# 1) Se registran todos los participantes en una lista numerada
# 2) Se configura el programa con el número de participantes
# 3) El programa revuelve una lista con la relación de quien da y quien recibe

# TODO:
# 1) Incluir un diccionario con los nombre de los participantes o tomarlos de una base de datos
# 2) Enviar los correos de resultado directamente a los participantes

import random

num_participantes = 9
da = range(1,num_participantes+1)
recibe = []

for d in da:
  asignado = False
  while not asignado:
    r = random.randint(1,num_participantes)
    if not r in recibe and r != d:
      recibe.append(r)
      asignado = True
    else:
      asignado = False
print "Da:     " + str(da)
print "Recibe: " + str(recibe)
