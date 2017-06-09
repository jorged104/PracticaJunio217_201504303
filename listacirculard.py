import cola
class nodolista():
	"""docstring for nodolista"""
	def __init__(self,nombre,contra):
		self.nombre = nombre	
		self.contra = contra
		self.matriz = None
		self.matrizT = None
		self.cola = None
		self.next = None
		self.prev = None
# ***********************************  GET AN SET ************ 	
	def setcola(cola):
		self.cola = cola
	def setmatrizT(matrizT):
		self.matrizT = matrizT
	def setmatriz(matriz):
		self.matriz = matriz
	def getmatriz():
		return self.matriz
	def getmatrizT(matrizT):
		return self.matrizT
	def getcola():
		return self.cola
	def getnombre():
		return self.nombre
	def getcontra():
		return self.contra		
#*************************************
class listaC():
	"""docstring for listaC"""
	def __init__(self):
		self.cabeza = None
	def insertar(self,nombre,contra):
		nuevo = nodolista(nombre,contra)
		if self.cabeza == None :
			nuevo.next = nuevo
			nuevo.prev = nuevo
			self.cabeza = nuevo
		else:
			nodotemp = None
			nodotemp = self.cabeza.prev
			nuevo.prev = nodotemp
			nodotemp.next = nuevo
			nuevo.next = self.cabeza
			self.cabeza.prev = nuevo
	def imprimir(self):
		if self.cabeza != None:
			usuarios = ""
			nodotemp = self.cabeza
			#print("El nombre del usuario "+ nodotemp.nombre + " contra " +nodotemp.contra)
			#usuarios = usuarios +  nodotemp.nombre +" -> "
			nodotemp = nodotemp.prev
			if nodotemp != None:
				while nodotemp != self.cabeza:
					#print("El nombre del usuario "+ nodotemp.nombre + " contra " +nodotemp.contra)
					usuarios = usuarios + nodotemp.nombre + " ->"
					nodotemp = nodotemp.prev
				usuarios = usuarios +  self.cabeza.nombre +" -> " + self.cabeza.prev.nombre
				print(usuarios)
				usuarios2 = self.cabeza.nombre + "->"
				nodotemp = self.cabeza.next		
				while nodotemp != self.cabeza:
					#print("El nombre del usuario "+ nodotemp.nombre + " contra " +nodotemp.contra)
					usuarios2 = usuarios2 + nodotemp.nombre + " ->"
					nodotemp = nodotemp.next
				usuarios2 = usuarios2 +  self.cabeza.nombre 
				print(usuarios2)		
	def buscar(self,nombre):
		if self.cabeza != None:
			nodotemp = self.cabeza
			if nodotemp.nombre == nombre:
				return nodotemp
			nodotemp = nodotemp.prev
			if nodotemp != None:
				while nodotemp != self.cabeza:
					if nodotemp.nombre== nombre:
						return nodotemp
					nodotemp = nodotemp.prev