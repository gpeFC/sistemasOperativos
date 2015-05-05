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
	def __init__(self, dim_x=8, dim_y=8, pscn=".", obst="O", agnt="X", mta="M"):
		""" (Pseudo)Constructor de la clase <Simulador>. """
		self.filas = dim_y
		self.columnas = dim_x
		self.orientacion = "N"
		self.simbolos = (str(pscn), str(obst), str(agnt), str(mta))
		self.agente_xy = [0, 0]
		self.meta_xy = [0, 0]
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
				self.agente_xy[0], self.agente_xy[1] = a_x, a_y
				self.meta_xy[0], self.meta_xy[1] = m_x, m_y
				break
		self.mapa[self.agente_xy[0]][self.agente_xy[1]] = self.simbolos[2]
		self.mapa[self.meta_xy[0]][self.meta_xy[1]] = self.simbolos[3]
		cntdr = 0
		while cntdr < obts:
			x, y = random.randint(0,self.filas-1), random.randint(0,self.columnas-1)
			if self.mapa[x][y] == self.simbolos[0]:
				self.mapa[x][y] = self.simbolos[1]
				cntdr += 1

	def movimientos_posibles(self):
		""" Documentacion para la funcion <movimientos_posibles>. """
		movimientos = [None, None, None, None]
		xy = self.agente_xy
		if self.orientacion == 'N':
			xyn = [xy[0]+1, xy[1]]
			if 0<=xyn[0]<self.filas and 0<=xyn[1]<self.columnas and self.mapa[xyn[0]][xyn[1]]!=self.simbolos[1]:
				movimientos[0] = xyn
			xyn = [xy[0], xy[1]+1]
			if 0<=xyn[0]<self.filas and 0<=xyn[1]<self.columnas and self.mapa[xyn[0]][xyn[1]]!=self.simbolos[1]:
				movimientos[1] = xyn
			xyn = [xy[0], xy[1]-1]
			if 0<=xyn[0]<self.filas and 0<=xyn[1]<self.columnas and self.mapa[xyn[0]][xyn[1]]!=self.simbolos[1]:
				movimientos[2] = xyn
			xyn = [xy[0]-1, xy[1]]
			if 0<=xyn[0]<self.filas and 0<=xyn[1]<self.columnas and self.mapa[xyn[0]][xyn[1]]!=self.simbolos[1]:
				movimientos[3] = xyn
		elif self.orientacion == 'E':
			pass
		elif self.orientacion == 'O':
			pass
		elif self.orientacion == 's':
			pass
		return movimientos

	def mostrar_mapa(self):
		""" Documentacion para la funcion <mostrar_mapa>. """
		for i in range(self.filas):
			for j in range(self.columnas):
				print self.mapa[i][j] + " ",
			print


if __name__ == '__main__':
	simulador = Simulador()
	simulador.mostrar_mapa()
	simulador.poblar_mapa()
	print
	simulador.mostrar_mapa()
	print