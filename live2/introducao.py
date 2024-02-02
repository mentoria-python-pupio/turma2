total_dominios = 15
total_subdominios = 10

total_scan_dominios = total_dominios*total_subdominios

idade = 30
pi = 3.141592653

idade = "roberto"
print(idade)

if idade > 60:
    print("eh velho")
else:
    print("eh novo")

booleanas = True or False

list_frutas = ["banana", "maça", "pera"]*3000000

list_frutas.append("abacaxi")

tuplas = ("banana", "maça", "pera", 10, {})


dict_pessoa = {
    "nome": "Victor",
    "idade": 24,
    "eh_estudante": False,
    "historico_endereco": None,
}

DICT_MAPEAMENTO_CORES = {
    "AMARELO": "#004477",

}

lista_pessoas = [dict_pessoa, ]
if DICT_MAPEAMENTO_CORES["AMARELO"]:


# Tipos especiais
None

{1,2,3,4,5,6,7,8} | {10,15,8,8,8,8,8,8,} 
{1,2,3,4,5,6,7,8} & {10,15,8,8,8,8,8,8,}

sorted(set([]))
# Geradores

a = (i for i in range(100))

for i in a:
    print(i)

quantidade_de_itens = (46 + 10 + 12) ** 8

memoria_utilizada_pela_lista= (8 * quantidade_de_itens // (1024 ** 5)) + (28* quantidade_de_itens // (1024 ** 5))
quantidade_de_itens_para_3GB_memoria = 3 * (1024 ** 3) // (28 + 8)

lista_de_3GB = [i for i in range(quantidade_de_itens_para_3GB_memoria)]

blablabla = (i for i in range(quantidade_de_itens_para_3GB_memoria))


def matemagica(x):
    x = x -15
    return x*2

def cria_lista_tamanho(x):
    ...
    return [i for i in range(x)]

def cria_lista_tamanho(x):
    lista = []
    for i in range(x):
        lista.append(i)
    return lista

def cria_ger_tamanho(x):
    return (i for i in range(x))

def cria_ger_tamanho(x):
    for i in range(x):
        i = i**2
        yield i

i = 0
while i < 100:
    ...
    i +=1



cria_lista_tamanho(1)
cria_lista_tamanho(2)
cria_ger_tamanho(5)
cria_lista_tamanho(1)
cria_lista_tamanho(1)
cria_lista_tamanho(1)
cria_lista_tamanho(1)
cria_lista_tamanho(1)


#### LIVE 2

if ...: # Espressao depois do IF sempre resulta num boleano
    pass

prazo_restante = 5556

if prazo_restante == 9999:
    print("SEM DATA")
elif prazo_restante == 5555:
    print("EXEMPLO SEM LOGICA")
elif prazo_restante >= 0:
    print("EM ANDAMENTO")
else:    
    print("ATRASADO")

import time
for contador, numero in enumerate(range(10), start=1):
    print(f"itens: {contador} de 100", "TESTE", "TESTE")
    time.sleep(0.1)

for item in list:
    ...

lista = [("Nome", "CPF", "endereco", "teste"), ("Nome1", "CPF1", "endereco1", "teste1"), ("Nome2", "CPF2", "endereco2", "teste2"), ("Nome2", "CPF2", "endereco2", "teste2", "teste3", "teste4")]

for nome, cpf, endereco, teste in lista:
    print(nome, cpf, endereco, teste, sep=" - ")


lista = list(range(10))

lista[-2]

class MinhaExcessao(Exception):
    pass


#### Exceptions
y = 100
x = 0

import traceback


try:
    infinito = y/x
except ZeroDivisionError:
    print("DEU RUIM.. MAS TRATEI")
    infinito = 0
except ValueError:
    infinito = 10        
except TypeError:
    infinito = 100
else:
    print("NAO DEU ERRO NENHUM")
finally:
    print("RODEI E FODA-SE")
    try:
        100/0
    except:
        print(f"Registrando no log o erro: {traceback.format_exc()}")
        print("Deu Ruim, mas tratei...")


def func_dobra_tudo(*x):
    return [y * 2 for y in x]

def func_dobra_tudo(x):
    return x * 2

def func_url(dominio, path, http, **kwargs):
    print("KWARGS:", kwargs)
    verify = kwargs.get("verify", True)
    return f"{http}://{dominio}/{path}"

func_url(dominio="teste.com", path="xtudo",  http="https", verify=False, url_teste=True, numero_ataques=30)
func_url("teste.com","xtudo", "https")


## Uso de requests
import requests

response = requests.get("https://chaos-data.projectdiscovery.io/index.json")

dados = response.json()

for item in dados:
    if item["bounty"] and item["platform"]:
        print(item["platform"], item["URL"], sep=": ")

# DESAFIO:
        
# 1 - Fazer download de todos os zips que contenham bounty e exista uma plataforma
# 2 - Salvar o zip numa pasta da plataforma: Ex: yeswehack > arquivo1.zip ... arquivox.zip
# 3 - Extrair os arquivos zip e consolidar todos os txts em um unico com todas as URLS
# 4 - Remover as urls duplicadas e ordenar por ordem alfabetica


