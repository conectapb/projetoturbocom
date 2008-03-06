# -*- coding: UTF-8 -*-

class ManipuladorBD:
    """
    Esta é a Classe central deste módulo, que será responsável por
    controlar todas as funções do Manipulador do Banco de Dados.
    """
    
    bdMP = ""         # Instância da classe BDMP
    bdCliente = ""    # Instância da classe BDCliente
    bdChamada = ""    # Instância da classe BDChamada
    bdOS = ""         # Instância da classe BDOS
    bdUsuario = ""    # Instância da classe BDUsuario

    @returnType(string)
    @parameterTypes(selfType, Consulta)
    def consultaBD(self, __consulta):
        """ Método que realizará a função Consultar. """
        
        resultadoConsulta = ""
        
        return resultadoConsulta
    
    @returnType(boolean)
    @parameterTypes(selfType, Consulta)
    def adicionaBD(self, __consulta):
        """ Método que realizará a função Adicionar. """
        
        resultadoConsulta = False
        
        return resultadoConsulta
    
    @returnType(boolean)
    @parameterTypes(selfType, Consulta)
    def editaBD(self, __consulta):
        """ Método que realizará a função Editar. """
        
        resultadoConsulta = False
        
        return resultadoConsulta
    
    @returnType(boolean)
    @parameterTypes(selfType, Consulta)
    def removeBD(self, __consulta):
        """ Método que realizará a função Remover. """
        
        resultadoConsulta = False
        
        return resultadoConsulta
    