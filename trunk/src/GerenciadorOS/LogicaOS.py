# -*- coding: iso-8859-1 -*-

__version__="0.1"

#from ..MBD import Consulta,ManipuladorBD

"""
Autor: Henrique Eiji Mikado
Data: 06/03/2008
"""

class LogicaOS:
    """
    Esta classe será responsável por toda a lógica do Gerenciador de OS.
    """

    #Atributo da classe
	self.consulta = Consulta()

    @returnType()
    @parameterTypes(selfType, dict)
    def realizaAdicao(lista):
        """
        Recebe um dicionário contendo os dados e insere-os no objeto Consulta
        junto com o seu modo, para ser enviado ao módulo MBD a fim de
        cadastrar uma OS.
        """

        consulta.setDictConsulta(lista)
        consulta.setModoConsulta('os')
        ok = gravaBD(consulta)

    @returnType()
    @parameterTypes(selfType, dict)
    def realizaEdicao(lista):
        """
        Recebe um dicionário contendo os dados e insere-os no objeto Consulta
        junto com o seu modo, para ser enviado ao módulo MBD a fim de editar
        uma OS.
        """

        consulta.setDictConsulta(lista)
        consulta.setModoConsulta('os')
        ok = alteraBD(consulta)

    @returnType()
    @parameterTypes(selfType, dict)
    def realizaConsulta(lista):
        """
        Recebe um dicionário contendo os dados e insere-os no objeto Consulta
        junto com o seu modo, para ser enviado ao módulo MBD a fim de obter
        uma consulta de OSs.
        """

        consulta.setDictConsulta(lista)
        consulta.setModoConsulta('os')
        ok = consultaBD(consulta)

    @returnType()
    @parameterTypes(selfType, dict)
    #def realizaImpressao(lista):
        """
        Insere os dados do dicionário recebido em um arquivo pdf, gerando
        um OS. Além disso, esse arquivo será executado, podendo assim,
        ser imprimido.
        """
        
    @returnType()
    @parameterTypes(selfType, dict)
    #def emiteOS(lista):
