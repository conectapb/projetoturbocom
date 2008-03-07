# -*- coding: iso-8859-1 -*-

__version__="0.1"

"""
Autor: Henrique Eiji Mikado
Data: 06/03/2008
"""

class Consulta(object):
    """Esta classe implementa o objeto Consulta possuindo apenas sets e gets"""
    
    def __init__(self, modoConsulta = none, dictConsulta = none):
        """Inicializa os atributos da classe. """

        self.__modoConsulta = modoConsulta
        self.__dictConsulta = dictConsulta
        
    @returnType(string)
    @parameterTypes(selfType)
    def getModoConsulta():
        return self.__modoConsulta

    @returnType()
    @parameterTypes(selfType, dict)
    def setModoConsulta(modoConsulta):
        self.__modoConsulta = modoConsulta

    @returnType(string)
    @parameterTypes(selfType)    
    def getDictConsulta():
        p = self.__dictConsulta

    @returnType()
    @parameterTypes(selfType, dict)
    def setDictConsulta(campoConsulta):
        self.__dictConsulta = dictConsulta


