from xml.dom import minidom
import listacirculard
import matriz
import cola
import pila
class principal:
	def __init__(self):
		self.usuario = listacirculard.listaC()
		self.ciclo = True
		self.usuarioUsando = None
	def Salir(self):
		return False
	def LeerArchivo(self):
		#lectrura de xml
		lineas = ""
		try :
			archivo = input(" Ingrese el nombre del archivo .xml ")
		except KeyError:	
			archivo =  "archivo.xml"
		try:
			for line in open(archivo,"r"):
				lineas = lineas + line
			xmldoc = minidom.parseString(lineas)
			if self.usuarioUsando.cola == None:
				colatemp = cola.cola()
				self.usuarioUsando.cola = colatemp
			itemlist = xmldoc.getElementsByTagName("operacion")
			x = None
			y = None
			for j in xmldoc.getElementsByTagName("x"):
				s = j.firstChild.nodeValue
				s = s.strip('\t\n\r')
				x = s
			for k in xmldoc.getElementsByTagName("y"):
				s = k.firstChild.nodeValue
				s = s.strip('\t\n\r')
				y = s
			if self.usuarioUsando.matriz == None:
				nuevamatriz = matriz.matrizOrtogonal()
				nuevamatriz.crearmatriz(int(x),int(y))
				self.usuarioUsando.matriz = nuevamatriz
				print(" Se crea una matriz con dimenciones x : " + str(x) + " y : " +str(y))
			for i in itemlist:
				s = i.firstChild.nodeValue
				s = s.strip('\t\n\r')
				self.usuarioUsando.cola.push(s)	
		except KeyError:
			print("error")

	def ResolverOperaciones(self):
		#Resolutor de operaciones
		consulta = True
		while consulta:
			print("\n**************************")
			print("\t 1) Operar siguiente ")
			print("\t 2) Regresar ")
			var = input()
			try:
				consulta  = ({'1': self.OperarSiguiente, '2': self.RegresarCicloOp}[var])()
				if consulta == None:
					consulta = True
			except KeyError:
				print ("Te di 2 Opciones escoge una !!!!")

	def OperarMatriz(self):
		#Operador de Matriz
		if self.usuarioUsando.matriz != None:
			ciclo2 = True
			while ciclo2:
				print("*******************Operar Matriz ****************")
				print("1 ) IngresarDato")
				print("2 ) Operar transpuesta")
				print("3 ) Mostrar matriz original")
				print("4 ) Mostras matriz transpuesta")
				print("5 ) regresar")
				var = input()
				try:
					ciclo2  = ({'1': self.IngresarDato, '2': self.Operartranspuesta,'3':self.MostrarMatrizOriginal,'4':self.MostrarTranspuesta,'5':self.RegresarOpMatriz}[var])()
					if ciclo2 == None:
						ciclo2 = True
				except KeyError:
					print ("Te di 6 Opciones escoge una !!!!")

	def MostrarUsuarios(self):
		#Muestra Los usuarios
		#print("Holitas")
		self.usuario.imprimir()
	def MostrarCola(self):
		#Muestra la cola de operaciones del usuario
		#print("Holitas")
		if (self.usuarioUsando.cola != None ):
			self.usuarioUsando.cola.imprimir() 	
	def CerrarSecion(self):
		return False
	def CrearUsuario(self):
		nombre = input("\t Ingrese el nombre del usuario a crear  ")
		pas = input("\t Ingrese una password  ")
		if self.usuario.buscar(nombre) == None:
			self.usuario.insertar(nombre,pas)
		else:
			print( "**-- El usuario ya existe G.G  --**")
		#Crear Usuario
	def IngresoAlSistema(self):
		usuario = input("\t Ingrese un nombre de usuario ")
		pas = input("\t Ingrese su contrasena  ")
		# Validar usario  y mostrar el menu
		ustemp = self.usuario.buscar(usuario)
		if(ustemp != None):
			if(ustemp.contra  == pas):
				self.usuarioUsando = ustemp
				ciclo2 = True
				while ciclo2 :
					print("****************--Bienvenido-"+ usuario +"-*********************")
					print("\t 1) LeerArchivo")
					print("\t 2) Resolver Operaciones")
					print("\t 3) Operar la matriz")
					print("\t 4) Mostrar usuarios")
					print("\t 5) Mostrar colas")
					print("\t 6) Cerrar sesion")
					var = input()
					try:
						ciclo2  = ({'1': self.LeerArchivo, '2': self.ResolverOperaciones,'3':self.OperarMatriz,'4':self.MostrarUsuarios,'5':self.MostrarCola,'6':self.CerrarSecion}[var])()
						if ciclo2 == None:
							ciclo2 = True
					except KeyError:
						print ("Te di 6 Opciones escoge una !!!!")
			else:
				print("contra incorrecta WEE!!!! ")		
		else:
			print(" El usuario No existe GG ")				
	#------------------------------Opcion2ResolverOperaciones---------------------------------------
	def OperarSiguiente(self):
		#OperaElSiguienteEnCola
		#print("Holitas")
		if self.usuarioUsando.cola != None:
			operar = str(self.usuarioUsando.cola.pop())
			pilaOP = pila.pila()
			#agregardatos
			operar = operar.strip()
			print ( " Operacion : "  +  operar)
			print ( " Resolviendo....")
			dividido = operar.split(" ")
				#print (" Imprimir : " + str ( dividido[x] ))
			for x in range(len(dividido)):
				if (dividido[x] == "+" or dividido[x] == "-" or dividido[x] == "*" ):
					pilaOP.push(dividido[x])
					print ( " Push : " + dividido[x])
					operando = pilaOP.pop()
					print  ( "Pop  : " + str(operando))
					num1 = pilaOP.pop()
					print  ( "Pop  : " + str(num1))
					num2 = pilaOP.pop()
					print  ( "Pop  : " + str(num2))
					res = 0
					if( operando == "+"):
						res = int(num1) + int(num2)
					elif(operando == "-"):
						res = int(num2) - int(num1)	
					elif(operando == "*"):
						res = int(num1) * int(num2)
					print  ( "Push  : " + str(res))	
					pilaOP.push(res)						
				else:		
					pilaOP.push(dividido[x])
			print( " El resultado de la operacion es : " + str(pilaOP.peek()))		
	def RegresarCicloOp(self):
		return False
	#------------------------------Opcion3OperarMatriz-----------------------------------------------
	def IngresarDato(self):
		x = input(" Coordenada x : ")
		y = input (" Coordenada y : ")
		dato = input(" Ingrese un dato: ")
		self.usuarioUsando.matriz.set(x,y,dato)
		
		#Se ingresan los datos
	def Operartranspuesta(self):
		#Se opera la transpuesta
		if self.usuarioUsando.matriz != None:
			matristemp = matriz.matrizOrtogonal()
			matristemp.crearmatriz(self.usuarioUsando.matriz.y,self.usuarioUsando.matriz.x)
			conty = 0
			contx = 0
			while conty < int(matristemp.y):
				while contx < int(matristemp.x):
					matristemp.set(contx,conty,self.usuarioUsando.matriz.Obtener(conty,contx).data)
					#print("cambio :  " +str(self.usuarioUsando.matriz.Obtener(conty,contx).data) + " x :" +str(contx)+ "  y :" + str(conty) )
					contx = contx + 1
				conty = conty + 1
				contx = 0
			#matristemp.imprimir()
			self.usuarioUsando.matrizT = matristemp
			print("**********| Se creeo matriz Transpuesta |***********")				
		#print("Holitas")
	def MostrarMatrizOriginal(self):
		#se muestra la matriz origilanl
		if self.usuarioUsando.matriz != None:
			print("\n")
			self.usuarioUsando.matriz.imprimir()
			print("\n")
		else:
			print("\n ***! No exitse matriz creada weon !***")	
	def MostrarTranspuesta(self):
		#Se muestra la matriz transpuesta
		if self.usuarioUsando.matrizT != None:
			print("\n\n")
			self.usuarioUsando.matrizT.imprimir()
			print("\n\n")
		else:
			print("\n ***! No exitse matriz creada weon !***")	
		#print("Holitas")
	def RegresarOpMatriz(self):
		return  False
#--------------------------------------------------------------------------------------------------------

#usuario.insertar("jorge","daniel")
#usuario.insertar("danielM","danielito")
#usuario.insertar("danielM2","danielito2")
#usuario.imprimir()
#nuevamatriz = matriz.matrizOrtogonal()
#nuevamatriz.crearmatriz(1,1)
#nuevamatriz.imprimir()
	def inicio (self):
		
		while self.ciclo:  # Ciclo Menu 1 :
			
			print("****************--Menu--*********************")
			print("1) Crear Usuario")
			print("2) Ingresar al sistema")
			print("3) Salir del programa")
			var = input()
			try:
				self.ciclo = ({'1': self.CrearUsuario, '2': self.IngresoAlSistema,'3':self.Salir}[var])()
				if self.ciclo == None:
					self.ciclo = True
			except KeyError:
				print ("Te di 3 Opciones escoge una !!!!")

principal = principal()
principal.inicio()

