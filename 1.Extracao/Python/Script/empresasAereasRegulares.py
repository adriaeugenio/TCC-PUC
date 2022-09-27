from asyncio.windows_events import NULL
from contextlib import nullcontext
import os
from selenium import webdriver
import time
import parametros as p
import csv
import codecs
import verificaPastaExiste as ve
import transformaCSVExcel as csvexcel

pasta = p.pastaDados + '/Empresas Aéreas Regulares/'
nomeArquivo = 'Não Existe' 

#Verifica se a Pasta Existe (Caso Não Exista, Ela é criada)
v = ve.verificaPasta(p.pastaDados + '/Empresas Aéreas Regulares')

#Verifica os Todos os Arquivos que Existem na Pasta
for diretorio, subpastas, arquivos in os.walk(pasta):
    
    for arquivo in arquivos:

        if len(os.path.join(arquivo)) >= 1:

            nomeArquivo = os.path.join(arquivo) 

#Remove os arquivos da pasta
if os.path.exists(pasta + nomeArquivo):

    os.remove(pasta + nomeArquivo)

os.chdir(p.caminhoPasta + '/Driver') 

#Download dos arquivos
op = webdriver.ChromeOptions()
p = {'download.default_directory':p.caminhoPastaAlternativo + 'Dados\\Empresas Aéreas Regulares'}

op.add_experimental_option('prefs', p)

#Adiciona as Opções do Navegador
op.add_experimental_option('prefs', p)

#Seta o caminho chromedriver.exe
navegador = webdriver.Chrome(options=op)

#Maximiza o Navegador
navegador.maximize_window()

navegador.get('https://sistemas.anac.gov.br/sas/empresasaereas/view/frmEmpresas.aspx')

navegador.find_element_by_xpath('//*[@id="MainContent_rdList_0"]').click()

navegador.find_element_by_xpath('//*[@id="MainContent_cboVocativo"]/option[9]').click()

navegador.find_element_by_xpath('//*[@id="MainContent_btnPesquisar"]').click()
    
download = navegador.find_element_by_xpath('//*[@id="MainContent_btnCSV"]')
    
download.click()

time.sleep(5)

navegador.close()

#Verifica os Todos os Arquivos que Existem na Pasta
for diretorio, subpastas, arquivos in os.walk(pasta):
    
    for arquivo in arquivos:

        if len(os.path.join(arquivo)) >= 1:

            nomeArquivo = os.path.join(arquivo) 

#Trata a Fonte de Dados
os.chdir(pasta)

linhas = csv.reader(codecs.open(nomeArquivo, 'rU', 'utf-16'), delimiter=';')

linhascsv = list(linhas)

file = open(nomeArquivo, 'w+', newline ='', encoding='utf-8') 

with file: 

    write = csv.writer(file, delimiter=';') 
    write.writerows(linhascsv) 

#Carrega Novamente para Tratar os Acentos
with open(nomeArquivo, 'r', encoding='utf-8') as f:
                        
    linhas = csv.reader(f, delimiter=';')
                        
    linhascsv = list(linhas)

file = open(nomeArquivo, 'w+', newline ='') 

with file: 

    write = csv.writer(file, delimiter=';') 
    write.writerows(linhascsv) 

os.rename(nomeArquivo, 'EmpresasAereasRegulares.csv')

#Transforma o Arquivo CSV em Excel
ce = csvexcel.transformaCSVExcel('EmpresasAereasRegulares') 