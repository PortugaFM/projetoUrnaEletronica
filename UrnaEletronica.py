##Funções##

#Aqui se iniciará o programa, dando a escolha de imprimir Zerésima ou iniciar a votação
def IniciodeTudo():
    print('--' * 10)
    print('Bem-vindo(a) as votações para vereadores e prefeitos da cidade de São Paulo.')
    print('--' * 10)

    menu = input("Selecione 1 para Imprimir Zerésima ou 2 para Iniciar Votação: ")
    print(menu)
    if menu == str('1'):
        print("Todos os candidatos estão sem votos computados")

    else:
        InicioVotacao()

#Caso seja escolhida a votação, aqui será onde o eleitor poderá iniciar suas escolhas, e para onde o código voltará a cada eleitor
def InicioVotacao():

    votacaoVereador = IniciarVotacaoVereador()

    votacaoPrefeito = IniciarVotacaoPrefeito()

    ContinuarouFinalizar()

#A votação para vereador se inicia aqui
def IniciarVotacaoVereador():
    print('--' * 10)
    print("Bem vindo a escolha dos candidatos a VEREADOR.")
    print('--' * 10)
    votacaoVereador = input("Digite 1 para votar no vereador ou 2 para votar em Branco: ")
    if votacaoVereador == '1':
        VotoValidoVereador()
    else:
        VotoBrancoVereador()

#Caso o voto para vereador seja um número válido, o programa deverá cair nessa condição, que contabilizará o voto como válido
def VotoValidoVereador():
    print('--' * 10)
    vereador = input("Digite o número do vereador com 5 dígitos: ")
    print('--' * 10)
    print(vereador)
    verifica = False

    if vereador == str('00001'):
        print("João")
        print("Partido: PSDB")
        verifica = True
    elif vereador == str('00002'):
        print("Fernando")
        print("Partido: PSDB")
        verifica = True
    elif vereador == '00003':
        print("Gustavo")
        print("Partido: PSDB")
        verifica = True
    elif vereador == '00004':
        print("José")
        print("Partido: PSDB")
        verifica = True
    elif vereador == '00005':
        print("Felipe")
        print("Partido: PSDB")
        verifica = True
    elif vereador == '00006':
        print("Eduardo")
        print("Partido: PSDB")
        verifica = True
    elif vereador == '00007':
        print("Pedro")
        print("Partido: PSDB")
        verifica = True
    elif vereador == '00008':
        print("Gabriel")
        print("Partido: PSDB")
        verifica = True
    elif vereador == '00009':
        print("Vinicius")
        print("Partido: PSDB")
        verifica = True
    elif vereador == '00010':
        print("Armando")
        print("Partido: PSDB")
        verifica = True
    else:
        print('--' * 10)
        print("Candidato a vereador não existe. Seu voto será computado como NULO")
        print('--' * 10)
        verifica = False

    confirmarVotoVereador = (input("Confirmar??? Digite 1 para SIM ou 2 para reiniciar a votação para Vereador: "))
    print(confirmarVotoVereador)
    if confirmarVotoVereador == str('1'):
        if verifica == True:
            print('--' * 10)
            print("Seu voto foi confirmado")
            print('--' * 10)
            votosIndividuaisVereador[vereador]["qtdvotos"] +=1

        else:
            print('--' * 10)
            print("Seu voto foi computado como Nulo")


    if confirmarVotoVereador == str('2'):
        IniciarVotacaoVereador()

#Caso o voto para vereador não seja um número válido, o programa deverá cair nessa condição, que contabilizará o voto como nulo
def VotoBrancoVereador():
    print('--' * 10)
    print("Você votou em BRANCO.")
    print('--' * 10)
    votoBrancoVereador = (input("Deseja confirmar??? Digite 1 para SIM ou 2 para reiniciar a votação para Vereador: "))
    print('--' * 10)

    if votoBrancoVereador == str('1'):
        print('--' * 10)
        print("O seu voto foi computado como NULO!!!")
        print('--' * 10)
    else:
        IniciarVotacaoVereador()

#A votação para prefeito se inicia aqui
def IniciarVotacaoPrefeito():
    print("********** Agora é a vez de escolher o PREFEITO. **********")
    print('--' * 10)
    votacaoPrefeito = input("Digite 1 para votar no Prefeito ou 2 para votar em Branco: ")
    print(votacaoPrefeito)

    if votacaoPrefeito == '1':
        VotoValidoPrefeito()
    else:
        VotoBrancoPrefeito()

#Caso o voto para prefeito seja um número válido, o programa deverá cair nessa condição, que contabilizará o voto como válido
def VotoValidoPrefeito():
    print('--' * 10)
    prefeito = input("Digite o número do Prefeito: ")
    print('--' * 10)
    print(prefeito)
    verifica = False

    if prefeito == str('01'):
        print("Amadeu")
        print("Partido: PSDB")
        verifica = True

    elif prefeito == str('02'):
        print("Flávio")
        print("Partido: PSDB")
        verifica = True

    elif prefeito == '03':
        print("Rafael")
        print("Partido: PSDB")
        verifica = True

    else:
        print('--' * 10)
        print("Candidato a Prefeito não existe. Seu voto será computado como NULO")
        print('--' * 10)
        verifica = False

    confirmarVotoPrefeito = (input("Confirmar??? Digite 1 para SIM ou 2 para reiniciar a votação para Prefeito: "))
    print(confirmarVotoPrefeito)
    if confirmarVotoPrefeito == str('1'):
        if verifica == True:
            print('--' * 10)
            print("Seu voto foi confirmado")
            print('--' * 10)
            votosIndividuaisPrefeito[prefeito]["qtdvotos"] += 1

        else:
            print('--' * 10)
            print("Seu voto foi computado como Nulo")

    if confirmarVotoPrefeito == str('2'):
        IniciarVotacaoPrefeito()

