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

	def movimiento(self):
		""" Documentacion para la funcion <movimiento>. """
		if self.orientacion == 'N':
			if 0<=self.axy[0]-1<self.filas and 0<=self.axy[1]<self.columnas and self.mapa[self.axy[0]-1][self.axy[1]]!=self.simbolos[1]:
				self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[0]
				self.axy[0] = self.axy[0]-1
				self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[2]
			elif 0<=self.axy[0]<self.filas and 0<=self.axy[1]+1<self.columnas and self.mapa[self.axy[0]][self.axy[1]+1]!=self.simbolos[1]:
				self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[0]
				self.axy[1] = self.axy[1]+1
				self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[2]
				self.orientacion = 'E'
			elif 0<=self.axy[0]<self.filas and 0<=self.axy[1]-1<self.columnas and self.mapa[self.axy[0]][self.axy[1]-1]!=self.simbolos[1]:
				self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[0]
				self.axy[1] = self.axy[1]-1
				self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[2]
				self.orientacion = 'O'
			elif 0<=self.axy[0]+1<self.filas and 0<=self.axy[1]<self.columnas and self.mapa[self.axy[0]+1][self.axy[1]]!=self.simbolos[1]:
				self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[0]
				self.axy[0] = self.axy[0]+1
				self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[2]
				self.orientacion = 'S'
		elif self.orientacion == 'E':
			if 0<=self.axy[0]<self.filas and 0<=self.axy[1]+1<self.columnas and self.mapa[self.axy[0]][self.axy[1]+1]!=self.simbolos[1]:
				self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[0]
				self.axy[1] = self.axy[1]+1
				self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[2]
			elif 0<=self.axy[0]+1<self.filas and 0<=self.axy[1]<self.columnas and self.mapa[self.axy[0]+1][self.axy[1]]!=self.simbolos[1]:
				self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[0]
				self.axy[0] = self.axy[0]+1
				self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[2]
				self.orientacion = 'S'
			elif 0<=self.axy[0]-1<self.filas and 0<=self.axy[1]<self.columnas and self.mapa[self.axy[0]-1][self.axy[1]]!=self.simbolos[1]:
				self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[0]
				self.axy[0] = self.axy[0]-1
				self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[2]
				self.orientacion = 'N'
			elif 0<=self.axy[0]<self.filas and 0<=self.axy[1]-1<self.columnas and self.mapa[self.axy[0]][self.axy[1]-1]!=self.simbolos[1]:
				self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[0]
				self.axy[1] = self.axy[1]-1
				self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[2]
				self.orientacion = 'O'
		elif self.orientacion == 'O':
			if 0<=self.axy[0]<self.filas and 0<=self.axy[1]-1<self.columnas and self.mapa[self.axy[0]][self.axy[1]-1]!=self.simbolos[1]:
				self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[0]
				self.axy[1] = self.axy[1]-1
				self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[2]
			elif 0<=self.axy[0]-1<self.filas and 0<=self.axy[1]<self.columnas and self.mapa[self.axy[0]-1][self.axy[1]]!=self.simbolos[1]:
				self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[0]
				self.axy[0] = self.axy[0]-1
				self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[2]
				self.orientacion = 'N'
			elif 0<=self.axy[0]+1<self.filas and 0<=self.axy[1]<self.columnas and self.mapa[self.axy[0]+1][self.axy[1]]!=self.simbolos[1]:
				self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[0]
				self.axy[0] = self.axy[0]+1
				self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[2]
				self.orientacion = 'S'
			elif 0<=self.axy[0]<self.filas and 0<=self.axy[1]+1<self.columnas and self.mapa[self.axy[0]][self.axy[1]+1]!=self.simbolos[1]:
				self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[0]
				self.axy[1] = self.axy[1]+1
				self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[2]
				self.orientacion = 'E'
		elif self.orientacion == 'S':
			if 0<=self.axy[0]+1<self.filas and 0<=self.axy[1]<self.columnas and self.mapa[self.axy[0]+1][self.axy[1]]!=self.simbolos[1]:
				self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[0]
				self.axy[0] = self.axy[0]+1
				self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[2]
			elif 0<=self.axy[0]<self.filas and 0<=self.axy[1]-1<self.columnas and self.mapa[self.axy[0]][self.axy[1]-1]!=self.simbolos[1]:
				self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[0]
				self.axy[1] = self.axy[1]-1
				self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[2]
				self.orientacion = 'O'
			elif 0<=self.axy[0]<self.filas and 0<=self.axy[1]+1<self.columnas and self.mapa[self.axy[0]][self.axy[1]+1]!=self.simbolos[1]:
				self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[0]
				self.axy[1] = self.axy[1]+1
				self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[2]
				self.orientacion = 'E'
			elif 0<=self.axy[0]-1<self.filas and 0<=self.axy[1]<self.columnas and self.mapa[self.axy[0]-1][self.axy[1]]!=self.simbolos[1]:
				self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[0]
				self.axy[0] = self.axy[0]-1
				self.mapa[self.axy[0]][self.axy[1]] = self.simbolos[2]
				self.orientacion = 'N'

	def mostrar_mapa(self):
		""" Documentacion para la funcion <mostrar_mapa>. """
		for i in range(self.filas):
			for j in range(self.columnas):
				print self.mapa[i][j] + " ",
			print


if __name__ == '__main__':
	simulador = Simulador(8,8," ",".")
	simulador.poblar_mapa()
	contador = 0
	#while contador < 15:
	while True:
		os.system('clear')
		simulador.mostrar_mapa()
		simulador.movimiento()
		if simulador.axy == simulador.mxy:
			print "Meta alcanzada"
			break
		time.sleep(1)
		contador += 1