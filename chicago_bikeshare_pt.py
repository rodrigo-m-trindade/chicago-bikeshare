# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

#----> change standard path
#import os
#os.chdir('C:\\Users\\rodrigo.m.trindade\\Desktop\\Udacity\\Data Science I\\Projeto I\\chicago-bikeshare-pt')

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for i in range(1,21):
    print(data_list[i])


# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for i in range(20):
    print(str(i+1) + ': ' + data_list[i][6])

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    """
    Função para adicionar coluna de uma lista em outra lista.
    Argumentos:
        data: lista a ser copiada
        index: indice que indica a coluna a ser copiada.
    Retorna:
        Uma lista com a coluna copiada da lista de entrada.
    """
    column_list = []
    
    for i in range(len(data)):
        column_list.append(data[i][index])
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.
male = 0
female = 0

def count_genders(data,gender):
    """
    Função para contar as ocorrencias de um determinado genero.
    Argumentos:
        data: lista a ser lida.
        gender: string que identifica o genero a ser pesquisado.
    Retorna:
        Variável int com a quantidade de ocorrencias do genero pesquisado.
    """    
    count_gender = 0
    for i in range(len(data)):
        if data[i][-2] == gender:
            count_gender += 1
    return(count_gender)

male = count_genders(data_list,'Male')
female = count_genders(data_list,'Female')
            

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """
    Função para contar as ocorrencias dos generos "Male" e "Female".
    Argumentos:
        data_list: lista a ser lida.
    Retorna:
        Duas variáveis int com o numero da ocorrencia de cada genero.
    """        
    male = 0
    female = 0
    for i in range (len(data_list)):
        if data_list[i][-2] == 'Male':
            male += 1
        elif data_list[i][-2] == 'Female':
            female += 1
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data_list):
    """
    Função para verificar qual o genero mais popular, de acordo com a contagem feita anteriormente.
    Argumentos:
        lista de dados.
    Retorna:
        String com o gênero mais popular.
    """        
    counter = count_gender(data_list)
    male = counter[0]
    female = counter[1]
    
    if male > female:
        answer = "Masculino"
    elif female > male:
        answer = "Feminino"
    else:
        answer = "Igual"
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.

def count_user_types(data):
    """
    Função para contar as ocorrencias de tipos de usuários em uma lista.
    Argumentos:
        data: lista a ser lida.
    Retorna:
        Duas variáveis int com o numero da ocorrencia de cada tipo de usuario.
    """        
    customer = 0
    subscriber = 0
    for i in range (len(data)):
        if data_list[i][-3] == 'Customer':
            customer += 1
        elif data_list[i][-3] == 'Subscriber':
            subscriber += 1
            
    return [customer, subscriber]

print(count_user_types(data_list))

print("\nTAREFA 7: Verifique o gráfico!")
gender_list = column_to_list(data_list, -3)
types = ["Customer", "Subscriber"]
quantity = count_user_types(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de Usuario')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo de Usuario')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Por que no arquivo usado há linhas onde esta coluna está em branco."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.

def calc_trip(tdl):
    """
    Função para calcular as seguintes medidas relativa a duração das viagens:
        - Viagem com menor duraçao;
        - Viagem com maior duração;
        - Media do tempo de viagem;
        - Mediana do tempo de viagem;
    Argumentos:
        tdl: lista com os tempos de duração das corridas.
    Retorna:
        4 variaveis com as informacoes calculadas, na ordem:
            - Viagem com menor duraçao;
            - Viagem com maior duração;
            - Media do tempo de viagem;
            - Mediana do tempo de viagem;            
            
    """        
    min_t = int(tdl[0])
    max_t = 0
    count_t = 0
    mean_t = 0
    med_t = 0
    tdl_int = []

    for i in range(len(tdl)):
        tdl_int.append(int(tdl[i])) #cria nova lista com valores inteiros
    
    for i in range(len(tdl_int)):
        if tdl_int[i] > max_t: #verifica se o numero lido é maior do que o guardado
            max_t = tdl_int[i]
        if tdl_int[i] < min_t: #verifica se o numero lido é menor do que o guardado
            min_t = tdl_int[i]
        count_t += tdl_int[i]  #acumula os valores
    
    mean_t = count_t / len(tdl_int) #calcula a media
    
    tdl_s = sorted(tdl_int) #ordena a lista de numeros
     
    if len(tdl_s) % 2 == 0:  #verifica se o tamanho da lista é par ou impar
        x = int(len(tdl_s)/2)
        y = int(x - 1)
        med_t = int((tdl_s[x] + tdl_s[y])/2)
    else:
        x = int(len(tdl_s)/2)
        med_t = tdl_s[x]
    
    return(min_t,max_t,mean_t,med_t)
    
min_trip = calc_trip(trip_duration_list)[0]
max_trip = calc_trip(trip_duration_list)[1]
mean_trip = calc_trip(trip_duration_list)[2]
median_trip = calc_trip(trip_duration_list)[3]

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_station_list = column_to_list(data_list, 3)
user_types = set(start_station_list)

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""
      Função de exemplo com anotações.
      Argumentos:
          param1: O primeiro parâmetro.
          param2: O segundo parâmetro.
      Retorna:
          Uma lista de valores x.

"""

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list):
    item_types = []
    count_items = []
    
    item_types = list(set(column_list))

    for i in range(len(item_types)):
        count_items.append(column_list.count(item_types[i]))

    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------