#Caso o voto para prefeito não seja um número válido, o programa deverá cair nessa condição, que contabilizará o voto como nulo
def VotoBrancoPrefeito():
    print('--'*10)
    print("Você votou em BRANCO.")
    print('--'*10)
    votoBrancoPrefeito = (input("Deseja confirmar??? Digite 1 para SIM ou 2 para reiniciar a votação para Prefeito: "))

    if votoBrancoPrefeito == str('1'):
        print('--'*10)
        print("O seu voto foi computado como NULO!!!")
        print('--'*10)
    else:
        IniciarVotacaoPrefeito()

#Após a votação de cada eleitor é possível finalizar a votação ou retornar à opção de votação de vereador e posteriormente de prefeito
def ContinuarouFinalizar():
    continuarOuFinalizarVotacao = (input("Você deseja continuar ou finalizar a votação? Digite 1 para continuar e 2 para finalizar a votação: "))
    print(continuarOuFinalizarVotacao)
    if continuarOuFinalizarVotacao == str('1'):
        InicioVotacao()
    else:
        print("Votação finalizada com sucesso")

#ContagemdosVotos
votosIndividuaisVereador = {
    "00001": {"qtdvotos":0,"nome":"João"},
    "00002": {"qtdvotos":0,"nome":"Fernando"},
    "00003": {"qtdvotos":0,"nome":"Gustavo"},
    "00004": {"qtdvotos":0,"nome":"José"},
    "00005": {"qtdvotos":0,"nome":"Felipe"},
    "00006": {"qtdvotos":0,"nome":"Eduardo"},
    "00007": {"qtdvotos":0,"nome":"Pedro"},
    "00008": {"qtdvotos":0,"nome":"Gabriel"},
    "00009": {"qtdvotos":0,"nome":"Vinicius"},
    "00010": {"qtdvotos":0,"nome":"Armando"}
}

votosIndividuaisPrefeito = {
    "01": {"qtdvotos":0,"nome":"Amadeu"},
    "02": {"qtdvotos":0,"nome":"Flávio"},
    "03": {"qtdvotos":0,"nome":"Rafael"}
}

#A Execução do programa começa aqui#

IniciodeTudo()

#Apuração dos votos para Vereador
for candidatoVereador in votosIndividuaisVereador:
    qtdvotos = votosIndividuaisVereador[candidatoVereador]['qtdvotos']
    if qtdvotos == 1:
        voto = "voto"
    else:
        voto = "votos"

    nomeVereador = votosIndividuaisVereador[candidatoVereador]['nome']
    print(f"O candidato a vereador {nomeVereador} tem {qtdvotos} {voto} ")

votosVereadorOrdenados = sorted(votosIndividuaisVereador.items(), key=lambda x: x[1]["qtdvotos"], reverse=True)

vereadorVencedor = votosVereadorOrdenados[0][1]['nome']
vereadorSegundoLugar = votosVereadorOrdenados[1][1]['nome']
vereadorTerceiroLugar = votosVereadorOrdenados[2][1]['nome']

if votosVereadorOrdenados[0][1]['qtdvotos'] == 0:
    print(f"De acordo com esses resultados, nenhum vereador recebeu votos, e portanto não haverá vereador eleito")

elif votosVereadorOrdenados[1][1]['qtdvotos'] == 0:
    print(f"De acordo com esses resultados, apenas o candidato {vereadorVencedor} recebeu votos, e portanto será o único eleito")

elif votosVereadorOrdenados[2][1]['qtdvotos'] == 0:
    print(f"De acordo com esses resultados, apenas os candidatos {vereadorVencedor} e {vereadorSegundoLugar} recebram fotos, e portanto serão os únicos eleitos")

else:
    print(f"De acordo com esses resultados, os vereadores eleitos serão {vereadorVencedor}, {vereadorSegundoLugar} e {vereadorTerceiroLugar}")

print("\n")

#Apuração dos votos para Prefeito

for candidatoPrefeito in votosIndividuaisPrefeito:
    qtdvotos = votosIndividuaisPrefeito[candidatoPrefeito]['qtdvotos']
    if qtdvotos == 1:
        voto = "voto"
    else:
        voto = "votos"

    nomePrefeito = votosIndividuaisPrefeito[candidatoPrefeito]['nome']
    print(f"O candidato a prefeito {nomePrefeito} tem {qtdvotos} {voto} ")

votosPrefeitoOrdenados = sorted(votosIndividuaisPrefeito.items(), key=lambda x: x[1]["qtdvotos"], reverse=True)

prefeitoVencedor = votosPrefeitoOrdenados[0][1]['nome']
prefeitoSegundoLugar = votosPrefeitoOrdenados[1][1]['nome']

if votosPrefeitoOrdenados[0][1]['qtdvotos'] == 0:
    print(f"De acordo com esses resultados, nenhum prefeito recebeu votos, e portanto não haverá prefeito eleito")

elif votosPrefeitoOrdenados[0][1]['qtdvotos'] == votosPrefeitoOrdenados[1][1]['qtdvotos']:

    print(f"De acordo com esses resultados, haverá segundo turno entre os candidatos {prefeitoVencedor} e {prefeitoSegundoLugar}")

else:
    print(f"De acordo com esses resultados, o prefeito eleito será {prefeitoVencedor}")