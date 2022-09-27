import requests
import csv
import os
import pandas as pd
import parametros as p
import verificaPastaExiste as ve
import transformaCSVExcel as csvexcel

#Verifica se a Pasta Existe (Caso Não Exista, Ela é criada)
v = ve.verificaPasta(p.pastaDados + '/Aeronáves')

#Define a Url de Origem do Arquivo
remote_url = p.urlOrigem + "dadosabertos/Aeronaves/RAB/dados_aeronaves.csv"

#Define a Url o Local de Salvamento do Arquivo
local_file = p.pastaDados + '/Aeronáves/' + 'Aeronaves.csv'

#Requisição HTTP
data = requests.get(remote_url)

print(remote_url)

#Salva o Arquivo
with open(local_file, 'wb') as file:

    file.write(data.content)

#Define o Caminho de Pasta
os.chdir(p.pastaDados + '/Aeronáves')  

#Abre o Arquivo para Leitura
#Remove a Linha (Observação da Data de Atualização)
df = pd.read_csv('Aeronaves.csv',sep=';',encoding='utf-8-sig', on_bad_lines='skip', skiprows=[0])

#Salva o Arquivo Novamente
df.to_excel('Aeronaves.xlsx',engine='xlsxwriter', index = None, header=True)

#Exclui o Arquivo CSV da pasta para Manter somente o Novo Arquivo
os.remove('Aeronaves.csv')