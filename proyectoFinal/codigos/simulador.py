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
	def __init__(self, dim_x=8, dim_y=8, pscn=".", obst="O", agnt="R", mta="M"):
		""" (Pseudo)Constructor de la clase <Simulador>. """
		self.filas = dim_y
		self.columnas = dim_x
		self.orientacion = 'N'
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
		orientacion = ''
		xy = self.agente_xy
		if self.orientacion == 'N':
			xyn = [xy[0]-1, xy[1]]
			if 0<=xyn[0]<self.filas and 0<=xyn[1]<self.columnas and self.mapa[xyn[0]][xyn[1]]!=self.simbolos[1]:
				movimientos[0] = xyn
			xyn = [xy[0], xy[1]+1]
			if 0<=xyn[0]<self.filas and 0<=xyn[1]<self.columnas and self.mapa[xyn[0]][xyn[1]]!=self.simbolos[1]:
				movimientos[1] = xyn
				if not movimientos[0]:
					orientacion = 'E'
			xyn = [xy[0], xy[1]-1]
			if 0<=xyn[0]<self.filas and 0<=xyn[1]<self.columnas and self.mapa[xyn[0]][xyn[1]]!=self.simbolos[1]:
				movimientos[2] = xyn
				if not movimientos[0]:
					orientacion = 'O'
			xyn = [xy[0]+1, xy[1]]
			if 0<=xyn[0]<self.filas and 0<=xyn[1]<self.columnas and self.mapa[xyn[0]][xyn[1]]!=self.simbolos[1]:
				movimientos[3] = xyn
				if not movimientos[0]:
					orientacion = 'S'
		elif self.orientacion == 'E':
			xyn = [xy[0], xy[1]+1]
			if 0<=xyn[0]<self.filas and 0<=xyn[1]<self.columnas and self.mapa[xyn[0]][xyn[1]]!=self.simbolos[1]:
				movimientos[0] = xyn
			xyn = [xy[0]+1, xy[1]]
			if 0<=xyn[0]<self.filas and 0<=xyn[1]<self.columnas and self.mapa[xyn[0]][xyn[1]]!=self.simbolos[1]:
				movimientos[1] = xyn
				if not movimientos[0]:
					orientacion = 'S'
			xyn = [xy[0]-1, xy[1]]
			if 0<=xyn[0]<self.filas and 0<=xyn[1]<self.columnas and self.mapa[xyn[0]][xyn[1]]!=self.simbolos[1]:
				movimientos[2] = xyn
				if not movimientos[0]:
					orientacion = 'N'
			xyn = [xy[0], xy[1]-1]
			if 0<=xyn[0]<self.filas and 0<=xyn[1]<self.columnas and self.mapa[xyn[0]][xyn[1]]!=self.simbolos[1]:
				movimientos[3] = xyn
				if not movimientos[0]:
					orientacion = 'O'
		elif self.orientacion == 'O':
			xyn = [xy[0], xy[1]-1]
			if 0<=xyn[0]<self.filas and 0<=xyn[1]<self.columnas and self.mapa[xyn[0]][xyn[1]]!=self.simbolos[1]:
				movimientos[0] = xyn
			xyn = [xy[0]-1, xy[1]]
			if 0<=xyn[0]<self.filas and 0<=xyn[1]<self.columnas and self.mapa[xyn[0]][xyn[1]]!=self.simbolos[1]:
				movimientos[1] = xyn
				if not movimientos[0]:
					orientacion = 'N'
			xyn = [xy[0]+1, xy[1]]
			if 0<=xyn[0]<self.filas and 0<=xyn[1]<self.columnas and self.mapa[xyn[0]][xyn[1]]!=self.simbolos[1]:
				movimientos[2] = xyn
				if not movimientos[0]:
					orientacion = 'S'
			xyn = [xy[0], xy[1]+1]
			if 0<=xyn[0]<self.filas and 0<=xyn[1]<self.columnas and self.mapa[xyn[0]][xyn[1]]!=self.simbolos[1]:
				movimientos[3] = xyn
				if not movimientos[0]:
					orientacion = 'E'
		elif self.orientacion == 'S':
			xyn = [xy[0]+1, xy[1]]
			if 0<=xyn[0]<self.filas and 0<=xyn[1]<self.columnas and self.mapa[xyn[0]][xyn[1]]!=self.simbolos[1]:
				movimientos[0] = xyn
			xyn = [xy[0], xy[1]-1]
			if 0<=xyn[0]<self.filas and 0<=xyn[1]<self.columnas and self.mapa[xyn[0]][xyn[1]]!=self.simbolos[1]:
				movimientos[1] = xyn
				if not movimientos[0]:
					orientacion = 'O'
			xyn = [xy[0], xy[1]+1]
			if 0<=xyn[0]<self.filas and 0<=xyn[1]<self.columnas and self.mapa[xyn[0]][xyn[1]]!=self.simbolos[1]:
				movimientos[2] = xyn
				if not movimientos[0]:
					orientacion = 'E'
			xyn = [xy[0]-1, xy[1]]
			if 0<=xyn[0]<self.filas and 0<=xyn[1]<self.columnas and self.mapa[xyn[0]][xyn[1]]!=self.simbolos[1]:
				movimientos[3] = xyn
				if not movimientos[0]:
					orientacion = 'N'
		self.orientacion = orientacion
		return movimientos

	def movimiento(self, movimientos):
		""" Documentacion para la funcion <movimiento>. """
		anterior = self.agente_xy
		if movimientos[0]:
			self.agente_xy = movimientos[0]
		elif movimientos[1]:
			self.agente_xy = movimientos[1]
		elif movimientos[2]:
			self.agente_xy = movimientos[2]
		elif movimientos[3]:
			self.agente_xy = movimientos[3]
		if self.agente_xy == self.meta_xy:
			return False
		else:
			self.mapa[self.agente_xy[0]][self.agente_xy[1]] = self.simbolos[2]
			self.mapa[anterior[0]][anterior[1]] = self.simbolos[0]
			print "Re-Dibuja agente...", self.agente_xy
			return True

	def mostrar_mapa(self):
		""" Documentacion para la funcion <mostrar_mapa>. """
		for i in range(self.filas):
			for j in range(self.columnas):
				print self.mapa[i][j] + " ",
			print


if __name__ == '__main__':
	simulador = Simulador(25,20," ",".")
	simulador.poblar_mapa()
	contador = 0
	while contador < 7:
		#os.system('clear')
		#print "=" * 80
		#simulador.mostrar_mapa()
		#print "Agente: ", simulador.agente_xy
		#print "=" * 80
		time.sleep(1)
		if simulador.movimiento(simulador.movimientos_posibles()):
			contador += 1
			continue
		else:
			print "Meta alcanzada"
			break