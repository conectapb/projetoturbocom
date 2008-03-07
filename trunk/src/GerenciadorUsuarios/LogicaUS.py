# -*- coding: iso-8859-1 -*-

__version__="0.1"

#from ..MBD import Consulta,ManipuladorBD

"""
Autor: Henrique Eiji Mikado
Data: 06/03/2008
"""

class LogicaUS:
    """
    Esta classe será responsável por toda a lógica do Gerenciador de Usuários.
    """

    #Atributo da classe
	self.consulta = Consulta()

    @returnType()
    @parameterTypes(selfType, dict)
    def realizaAdicao(lista):
        """
        Recebe um dicionário contendo os dados e insere-os no objeto Consulta
        junto com o seu modo, para ser enviado ao módulo MBD a fim de
        cadastrar um usuário.
        """
        consulta.setValorConsulta(lista)
        consulta.setModoConsulta('cl')
        ok = gravaBD(consulta)

    @returnType()
    @parameterTypes(selfType, dict)
    def realizaEdicao(lista):
        """
        Recebe um dicionário contendo os dados e insere-os no objeto Consulta
        junto com o seu modo, para ser enviado ao módulo MBD a fim de editar
        um usuário.
        """

        consulta.setValorConsulta(lista)
        consulta.setModoConsulta('cl')
        ok = editaBD(consulta)

    @returnType()
    @parameterTypes(selfType, string)
    def realizaRemocao(usuario):
        """
        Recebe um dicionário contendo os dados e insere-os no objeto Consulta
        junto com o seu modo, para ser enviado ao módulo MBD a fim de remover
        um usuário.
        """

        consulta.setValorConsulta(lista)
        consulta.setModoConsulta('cl')
        ok = removeBD(consulta)

    @returnType()
    @parameterTypes(selfType, dict)        
    def realizaConsulta():
        """
        Recebe um dicionário contendo os dados e insere-os no objeto Consulta
        junto com o seu modo, para ser enviado ao módulo MBD a fim de obter
        uma consulta de usuários.
        """
        
        consulta.setValorConsulta(lista)
        consulta.setModoConsulta('cl')
        ok = consultaBD(consulta)
