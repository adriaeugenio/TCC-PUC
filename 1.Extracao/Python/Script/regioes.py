import requests
import os
import parametros as p
import verificaPastaExiste as ve
import transformaCSVExcel as csvexcel
import pandas as pd 

#Verifica se a Pasta Existe (Caso Não Exista, Ela é criada)
v = ve.verificaPasta(p.pastaDados + '/Regiões')

#Define a Url de Origem do Arquivo
remote_url = p.ourAirports + "regions.csv"

#Define a Url o Local de Salvamento do Arquivo
local_file = p.pastaDados + '/Regiões/' + 'Regioes.csv'

#Requisição HTTP
data = requests.get(remote_url)

print(remote_url)

#Salva o Arquivo
with open(local_file, 'wb') as file:

    file.write(data.content) 

#Define o Caminho de Pasta
os.chdir(p.pastaDados + '/Regiões')  

#Abre o Arquivo para Leitura
read_file = pd.read_csv('Regioes.csv', sep=',',encoding='utf-8-sig',index_col=False)

#Salva o Arquivo Novamente
read_file.to_excel('Regioes.xlsx', index = None, header=True)

#Exclui o Arquivo CSV da pasta para Manter somente o Novo Arquivo
os.remove('Regioes.csv')