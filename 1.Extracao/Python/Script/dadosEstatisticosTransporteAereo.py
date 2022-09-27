import requests
import csv
import os
import parametros as p
import verificaPastaExiste as ve
import transformaCSVExcel as csvexcel
import pandas as pd
import apagaArquivoPasta as apagaarquivos

#Declara o caminho da Pasta
caminhoPasta = p.pastaDados + '/Dados Estatísticos do Transporte Aéreo/'

#Verifica se a Pasta Existe (Caso Não Exista, Ela é criada)
v = ve.verificaPasta(caminhoPasta)

#Verifica se o Arquivo Existe na Pasta
if os.path.exists(caminhoPasta + 'DadosEstatisticosTransporteAereo.csv'):

    os.remove(caminhoPasta + 'DadosEstatisticosTransporteAereo.csv')

#Define a Url de Origem do Arquivo
remote_url = p.urlOrigem + "dadosabertos/Voos%20e%20operações%20aéreas/Dados%20Estatísticos%20do%20Transporte%20Aéreo/Dados_Estatisticos.csv"

#Define a Url o Local de Salvamento do Arquivo
local_file = caminhoPasta + 'DadosEstatisticos.csv'

#Requisição HTTP
data = requests.get(remote_url)

print(remote_url)

#Salva o Arquivo
with open(local_file, 'wb') as file:

    file.write(data.content)

#Define o Caminho de Pasta
os.chdir(caminhoPasta)  

#Abre o Arquivo para Leitura
with open('DadosEstatisticos.csv', 'r', encoding='utf-8-sig') as f:
   
   linhas = csv.reader(f, delimiter=';')
   
   linhascsv = list(linhas)

#Remove a Linha (Observação da Data de Atualização)
   linhascsv.remove(linhascsv[0])

file = open('DadosEstatisticos.csv', 'w+', newline ='') 

#Salva o Arquivo Novamente
with file: 

    write = csv.writer(file, delimiter=';') 
    write.writerows(linhascsv)

#Adiciona o 'ID' da Tabela    
    
#Abre o ficheiro
csv = open('DadosEstatisticos.csv', 'r', encoding='latin-1')

tabela = csv

contador = 0

# Abre ficheiro de saida...
saida = open('DadosEstatisticosTransporteAereo.csv', "a",encoding='utf-8-sig')

#Para cada uma das demais linhas no ficheiro...
for linha in csv:

    contador += 1

    if contador == 1: 

        linha = linha.rstrip() + ';' + 'ID' + '\n'

    else:
        
        linha = linha.rstrip() + ';' + str((contador - 1)) + '\n'  

    saida.write(linha) 

#Fecha ficheiro CSV de entrada
csv.close()

os.remove('DadosEstatisticos.csv')