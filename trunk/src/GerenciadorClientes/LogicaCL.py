# -*- coding: iso-8859-1 -*-

__version__="0.1"

#from ..MBD import Consulta,ManipuladorBD
#from ..OS import EmitirOS

"""
Autor: Henrique Eiji Mikado
Data: 06/03/2008
"""

class LogicaCL:
    """
    Esta classe será responsável por toda a lógica do Gerenciador de Clientes.
    """

    #Atributo da classe
    self.consulta = Consulta()

    @returnType()
    @parameterTypes(selfType, dict)
    def realizaAdicao(lista):
        """
        Recebe um dicionário contendo os dados e insere-os no objeto Consulta
        junto com o seu modo, para ser enviado ao módulo MBD a fim de
        cadastrar um cliente.
        """
        
        consulta.setDictConsulta(lista)
        consulta.setModoConsulta('cl')
        ok = gravaBD(consulta)

    @returnType()
    @parameterTypes(selfType, dict)        
    def realizaEdicao(lista):
        """
        Recebe um dicionário contendo os dados e insere-os no objeto Consulta
        junto com o seu modo, para ser enviado ao módulo MBD a fim de editar
        um cliente.
        """

        consulta.setDictConsulta(lista)
        consulta.setModoConsulta('cl')
        ok = alteraBD(consulta)

    @returnType()
    @parameterTypes(selfType, dict)        
    def realizaConsulta(lista):
        """
        Recebe um dicionário contendo os dados e insere-os no objeto Consulta
        junto com o seu modo, para ser enviado ao módulo MBD a fim de obter
        uma consulta de clientes.
        """
    
        consulta.setDictConsulta(lista)
        consulta.setModoConsulta('cl')
        ok = consultaBD(consulta)

    @returnType()
    @parameterTypes(selfType, dict)
    def realizaRemocao(lista):
        """
        Recebe um dicionário contendo os dados e insere-os no objeto Consulta
        junto com o seu modo, para ser enviado ao módulo MBD a fim de remover
        um cliente.
        """
            
        consulta.setDictConsulta(lista)
        consulta.setModoConsulta('cl')
        ok = deletaBD(consulta)

    @returnType()
    @parameterTypes(selfType, dict)        
    #def realizaImpressao(lista):
        """
        Insere os dados do dicionário recebido em um arquivo pdf, gerando uma
        tabela de clientes. Além disso, esse arquivo será executado, podendo
        assim, ser imprimido.
        """ 

    @returnType()
    @parameterTypes(selfType, dict)
    def emiteOS(lista):
        """
        Redireciona o dicionário recebido para o módulo de OS para preencher
        o formulário.
        """       

        osCliente(lista)

    @returnType()
    @parameterTypes(selfType, dict)
    def adicionaSelecionaveis(lista):
        """
        Recebe um dicionário contendo os dados e insere-os no objeto Consulta
        junto com o seu modo, para ser enviado ao módulo MBD a fim de adicionar
        uma opção em um campo selecionável da tabela de clientes.
        """

        consulta.setDictConsulta(lista)
        consulta.setModoConsulta('cl')
        ok = adicionaCampo(consulta)

    @returnType()
    @parameterTypes(selfType, dict)
    def consultaSelecionaveis(lista):
        """
        Recebe um dicionário contendo os dados e insere-os no objeto Consulta
        junto com o seu modo, para ser enviado ao módulo MBD a fim de consultar
        as opções de um campo selecionável da tabela de clientes.
        """

        consulta.setDictConsulta(lista)
        consulta.setModoConsulta('cl')
        ok = consultaCampo(consulta)

    @returnType()
    @parameterTypes(selfType, dict)    
    def editaSelecionaveis(lista):
        """
        Recebe um dicionário contendo os dados e insere-os no objeto Consulta
        junto com o seu modo, para ser enviado ao módulo MBD a fim de editar
        as opções de um campo selecionável da tabela de clientes.
        """

        consulta.setDictConsulta(lista)
        consulta.setModoConsulta('cl')
        ok = editaCampo(consulta) 

    @returnType()
    @parameterTypes(selfType, dict)    
    def removeSelecionaveis(lista):
        """
        Recebe um dicionário contendo os dados e insere-os no objeto Consulta
        junto com o seu modo, para ser enviado ao módulo MBD a fim de remover
        uma opção em um campo selecionável da tabela de clientes.
        """

        consulta.setDictConsulta(lista)
        consulta.setModoConsulta('cl')
        ok = removeCampo(consulta)        
    
