# import modulos_verificacao
print()
print('Questionário')

def ifHadOne(dados_enviados_do_usuario):
    if len(dados_enviados_do_usuario) > 1 or len(dados_enviados_do_usuario) < 0:
        return False
    if dados_enviados_do_usuario != 'a' and dados_enviados_do_usuario != 'b' and dados_enviados_do_usuario != 'c' and dados_enviados_do_usuario != 'd' and dados_enviados_do_usuario != 'e':
        return 'Alternativa inválida!'
    return True

perguntas = {
    'Pergunta 1': {'pergunta': 'Quanto é 50 + 50?', 'respostas': {
        'a': '1',
        'b': '200',
        'c': '150',
        'd': '100',
        'e': '50'
    }, 'resposta_certa': 'd'},
    'Pergunta 2': {
        'pergunta': 'O que significa THC?',
        'respostas': {
            'a': 'Trihidrocarboneto',
            'b': 'Tetrahidrocarboneto',
            'c': 'Tetrah2corlean',
            'd': 'Tetrahidrocanabinol',
            'e': 'Tetrahidrocanabidiol'
        },
        'resposta_certa': 'd'
    },
    'Pergunta 3': {
        'pergunta': 'Qual é a empresa mais valiosa do mundo?',
        'respostas': {
            'a': 'Microsoft',
            'b': 'Amazon',
            'c': 'Apple',
            'd': 'Meta',
            'e': 'Tesla'
        },
        'resposta_certa': 'c'
    },
    'Pergunta 4': {
        'pergunta': 'Qual o país que tem a maior biodiversidade do mundo?',
        'respostas': {
            'a': 'Austrália',
            'b': 'India',
            'c': 'Cuba',
            'd': 'Brasil',
            'e': 'Peru'
        },
        'resposta_certa': 'd'
    },
    'Pergunta 5': {
        'pergunta': 'Quanto é 10 - 10 * 2?',
        'respostas': {
            'a': '20',
            'b': '0',
            'c': '10',
            'd': '30',
            'e': '15'
        },
        'resposta_certa': 'c'
    },
    'Pergunta 6': {
        'pergunta': 'Quantas patas tem uma aranha?',
        'respostas': {
            'a': '6',
            'b': '5',
            'c': '10',
            'd': '9',
            'e': '8'
        },
        'resposta_certa': 'e'
    },
    'Pergunta 7': {
        'pergunta': 'Quantos graus a torre de Pisa é inclinada?',
        'respostas': {
            'a': '4,9 graus',
            'b': '5,3 graus',
            'c': '4,1 graus',
            'd': '2.7 graus',
            'e': '3,9 graus'
        },
        'resposta_certa': 'e'
    },
    'Pergunta 8': {
        'pergunta': 'Qual a altura da Torre Eiffel?',
        'respostas': {
            'a': '250 m',
            'b': '300 m',
            'c': '150 m',
            'd': '200 m',
            'e': '100 m'
        },
        'resposta_certa': 'b'
    },
    'Pergunta 9': {
        'pergunta': 'Qual o animal da nota de 200?',
        'respostas': {
            'a': 'Arara',
            'b': 'Garça',
            'c': 'Peixe',
            'd': 'Lobo',
            'e': 'Guará'
        },
        'resposta_certa': 'd'
    },
    'Pergunta 10': {
        'pergunta': 'Em que ano Hittler cometeu suicídio?',
        'respostas': {
            'a': '1945',
            'b': '1948',
            'c': '1950',
            'd': '1941',
            'e': '1955'
        },
        'resposta_certa': 'a'
    },
    'Pergunta 11': {
        'pergunta': 'Qual o coletivo de Elefante? (você me ama?)',
        'respostas': {
            'A': 'Ma nada',
            'b': 'Alcateia',
            'c': 'Matilha',
            'd': 'Bando',
            'e': 'Cardume'
        },
        'resposta_certa': 'a'
    },
    'Pergunta 12': {
        'pergunta': 'Qual é o maior país do mundo?',
        'respostas': {
            'a': 'Brasil',
            'b': 'Austrália',
            'c': 'Rússia',
            'd': 'China',
            'e': 'Inglaterra'
        },
        'resposta_certa': 'c'
    },
    'Pergunta 13': {
        'pergunta': 'Qual é o menor país do mundo?',
        'respostas': {
            'a': 'Jordânia',
            'b': 'Iraque',
            'c': 'Japão',
            'd': 'China',
            'e': 'Vaticano'
        },
        'resposta_certa': 'e'
    },
    'Pergunta 14': {
        'pergunta': 'Com quantos paus se faz uma canoa?',
        'respostas': {
            'a': '1',
            'b': '5',
            'c': '10',
            'd': '100',
            'e': '20'
        },
        'resposta_certa': 'a'
    },
    'Pergunta 15': {
        'pergunta': 'Qual é o prato principal do Brasil?',
        'respostas': {
            'a': 'Estrogonofe',
            'b': 'Estrela do mar',
            'c': 'Panquecas',
            'd': 'Feijoada',
            'e': 'Baião de dois'
        },
        'resposta_certa': 'd'
    },
}
print()
respostas_certas = 0
resposta_usuario = ''
erradas = {}
for perg_key, perg_valor in perguntas.items():
    print(f"{perg_key}: {perg_valor['pergunta']}")
    print('Alternativas:')

    for resp_key, resp_valor in perg_valor['respostas'].items():
        print(f'[{resp_key}]: {resp_valor}')

    resposta_usuario = input('Sua resposta: ')

    variavelk = ifHadOne(resposta_usuario)

    if not variavelk:
        print('Lembrando que será considerada apenas a primeira letra inserida!')

    elif variavelk is not True and variavelk is not False:
        print(variavelk)
        print('=/')
        continue

    resposta_unica = resposta_usuario.__getitem__(0)

    if resposta_unica.isupper():
        resposta_unica = resposta_unica.lower()

    if resposta_unica == perg_valor['resposta_certa']:
        respostas_certas += 1
        print(';)')
    else:
        erradas[perg_key] = resposta_unica
        print('=/')
    print()

porcentagem_acerto = respostas_certas / len(perguntas) * 100
print(f'De {len(perguntas)} você acertou {respostas_certas} tendo um acerto de {porcentagem_acerto}%')
print(f'Essas foram as que você errou: {erradas} ')
