# -*- coding: ISO-8859-1 -*-

#Autor: Roberto Vito Rodrigues Filho
#Data: 28/02/2008
#Descrição: Classe InterfaceGraficaCH é a classe que implementa a interface gráfica do gerenciador de chamadas de acordo com o design v.0.3

import gtk
import pygtk
import gtk.glade
import gobject

class InterfaceGraficaCH(object):
	def __init__(self,filtroCH):
		#Filtro & InterfaceGrafica
		self.__filtroCH = filtroCH
		self.__interfaceGrafica = gtk.glade.XML("interfacegrafica.glade")
		#BarraDeProgresso
		self.__barraDeProgresso = self.__interfaceGrafica("barraDeProgresso")
		self.__timer = gobject.timeout_add (100, self.disparaPulso)
		#Telas
		self.__telaCH = self.__interfaceGrafica.get_widget("telaCH")
		self.__telaPrincipalCH = self.__interfaceGrafica.get_widget("telaPrincipalCH")
		self.__telaAdicionarCH = self.__interfaceGrafica.get_widget("telaAdicionarCH")
		self.__telaEditarCH = self.__interfaceGrafica.get_widget("telaEditarCH")
		self.__telaSelecionaveisCH = self.__interfaceGrafica.get_widget("telaSelecionaveisCH")
		self.__telaVisualizarCH = self.__interfaceGrafica.get_widget("telaVisualizarCH")
		self.__telaConsultarCH = self.__interfaceGrafica.get_widget("telaConsultarCH")
		#Botões telaPrincipalCH
		self.__botaoAdicionarCH = self.__interfaceGrafica.get_widget("botaoAdicionarCH")
		self.__botaoConsultarCH = self.__interfaceGrafica.get_widget("botaoConsultarCH")
		self.__botaoCancelarCH = self.__interfaceGrafica.get_widget("botaoCancelarCH")
		self.__botaoEditarCH = self.__interfaceGrafica.get_widget("botaoEditarCH")
		self.__botaoRemoverCH = self.__interfaceGrafica.get_widget("botaoRemoverCH")
		self.__botaoVisualizarCH = self.__interfaceGrafica.get_widget("botaoVisualizarCH")
		self.__botaoSelecionaveisCH = self.__interfaceGrafica.get_widget("botaoSelecionaveisCH")
		self.__botaoImprimirCH = self.__interfaceGrafica.get_widget("botaoImprimirCH")
		self.__botaoEmitirOSCH = self.__interfaceGrafica.get_widget("botaoEmitirOSCH")
		#Não precisa ter botões de todas as telas, pois seus eventos estarão sendo tratados no dicionário

	def mapeiaFiltro(self):
		#Telas		
		self.__telaCH.show()
		self.__telaPrincipalCH.show()
		self.__telaAdicionarCH.hide()
		self.__telaEditarCH.hide()
		self.__telaSelecionaveisCH.hide()
		self.__telaVisualizarCH.hide()
		self.__telaConsultarCH.hide()
		#Botões
		self.__botaoCancelar.show()
		if (self.__filtroCH.getAdicionar()):
			self.__botaoAdicionarCH.show()
		else:
			self.__botaoAdicionarCH.hide()
		
		if (self.__filtroCH.getConsultar()):
			self.__botaoConsultarCH.show()
		else:
			self.__botaoConsultarCH.hide()

		if (self.__filtroCH.getEditar()):
			self.__botaoEditarCH.show()
		else:
			self.__botaoEditarCH.hide()

		if (self.__filtroCH.getVisualizar()):
			self.__botaoVisualizarCH.show()
		else:
			self.__botaoVisualizarCH.hide()

		if (self.__filtroCH.getSelecionaveis()):
			self.__botaoSelecionaveisCH.show()
		else
			self.__botaoSelecionaveisCH.hide()

		if (self.__filtroCH.getImprimirCH()):
			self.__botaoImprimirCH.show()
		else
			self.__botaoImprimirCH.hide()

		if (self.__filtroCH.getEmitirOS()):
			self.__botaoEmitirOS.show()
		else
			self.__botaoEmitirOS.hide()

	def handlerAdicionar(self):
		self.__telaPrincipalCH.hide()
		self.__telaAdicionarCH.show()

	def handlerConsultar(self):
		self.__tela

	def handlerCancelar(self):
		print oie

	def handlerEditar(self):
		print oie

	def handlerRemover(self):
		print oie

	def handlerVisualizar(self):
		print oie

	def handlerSelecionaveis(self):
		print oie

	def handlerImprimir(self):
		print oie

	def handlerEmitirOS(self):
		print oie

	def okConsultar(self):
		print oie

	def okEditar(self):
		print oie

	def okAdicionar(self):
		print oie

	def confirmaRemocao(self):
		print oie

	def inserirSelecionaveis(self):
		print oie

	def removerSelecionaveis(self):
		print oie

	def editarSelecionaveis(self):
		print oie

	def verificaDadosAdicionar(self):
		print oie

	def verificaDadosEditar(self):
		print oie

	def disparaPulso(self):
		self.__barraDeProgresso.pusle()
		return True

	def destroiBarraDeProgresso(self):
		gobject.source_remove(self.timer)
        	self.__timer = 0
		self.__barraDeProgresso.hide()
