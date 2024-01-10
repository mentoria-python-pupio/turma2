import os
import requests
import zipfile
import argparse


# DESAFIO:


#1 - Fazer download de todos os zips que contenham bounty e exista uma plataforma
#2 - Salvar o zip numa pasta da plataforma: Ex: yeswehack > arquivo1.zip ... arquivox.zip
#3 - Extrair os arquivos zip e consolidar todos os txts em um unico com todas as URLS
#4 - Remover as urls duplicadas e ordenar por ordem alfabetica


def get_json_data_from_chaos(only_bount: bool = True):

    response = requests.get("https://chaos-data.projectdiscovery.io/index.json")

    # Verifica se a requisicao foi bem sucedida
    if response.status_code != 200:
        print("PROBLEMA AO OBTER DADOS DO CHAOS!!")

    # obtem os dados da requisicao
    dados = response.json()
    
    # Se só nos interessar os casos com bounty
    if only_bount:
        dados = list(filter(lambda x: x["bounty"] == True, dados))
    
    return dados

def download_file(dados: list, plataforma: str):
    # Verificamos se existe a pastinha da plataforma a ser baixada
    if not os.path.exists("zip/" + plataforma):
        os.mkdir("zip/" + plataforma)

    # Filtramos os dados da plataforma desejada
    dados_plataforma = filter(lambda x: x["platform"]== plataforma, dados)

    # Pra cada item dentro dos dados da plataforma filtrada
    for item in dados_plataforma:
        # Fazemos o download do arquivo
        response = requests.get(item["URL"])
        # Obtemos o nome do arquivo baixado (pois ja esta na URL)
        output_file = item["URL"].split("/")[-1]
        # Salva o conteudo do download em um arquivo no nosso HD
        with open(f"zip/{plataforma}/{output_file}", "wb") as file:
            file.write(response.content)

    print(f"Terminei de baixar os itens da {plataforma}")

def unzip_and_read_text_files(plataforma: str):
    for arquivo in os.listdir(f"zip/{plataforma}"):
        # Um controle para garantir que apenas vamos extrair arquivos que são ZIP
        if not arquivo.endswith(".zip"):
            continue
        with zipfile.ZipFile(f"zip/{plataforma}/{arquivo}", "r") as zip_ref:
            # Extrai todos os arquivos do zip
            zip_ref.extractall()
            # Depois de extrair, conseguimos listar o nome dos arquivos extraidos
            extracted_files = zip_ref.namelist()
            # Movemos eles para a pasta da plataforma
            for extracted_file in extracted_files:
                os.rename(extracted_file, f"zip/{plataforma}/{extracted_file}")
        # Deletamos o arquivo zip baixado!
        os.remove(f"zip/{plataforma}/{arquivo}")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Parsers dos argumentos passados no script"
    )

    parser.add_argument(
        "--plataforma", "-p", type=str, required=True, help="Plataformas separadas por virgula. Ex: hackerone,bugcrowd,yeswehack"
    )
    
    # Força o uso dos argumentos definidos acima
    args = parser.parse_args()
    
    plataformas = args.plataforma.split(",")

    # PASSO 1: OBTER OS DADOS DA TABELA DO CHAOS!
    dados = get_json_data_from_chaos()
    print("Terminei de baixar todas as URLs dos ZIPs")

    if not os.path.exists("zip"):
        os.mkdir("zip")
    
    for plataforma in plataformas:
        print(f"INICIANDO DOWNLOAD DOS DADOS DA {plataforma}")
        # Faz o Download dos itens da plataforma
        download_file(dados, plataforma=plataforma)
        # Extrai o conteudo dos arquivos zip da plataforma
        unzip_and_read_text_files(plataforma=plataforma)