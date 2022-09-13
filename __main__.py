"""
PROGRAMA: Projeto Final Python
REQUISITOS:
Faca uma aplicac˜ao que efetue as operac˜oes a seguir:
1. O Portal de Dados Abertos do TCE-RS contem o Balancete de Despesa
Consolidados 2022 no link (http://dados.tce.rs.gov.br/dados/municipal/balancete-despesa/2022.csv).
2. Use o pacote Requests para armazenar em memoria baixar o arquivo do
balancete na variavel denominada ”dados”.
3. Grave em disco o conteudo da variavel ”dados” em um arquivo denominado
”balancete.csv”
4. Use o pacote Pandas, para ler o arquivo ”balancete.csv” para a variavel
”balancete”.
5. Usando o pacote Pandas, grave em disco o conteudo da variavel ”balancete”
em um arquivo denominado ”balancete.xlsx”, e
6. Usando o pacote OpenPyXL, leia o conteudo do arquivo ”balancete.xlsx”
para a variavel ”novo balancete”, e
7. Finalizando a aplicac˜ao, usando o OpenPyXL, grave o conteudo da variavel
”novo balancete” no arquivo ”novo balancete.xlsx”
Coloque seu codigo no Moodle em um arquivo compactado de extens˜ao.zip.

AUTOR:  Ítalo de Castro Rodrigues
DATA:   12/09/2022
VERSÃO: 1.0.0
"""

#1. dados do link do TCE

#{'Server': 'nginx/1.4.6 (Ubuntu)', 'Date': 'Mon, 12 Sep 2022 19:45:13 GMT',
#'Content-Type': 'application/octet-stream', 'Content-Length': '169609687',
#'Last-Modified': 'Sat, 10 Sep 2022 16:20:08 GMT', 'Connection': 'keep-alive',
#'ETag': '"631cb938-a1c09d7"', 'Accept-Ranges': 'bytes'}

#Módulos

    #pip install requests
    #pip install pandas
    #pip install openpyxl


def main():

    import requests
    import pandas as pd
    import openpyxl

    #variáveis e trabalhos para os passos 2 e 3 (requests + write bytes em variável, gerando arquivo csv)
    print ("trabalhando os passos 2 e 3 do projeto.... requests gerando variável dados e arquivo balancete.csv")

    html = 'http://dados.tce.rs.gov.br/dados/municipal/balancete-despesa/2022.csv'
    resp = requests.get(html)
    dados = resp.iter_content()

    csvs = open ('balancete.csv', 'wb')
    for escrevendo in dados:
        csvs.write(escrevendo)
        
    csvs.close()


    #variáveis e trabalhos para os passos 4 e 5
    #OBSERVAÇÃO DO PASSO 5: O TAMANHO DO ARQUIVO DEMANDA TEMPO PARA GERAR XLSX.
    print ("trabalhando os passos 4 e 5 do projeto....com pandas, lendo arquivo balancete.csv, e com a variável balancete gerando arquivo balancete.xlsx")

    balancete = pd.DataFrame(pd.read_csv('balancete.csv'))
    print (balancete)
    balancete.to_excel('balancete.xlsx')


    #variáveis e trabalhos para os passos 6 e 7
    print ("trabalhando os passos 6 e 7 do projeto....usando openpyxl para ler balancete.xlsx e gravar novo balancete.xlsx com variável novo balancete")

    novo_balancete = openpyxl.load_workbook('balancete.xlsx')
    novo_balancete.save('novo balancete.xlsx')


if __name__ == "__main__":
    main()






