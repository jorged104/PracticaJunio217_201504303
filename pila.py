from graphviz import Digraph
import listacirculard
class nodosimple():
	"""docstring for nodosimple"""
	def __init__(self,dato,indice):
		super(nodosimple, self).__init__()
		self.dato = dato
		self.nodosiguiente	=  None
		self.indice = indice
class pila():
	def __init__(self):
		self.cabeza = None
	def push(self,dato):
		nuevo = nodosimple(dato,0)
		if self.cabeza == None:
			self.cabeza = nuevo
		else:
			nuevo.nodosiguiente = self.cabeza
			self.cabeza = nuevo
	def pop(self):
		if self.cabeza != None:
			aux = None
			aux = self.cabeza
			self.cabeza = self.cabeza.nodosiguiente
			return aux.dato
		return "null"	
	def peek(self):
		if self.cabeza != None:
			return self.cabeza.dato
	def graficar(self):
		if self.cabeza != None:
			dot = Digraph('structs',node_attr={'shape':'plaintext'})

			aux = self.cabeza
			tabla = '<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">'
			while aux != None:
				tabla = tabla + '<TR><TD>'+aux.dato+'</TD></TR>'
				aux = aux.nodosiguiente
			tabla = tabla + '</TABLE>>'	
			dot.node('structura1',tabla)
			dot.format = 'png' 
			dot.render('PILA')
			return dot.source

