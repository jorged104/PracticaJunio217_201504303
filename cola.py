from graphviz import Digraph

class nodosimple():
	"""docstring for nodosimple"""
	def __init__(self,dato,indice):
		super(nodosimple, self).__init__()
		self.dato = dato
		self.nodosiguiente	=  None
		self.indice = indice

class cola():
	def __init__(self):
		self.cabeza = None
	def push(self,dato):
		nuevo = nodosimple(dato,0)
		if self.cabeza == None:
			self.cabeza = nuevo
		else:
			aux = self.cabeza
			while aux.nodosiguiente != None:
				aux = aux.nodosiguiente
			aux.nodosiguiente = nuevo
	def pop(self):
		if(self.cabeza != None):
			aux = self.cabeza
			self.cabeza = self.cabeza.nodosiguiente
			return aux.dato
		else:
			print("-* La cola esta vacia *-")	
	def imprimir(self):
		aux = self.cabeza
		cola = ""
		while aux != None:
			if(aux.nodosiguiente == None):
				cola = cola + str(aux.dato)
			else:	
				cola = cola + str(aux.dato) + "  ->  "
			aux = aux.nodosiguiente	
		print ( "\n " + cola + "\n")	
	def graficar(self):
		dot = Digraph()
		if self.cabeza != None:
			dot.node('cabeza',"cabeza "+self.cabeza.dato)
			dot.node('null','nulo')
			aux = self.cabeza
			diferenciador = 0
			while aux.nodosiguiente != None:
				aux = aux.nodosiguiente
				dot.node(str(aux.dato)+str(diferenciador),str(aux.dato))
				diferenciador = diferenciador + 1
		#dot.node(str(aux.dato),str(aux.dato))	
			if self.cabeza.nodosiguiente != None:
				dot.edge('cabeza',str(self.cabeza.nodosiguiente.dato)+str(0))
				aux = self.cabeza.nodosiguiente
				diferenciador = 0
				while aux.nodosiguiente != None:
					dot.edge(str(aux.dato)+str(diferenciador),str(aux.nodosiguiente.dato)+str(diferenciador+1))
					diferenciador = diferenciador + 1
					aux = aux.nodosiguiente
			
				dot.edge(str(aux.dato)+str(diferenciador),"null")
		else:
			dot.node('cabeza','Null')	
		dot.format = 'png' 
		dot.render('cola')	
		return dot.source			
