import os
import requests
import zipfile
import argparse
import threading

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


def slice_list(input_list, num_slices):
    """
    Criado pelo chat GPT com o seguinte prompt:
    'I need your help to create a function that gives me a N slices of a list'
    """
    if num_slices <= 0:
        raise ValueError("Number of slices must be greater than 0.")
    # Calculate the approximate size of each slice
    slice_size = len(input_list) // num_slices
    # Calculate the remainder for the last slice
    remainder = len(input_list) % num_slices
    slices = []
    start_index = 0
    for i in range(num_slices):
        # Calculate the end index for the current slice
        end_index = start_index + slice_size + (1 if i < remainder else 0)
        # Append the slice to the result list
        slices.append(input_list[start_index:end_index])
        # Update the start index for the next slice
        start_index = end_index
    return slices


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Parsers dos argumentos passados no script"
    )

    parser.add_argument(
        "--plataforma", "-p", type=str, required=True, help="Plataformas separadas por virgula. Ex: hackerone,bugcrowd,yeswehack"
    )
    parser.add_argument(
        "--threads", "-t", type=int, default=60, help="Numero de threads que serao utilizadas para fazer o download do zip"
    )
    
    # Força o uso dos argumentos definidos acima
    args = parser.parse_args()
    
    plataformas = args.plataforma.split(",")
    threads = args.threads

    # PASSO 1: OBTER OS DADOS DA TABELA DO CHAOS!
    dados = get_json_data_from_chaos()
    print("Terminei de baixar todas as URLs dos ZIPs")

    if not os.path.exists("zip"):
        os.mkdir("zip")
    
    lista_threads = []

    for plataforma in plataformas:
        print(f"INICIANDO DOWNLOAD DOS DADOS DA {plataforma}")
        # Faz o Download dos itens da plataforma
        # Filtramos os dados da plataforma desejada
        dados_plataforma = list(filter(lambda x: x["platform"]== plataforma, dados))
        
        # Dividimos os dados igualmente entre as threads
        for slice_data in slice_list(dados_plataforma, threads):
            # Definimos que a thread vai fazer o download em cima de uma fatia dos dados
            thread = threading.Thread(
                target=download_file, args=(slice_data, plataforma)
            )
            # Guardamos a thread para acompanhamento do seu status
            lista_threads.append(thread)
            # Iniciamos a execucao da thread
            thread.start()
        
        # Aguarda o status de encerramento das threads abertas
        for thread in lista_threads:
            thread.join()
        
        print(f"Terminei de baixar os itens da {plataforma}")

        # Extrai o conteudo dos arquivos zip da plataforma
        unzip_and_read_text_files(plataforma=plataforma)
