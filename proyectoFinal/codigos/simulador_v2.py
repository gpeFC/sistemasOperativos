"""
Version 2 del simulador.
"""

import random
import math
import time
import os


class Simulador:
	""" Documentacion de la clase <Simulador>. """
	def __init__(self, dim_x=8, dim_y=8, pscn=".", obst="O", agnt="R", mta="M"):
		""" (Pseudo)Constructor de la clase <Simulador>. """
		self.filas = dim_y
		self.columnas = dim_x
		self.orientacion = 'N'
		self.simbolos = (str(pscn), str(obst), str(agnt), str(mta))
		self.axy = [0, 0]
		self.mxy = [0, 0]
		self.mapa = []
		for i in range(self.filas):
			fila = []
			fila = [self.simbolos[0]] * self.columnas
			self.mapa.append(fila)

	def poblar_mapa(self, obts=0):
		""" Documentacion para la funcion <poblar_mapa>. """
		if obts==0 or obts<((self.filas*self.columnas)//3) or obts>(((self.filas*self.columnas)//3)*2):
			obts = (self.filas * self.columnas)//3
		while True:
			a_x, a_y = random.randint(0,self.filas-1), random.randint(0,self.columnas-1)
			m_x, m_y = random.randint(0,self.filas-1), random.randint(0,self.columnas-1)
			if a_x!=m_x and a_y!= m_y:
				self.axy[0], self.axy[1] = a_x, a_y
				self.mxy[0], self.mxy[1] = m_x, m_y
				break
		self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[2]
		self.mapa[self.mxy[0]][self.mxy[1]] = self.simbolos[3]
		cntdr = 0
		while cntdr < obts:
			x, y = random.randint(0,self.filas-1), random.randint(0,self.columnas-1)
			if self.mapa[x][y] == self.simbolos[0]:
				self.mapa[x][y] = self.simbolos[1]
				cntdr += 1

	def movimiento(self, movimientos):
		""" Documentacion para la funcion <movimiento>. """
		indice = 0
		menor = self.distancia(0,self.filas-1,0,self.columnas-1)
		mxy = self.mxy
		for i in range(len(movimientos)):
			if movimientos[i] != None:
				dxy = movimientos[i]
				if self.distancia(dxy[0],mxy[0],dxy[1],mxy[1]) < menor:
					indice = i
					menor = self.distancia(dxy[0],mxy[0],dxy[1],mxy[1])
		if indice == 0:
			self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[0]
			self.axy[0] = self.axy[0]-1
			self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[2]
			self.orientacion = 'N'
		elif indice == 1:
			self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[0]
			self.axy[0], self.axy[1] = self.axy[0]-1, self.axy[1]+1
			self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[2]
			self.orientacion = 'NE'
		elif indice == 2:
			self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[0]
			self.axy[1] = self.axy[1]+1
			self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[2]
			self.orientacion = 'E'
		elif indice == 3:
			self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[0]
			self.axy[0], self.axy[1] = self.axy[0]+1, self.axy[1]+1
			self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[2]
			self.orientacion = 'SE'
		elif indice == 4:
			self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[0]
			self.axy[0] = self.axy[0]+1
			self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[2]
			self.orientacion = 'S'
		elif indice == 5:
			self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[0]
			self.axy[0], self.axy[1] = self.axy[0]+1, self.axy[1]-1
			self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[2]
			self.orientacion = 'SO'
		elif indice == 6:
			self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[0]
			self.axy[1] = self.axy[1]-1
			self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[2]
			self.orientacion = 'O'
		elif indice == 7:
			self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[0]
			self.axy[0], self.axy[1] = self.axy[0]-1, self.axy[1]-1
			self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[2]
			self.orientacion = 'NO'

	def movimientos(self):
		""" Documentacion para la funcion <movimientos>. """
		movimientos = [None] * 8
		axy = self.axy
		f, c = self.filas, self.columnas
		mapa = self.mapa
		if (0 <= axy[0]-1 < f) and (0 <= axy[1] < c) and \
		(mapa[axy[0]-1][axy[1]] != self.simbolos[1]):	# N
			movimientos[0] = [axy[0]-1, axy[1]]
		if (0 <= axy[0]-1 < f) and (0 <= axy[1]+1 < c) and \
		(mapa[axy[0]-1][axy[1]+1] != self.simbolos[1]):	# NE
			movimientos[1] = [axy[0]-1, axy[1]+1]
		if (0 <= axy[0] < f) and (0 <= axy[1]+1 < c) and \
		(mapa[axy[0]][axy[1]+1] != self.simbolos[1]):	# E
			movimientos[2] = [axy[0], axy[1]+1]
		if (0 <= axy[0]+1 < f) and (0 <= axy[1]+1 < c) and \
		(mapa[axy[0]+1][axy[1]+1] != self.simbolos[1]):	# SE
			movimientos[3] = [axy[0]+1, axy[1]+1]
		if (0 <= axy[0]+1 < f) and (0 <= axy[1] < c) and \
		(mapa[axy[0]+1][axy[1]] != self.simbolos[1]):	# S
			movimientos[4] = [axy[0]+1, axy[1]]
		if (0 <= axy[0]+1 < f) and (0 <= axy[1]-1 < c) and \
		(mapa[axy[0]-1][axy[1]-1] != self.simbolos[1]):	# SO
			movimientos[5] = [axy[0]+1, axy[1]-1]
		if (0 <= axy[0] < f) and (0 <= axy[1]-1 < c) and \
		(mapa[axy[0]][axy[1]-1] != self.simbolos[1]):	# O
			movimientos[6] = [axy[0], axy[1]-1]
		if (0 <= axy[0]-1 < f) and (0 <= axy[1]-1 < c) and \
		(mapa[axy[0]-1][axy[1]-1] != self.simbolos[1]):	# NO
			movimientos[7] = [axy[0]-1, axy[1]-1]
		print movimientos
		return movimientos

	def distancia(self, x1, x2, y1, y2):
		""" Documentacion para la funcion <distancia>. """
		return math.sqrt(((x2-x1)**2)+((y2-y1)**2))

	def mostrar_mapa(self):
		""" Documentacion para la funcion <mostrar_mapa>. """
		for i in range(self.filas):
			for j in range(self.columnas):
				print self.mapa[i][j] + " ",
			print


if __name__ == '__main__':
	simulador = Simulador(27,18," ",".")
	simulador.poblar_mapa()
	contador = 0
	while True:
		contador += 1
		os.system('clear')
		simulador.mostrar_mapa()
		print simulador.axy
		simulador.movimiento(simulador.movimientos())
		if simulador.axy == simulador.mxy:
			print "Meta alcanzada..."
			break
		time.sleep(1)
	print "Movimientos:", contador
