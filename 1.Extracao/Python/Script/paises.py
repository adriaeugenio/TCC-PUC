import requests
import os
import parametros as p
import verificaPastaExiste as ve
import transformaCSVExcel as csvexcel
import pandas as pd 

#Verifica se a Pasta Existe (Caso Não Exista, Ela é criada)
v = ve.verificaPasta(p.pastaDados + '/Paises')

#Define a Url de Origem do Arquivo
remote_url = p.ourAirports + "countries.csv"

#Define a Url o Local de Salvamento do Arquivo
local_file = p.pastaDados + '/Paises/' + 'Paises.csv'

#Requisição HTTP
data = requests.get(remote_url)

print(remote_url)

#Salva o Arquivo
with open(local_file, 'wb') as file:

    file.write(data.content) 

#Define o Caminho de Pasta
os.chdir(p.pastaDados + '/Paises')  

#Abre o Arquivo para Leitura
read_file = pd.read_csv('Paises.csv', sep=',',encoding='utf-8-sig',index_col=False)

#Salva o Arquivo Novamente
read_file.to_excel('Paises.xlsx', index = None, header=True)

#Exclui o Arquivo CSV da pasta para Manter somente o Novo Arquivo
os.remove('Paises.csv')