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



