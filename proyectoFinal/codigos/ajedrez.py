"""
...
"""

pnt = "."
rbt = "R"
obst = "O"

tablero = []
for i in range(8):
	fila = []
	for j in range(8):
		columna = [pnt] * 8
	tablero.append(columna)

tablero[0][2], tablero[0][7], tablero[1][0] = obst, obst, obst
tablero[1][6], tablero[2][2], tablero[2][4] = obst, obst, obst
tablero[3][1], tablero[4][2], tablero[4][4] = obst, obst, obst
tablero[4][6], tablero[5][0], tablero[5][5] = obst, obst, obst
tablero[5][7], tablero[6][1], tablero[7][3] = obst, obst, obst
tablero[7][7], tablero[5][3] = obst, rbt

for fila in tablero:
	for casilla in fila:
		print casilla + "\t",
	print "\n"