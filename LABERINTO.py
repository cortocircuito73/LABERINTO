from random import randint

if __name__ == '__main__':
	n = int()
	# DEFINIR LA MATRIZ
	while True:
		print("INGRESE LA DIMENSION DE LA MATRIZ: ", end="")
		n = int(input())
		if n<=0:
			print("")
			print("*** INGRESE DIMENSIONES VALIDAS ***")
			
		if n>0: break
	# INICIAR LA MATRIZ
	matriz = [[int() for ind0 in range(n)] for ind1 in range(n)]
	print("")
	# RELLENAR LA MATRIZ
	for f in range(1,n+1):
		for c in range(1,n+1):
			# BORDE DEL LABERINTO 
			if f==1 or f==n or c==1 or c==n:
				matriz[f-1][c-1] = 1
			# RELLENO DEL LABERINTO
			if f>2 and f<n-1 and c>2 and c<n-1:
				if f>=randint(0,n-1) or f<n-2 or c>=randint(0,n-1) or c<n-2:
					matriz[f-1][c-1] = randint(0,1)
				else:
					matriz[f-1][c-1] = randint(0,1)
			# CONDICIONALES DE CAMINOS
			if f>2 and c==2 and f<n-1:
				matriz[f-1][c-1] = randint(0,n-1)
			if f>2 and c==n-1 and f<n-1:
				matriz[f-1][c-1] = randint(0,n-1)
			if c>2 and f==2 and c<n-1:
				matriz[f-1][c-1] = randint(0,n-1)
			if c>2 and f==n-1 and c<n-1:
				matriz[f-1][c-1] = randint(0,n-1)
	# DEFINIR LA POSICION INCIAL/FINAL Y PAREDES
	for f in range(1,n+1):
		for c in range(1,n+1):
			if matriz[f-1][c-1]==0 or matriz[f-1][c-1]>=2:
				matriz[f-1][c-1] = 0
			else:
				matriz[f-1][c-1] = 1
	# DEFINIR INICIO Y FIN DEL LABERINTO
	matriz[1][1] = 2
	matriz[n-2][n-2] = 3
	# MOSTRAR EL LABERINTO
	for f in range(1,n+1):
		for c in range(1,n+1):
			if matriz[f-1][c-1]==0:
				print(" "," ", end="")
			else:
				if matriz[f-1][c-1]==2:
					print("S"," ", end="")
				else:
					if matriz[f-1][c-1]==3:
						print("X"," ", end="")
					else:
						print(matriz[f-1][c-1]," ", end="")
		print("")
	# PARADA Y SOLUCION
	sol = str()
	while True:
		print("")
		print("INGRESE S/s PARA VER LA SOLUCION DEL LABERINTO: ", end="")
		sol = input()
		if sol=="S" or sol=="s": break
	print("")
	# SOLUCION DEL LABERINTO
	if sol=="S" or sol=="s":
		a = int()
		a = 1
		while a<=7:
			# arriba-abajo
			for f in range(1,n+1):
				for c in range(1,n+1):
					if matriz[f-1][c-1]==2:
						# arriba
						if matriz[f-2][c-1]==0 or matriz[f-2][c-1]==3:
							matriz[f-2][c-1] = 2
						# izquierda
						if matriz[f-1][c]==0 or matriz[f-1][c]==3:
							matriz[f-1][c] = 2
						# abajo
						if matriz[f][c-1]==0 or matriz[f][c-1]==3:
							matriz[f][c-1] = 2
						# derecha
						if matriz[f-1][c-2]==0 or matriz[f-1][c-2]==3:
							matriz[f-1][c-2] = 2
			# abajo-arriba
			for f in range(n,0,-1):
				for c in range(n,0,-1):
					if matriz[f-1][c-1]==2:
						# arriba
						if matriz[f-2][c-1]==0 or matriz[f-2][c-1]==3:
							matriz[f-2][c-1] = 2
						# izquierda
						if matriz[f-1][c]==0 or matriz[f-1][c]==3:
							matriz[f-1][c] = 2
						# abajo
						if matriz[f][c-1]==0 or matriz[f][c-1]==3:
							matriz[f][c-1] = 2
						# derecha
						if matriz[f-1][c-2]==0 or matriz[f-1][c-2]==3:
							matriz[f-1][c-2] = 2
			# izq-der
			for c in range(n,0,-1):
				for f in range(n,0,-1):
					if matriz[f-1][c-1]==2:
						# arriba
						if matriz[f-2][c-1]==0 or matriz[f-2][c-1]==3:
							matriz[f-2][c-1] = 2
						# izquierda
						if matriz[f-1][c]==0 or matriz[f-1][c]==3:
							matriz[f-1][c] = 2
						# abajo
						if matriz[f][c-1]==0 or matriz[f][c-1]==3:
							matriz[f][c-1] = 2
						# derecha
						if matriz[f-1][c-2]==0 or matriz[f-1][c-2]==3:
							matriz[f-1][c-2] = 2
			a = a+1
	# MOSTRAR LABERINTO SOLUCIONADO
	for f in range(1,n+1):
		for c in range(1,n+1):
			if matriz[f-1][c-1]==0:
				print(" "," ", end="")
			else:
				if matriz[f-1][c-1]==2:
					print("."," ", end="")
				else:
					print(matriz[f-1][c-1]," ", end="")
		print("")
	print("")
	print("***** LABERINTO RESUELTO *****")

# BY CORTO_CIRCUITO
