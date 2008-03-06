# -*- coding: iso-8859-1 -*-

#Autor: Roberto Vito Rodrigues Filho
#Data: 28/02/2008
#Descrição: Classe FiltroCH é a classe que implementa o filtro, nada mais é 
#           que um bean

class FiltroCH(object):
	def __init__(self):
		self.__adicionar = False
		self.__editar = False
		self.__consultar = False
		self.__remover = False
		self.__imprimir = False
		self.__emitirOS = False
		self.__selecionaveis = False

	def setAdicionar(self,botao):
		self.__adicionar = botao
	
	def getAdicionar(self):
		return self.__adicionar

	def setEditar(self,botao):
		self.__editar = botao

	def getEditar(self):
		return self.__editar
	
	def setConsultar(self,botao):
		self.__consultar = botao
	
	def getConsultar(self):
		return self.__consultar	

	def setRemover(self,botao):
		self.__remover = botao	

	def getRemover(self):
		return self.__remover	

	def setImprimir(self,botao):
		self.__imprimir = botao

	def getImprimir(self):
		return self.__imprimir	

	def setEmitirOS(self,botao):
		self.__emitirOS = botao	

	def getEmitirOS(self):
		return self.__emitirOS

	def setSelecionaveis(self,botao):
		self.__selecionaveis = botao

	def getEditar(self):
		return self.__selecionaveis
