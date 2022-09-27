import requests
import os
import parametros as p
import verificaPastaExiste as ve
import transformaCSVExcel as csvexcel
import pandas as pd 

#Verifica se a Pasta Existe (Caso Não Exista, Ela é criada)
v = ve.verificaPasta(p.pastaDados + '/Aerodromos Internacionais')

#Define a Url de Origem do Arquivo
remote_url = p.ourAirports + "airports.csv"

#Define a Url o Local de Salvamento do Arquivo
local_file = p.pastaDados + '/Aerodromos Internacionais/' + 'AerodromosInternacionais.csv'

#Requisição HTTP
data = requests.get(remote_url)

print(remote_url)

#Salva o Arquivo
with open(local_file, 'wb') as file:

    file.write(data.content) 

#Define o Caminho de Pasta
os.chdir(p.pastaDados + '/Aerodromos Internacionais')  

#Abre o Arquivo para Leitura
read_file = pd.read_csv('AerodromosInternacionais.csv', sep=',',encoding='utf-8-sig',index_col=False)

#Salva o Arquivo Novamente
read_file.to_csv('AerodromosInternacionais.csv', sep=';',index=None, header=True,  encoding='utf-8-sig')