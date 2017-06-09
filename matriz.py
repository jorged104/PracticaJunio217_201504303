class nodoM():
	"""docstring for nodoM"""
	def __init__(self):
		self.data = None
		self.arriba = None
		self.abajo = None
		self.derecha = None
		self.izquierda = None
		self.x = 0
		self.y = 0
class matrizOrtogonal():
	def __init__(self):
		self.cabeza = nodoM()
		self.x = None
		self.y = None
	def crearmatriz(self,tamx,tamy):
		contadory = 0
		contadorx = 1
		self.x = tamx
		self.y = tamy
		nodoaux = self.cabeza
		while contadory < tamy:
			tempAuxX = nodoaux
			while contadorx < tamx:
				
				nuevo = nodoM()
				nuevo.x = contadorx
				nuevo.y = contadory
				tempAuxX.derecha = nuevo
				nuevo.izquierda = tempAuxX
				tempAuxX = nuevo
				#print("Insertando y : " + str(contadory)  + " x: " + str(contadorx))
				contadorx = contadorx + 1
			
			if ( (contadory +1 )!= tamy):	
				contadorx = 0
				contadory = contadory + 1
				nuevoY = nodoM()
				nuevoY.x = contadorx
				nuevoY.y = contadory
				nodoaux.abajo = nuevoY
				nuevoY.arriba = nodoaux
				nodoaux = nuevoY
				#print("Insertando y : " + str(contadory)  + " x: " + str(contadorx)+ " Se creoo en y ")			
				contadorx = 1
			else:
				contadory = contadory + 1	
			
	def imprimir(self):
		nodoaux = self.cabeza
		while nodoaux != None:
			nodotempX = nodoaux
			linea = "| "
			while nodotempX != None:
				linea = linea + " "+str(nodotempX.data)+" |" 
				#print("Estoy en el nodito x: " + str(nodotempX.x) + " y: " + str(nodotempX.y) + " dato "+ str(nodotempX.data))
				nodotempX = nodotempX.derecha
			print(linea)	
			nodoaux = nodoaux.abajo
#************* Funcion buscar ******************************************************************		
	def buscar(self,data):
		nodoaux = self.cabeza
		while nodoaux != None:
			nodotempX = nodoaux
			while nodotempX != None:
				if ( nodotempX.data == data):
					return nodotempX
				nodotempX = nodotempX.derecha
			nodoaux = nodoaux.abajo
#************* Funcion obtener ******************************************************************
	def Obtener(self,x,y):
		nodoaux = self.cabeza
		while nodoaux != None:
			nodotempX = nodoaux
			while nodotempX != None:
				if ( nodotempX.x == int(x) and nodotempX.y == int(y)):
					return nodotempX
				nodotempX = nodotempX.derecha
			nodoaux = nodoaux.abajo
#*************** Setear datos *********************************************************************
	def set(self,x,y,data):
		nodoaux = self.cabeza
		while nodoaux != None:
			nodotempX = nodoaux
			while nodotempX != None:
				#print("Estoy en el nodito x: " + str(nodotempX.x) + " y: " + str(nodotempX.y) + " dato "+ str(nodotempX.data))
				if ( nodotempX.x == int(x) and nodotempX.y == int(y)):
					nodotempX.data = data
					#print("se disque iserto el dato " + data)
				nodotempX = nodotempX.derecha
			nodoaux = nodoaux.abajo				


						
		