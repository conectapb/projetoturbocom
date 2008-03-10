# -*- coding: iso-8859-1 -*-
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.colors import black, grey, pink
larguraMax = [0, 18*cm]
    
"""
Autor: Henrique Eiji Mikado
Data: 06/03/2008
"""    
 
__version__="0.1"

def oscliente(c):


    #Escreve o texto fora da tabela
    c.setFont("Helvetica-Bold",14)
    c.drawCentredString(10*cm, 28*cm, unicode("ORDEM DE SERVIÇO - CLIENTE     -     Nº. _______", "iso-8859-1"))
    c.translate(1.5*cm, 2*cm)
    c.setFont("Helvetica-Bold",10)
    c.drawString(0,25*cm, unicode("Natureza do serviço:___________", "iso-8859-1"))
    c.drawString(10*cm,25*cm, unicode("Tipo:___________", "iso-8859-1"))
    c.setFont("Helvetica",11)
    c.drawString(0, 18.5*cm, unicode("Agendamento com o cliente - Data:          Horário:", "iso-8859-1"))
    c.setFont("Helvetica-Bold",11)
    c.drawString(0, 15.2*cm, unicode("REQUISIÇÃO DE EQUIPAMENTOS", "iso-8859-1"))
    c.drawString(4.5*cm, 14.7*cm, unicode("Qtd", "iso-8859-1"))
    c.drawString(10.8*cm, 14.7*cm, unicode("Qtd", "iso-8859-1"))
    c.drawString(17.2*cm, 14.7*cm, unicode("Qtd", "iso-8859-1"))
    c.setFont("Helvetica-Bold",12)
    c.drawString(0, 6*cm, unicode("INFORMAÇÕES DE CONTROLE (Registro obriatório na via de controle):", "iso-8859-1"))   

    #Conteúdo das tabelas
    campos1 = [
        'Nome do Cliente:',
        'CPF:',
        'E-Mail:',
        'Endereço:',
        'Bairro:',
        'Ponto de Referência:',
        'Fone:',
        'Pessoa a Procurar:',
        'Banda:',
        'Condições de Pagto:',
        'Como ficou sabendo do nosso serviço?:',
    ]
    campos2 = [
        'Identidade/Emitente:',
        'Cidade:',
        'Celular:',
        'SIST OPERACIONAL:',
        'Fone:',
        'Login:',
        'Senha:',
        'Se Indicador, nome:',
    ]
    campos3 = [[
        'Abraçadeiras',
        'Antena 2.4',
        'Antena Zirok',
        'Bucha para parafuso',
        'Cabo Elétrico',
        'Cabo RGC 213',
        'Caixa Hermética Pq',
        'Caixa Hermética Gr',
        'Caixa Herm plástica',
        'Caixas de cabo UTP',
        'Canaleta',
        'Capa para RJ',
        'Conector N Macho',
        'Conectores N Femea',
        'Conector RJ 45'
        ],[
        'Dipolo de Antena 5.8',
        'Divisor de potencia',
        'Emenda para RJ 45',
        'Estabilizadores',
        'Ethernet Switch 8 pt',
        'Ethernet Switch 16 pt',
        'Extensão',
        'Fita de fusão',
        'Fita isolante',
        'Mastro 3 m',
        'Parafuso',
        'Pigtail',
        'Placa de rede Comum',
        'Placa de rede wireless',
        'Suporte achatado'
        ],[
        'Suporte com afastador',
        'Suporte metalon Tripé',
        'Suporte p/antena 109 B',
        'Suporte p/antena 209 B',
        'Tomadas Pino Femea',
        'Tomadas Pino Macho',
        'Transformador (100 W)',
        'Transformador (50 W)',
        'Transmissor AP 2.4 GHz',
        'Transmissor SM 5.8 GHz',
        'Transmissor Mikrotik',
        'T\'s',
        'Tubo de Cola Quente'
        ]
    ]


    #desenha as tabelas
    c.setLineWidth(0.5)
    c.grid(larguraMax, coords(12, 19))
    c.grid(larguraMax, coords(5, 16))

    c.grid(coordscampo3()[0], coords(16, 7))
    c.grid(coordscampo3()[1], coords(16, 7))
    c.grid(coordscampo3()[2], coords(16, 7))
    c.translate(0.2*cm, 0.15*cm)    
    c.setFont('Helvetica',10)
    
    #Preenche as tabelas
    #tabela 1
    for i in range(11):
        c.drawString(0, coords(12, 19)[i], unicode(campos1.pop(), 'iso-8859-1'))

    #tabela 2
    c.setFont('Helvetica-Bold',10)
    c.drawString(0, 17.5*cm, unicode('OBS.:', 'iso-8859-1')) 
    
    #tabela 3
    c.setFont('Helvetica',10)
    for i in range(15):
        c.drawString(0, coords(16, 7)[i], unicode(campos3[0].pop(), 'iso-8859-1'))
    for i in range(15):
        c.drawString(5.5*cm, coords(16, 7)[i], unicode(campos3[1].pop(), 'iso-8859-1'))
    for i in range(13):
        c.drawString(12*cm, coords(16, 8)[i], unicode(campos3[2].pop(), 'iso-8859-1'))

def coordscampo3():
    #coordenadas das colunas da terceira tabela
    return [[4.3*cm, 5.3*cm],[10.6*cm, 11.6*cm],[17*cm, larguraMax[1]]]
    

def coords(qtdLinhas, altura):
    #coordenadas das linhas ou textos em uma lista.
    
    x = altura
    coords = []
  
    for i in range(qtdLinhas):
        coords.append(x*cm)
        #distância vertical
        x += 0.5 
    
    return coords
    
def tabela():
    pass

c = canvas.Canvas("osCliente.pdf")
oscliente(c)
c.showPage()
c.save()


