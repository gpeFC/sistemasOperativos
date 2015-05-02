"""
Modulo para simular el movimiento de un robot en un mapa rectangular
poblado arbitrariamente con n obstaculos en el mapa, en lugares donde
el robot no puede posicionarse. Los movimientos son unicamente 
verticales y horizontales(adelante, atras, izquierda, derecha).
"""

import random
import time
import os


class Simulador:
	""" Documentacion de la clase <Simulador>. """
	def __init__(self, dim_x=8, dim_y=8, pscn=".", obst="O", agnt="X"):
		""" (Pseudo)Constructor de la clase <Simulador>. """
		self.filas = dim_y
		self.columnas = dim_x
		self.posicion = str(pscn)
		self.obstaculo = str(obst)
		self.agente = str(agnt)
		self.mapa = []
		for i in range(self.filas):
			fila = []
			fila = [self.posicion]* self.columnas
			self.mapa.append(fila)

	def poblar_mapa(self, obts=0):
		""" Documentacion para la funcion <poblar_mapa>. """
		if obts==0 or obts<((self.filas*self.columnas)//3) or obts>(((self.filas*self.columnas)//3)*2):
			obts = (self.filas * self.columnas)//3
		self.mapa[random.randint(0,self.filas-1)][random.randint(0,self.columnas-1)] = self.agente

	def imprime_mapa(self):
		""" Documentacion para la funcion <imprime_mapa>. """
		for i in range(self.filas):
			for j in range(self.columnas):
				print self.mapa[i][j] + " ",
			print


simulador = Simulador()
simulador.imprime_mapa()
simulador.poblar_mapa()
print
simulador.imprime_mapa()
print

pnt = "."
rbt = "R"
obst = "O"


tablero = []
for i in range(8):
	fila = []
	for j in range(8):
		fila = [pnt] * 8
	tablero.append(fila)

obsts = []
i = 0
while i < random.randint(15, 20):
	pass
	bndr = True
	obs = [random.randint(0,7), random.randint(0,7)]
	for j in range(len(obsts)):
		if obs == obsts[j]:
			bndr = False
			break
	if bndr:
		obsts.append(obs)
		i += 1
	else:
		i -= 1

for i in range(len(obsts)):
	tablero[obsts[i][0]][obsts[i][1]] = obst

tablero[random.randint(0,7)][random.randint(0,7)] = rbt
