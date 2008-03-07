# -*- coding: iso-8859-1 -*-

__version__="0.2"

"""
Autor: Taciano Messias Moraes
Data: 05/03/2008
"""

class ManipuladorBD:
    """
    Esta é a Classe central deste módulo, que será responsável por
    controlar todas as funções do Manipulador do Banco de Dados.
    """
    

    @returnType(string)
    @parameterTypes(selfType, Consulta)
    def consultaBD(self, __consulta):
        """ Método que realizará a função Consultar. """
        
        switch = {
            'cl': consultaCL,
            'ch': consultaCH,
            'os': consultaOS,
            'us': consultaUS,
            'mp': consultaMP}[consulta.getModoConsulta()](consulta)
        return switch
    
    @returnType(boolean)
    @parameterTypes(selfType, Consulta)
    def adicionaBD(self, __consulta):
        """ Método que realizará a função Adicionar. """
        
        switch = {
            'cl': adicionaCL,
            'ch': adicionaCH,
            'os': adicionaOS,
            'us': adicionaUS}[consulta.getModoConsulta()](consulta)
        return switch
    
    @returnType(boolean)
    @parameterTypes(selfType, Consulta)
    def editaBD(self, __consulta):
        """ Método que realizará a função Editar. """
        
        switch = {
            'cl': editaCL,
            'ch': editaCH,
            'us': editaUS}[consulta.getModoConsulta()](consulta)
        return switch
    
    @returnType(boolean)
    @parameterTypes(selfType, Consulta)
    def removeBD(self, __consulta):
        """ Método que realizará a função Remover. """
        
        switch = {
            'cl': removeCL,
            'ch': removeCH,
            'os': removeOS,
            'us': removeUS}[consulta.getModoConsulta()](consulta)
        return switch

    
