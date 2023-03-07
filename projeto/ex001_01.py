# Desenvolva um jogo de acerte o número, onde o computador escolhe um número inteiro aleatório de 0 a 10, e o usuário tem 5 tentativas para adivinhar o número
#OBS.: O design da tela pode ser implementado livremente
#(PLUS): Implemente um sistema de pontuação com o seguinte comportamento: se o usuário adivinhar o número na primeira tentativa, receberá a pontuação máxima (ex. 100 pontos); se o usuário adivinhar o número na última tentativa, receberá a pontuação mínima (ex. 10 pontos); se o usuário não acertar o número, não receberá nenhum ponto.
#(PLUS): Implemente um controle de erros. Caso o jogador digite um número fora da faixa permitida ou caracteres não numéricos, o sistema deve notificar o jogador e solicitar o input correto.
#(PLUS): Implemente a opção de o usuário iniciar uma nova partida. Ao finalizar uma rodada, após o resultado final, o jogo deve perguntar se o jogador quer iniciar uma nova partida e, em caso negativo, encerrar a aplicação.
from random import randint

DEBUG = False
TENTATIVAS = 6
TOTAL_RODADAS = TENTATIVAS - 1
PONTUACAO_MAXIMA = 100

Mensagens = {
    'Default': {
        'SAUDACAO': 'Escolhi um número entre 0 e 10. Tente adivinhar',
        'VITORIA': 'Parabéns!! Você acertou',
        'DERROTA': 'Que pena!! Você não acertou',
        'INPUT_JOGADOR': 'Digite um número entre 0 e 10: ',
        'NOVA_PARTIDA': 'Gostaria de jogar novamente? (1-Sim; 2-Não) ',
        'ENCERRAMENTO': 'Até a próxima!!!',
        'PONTUACAO': lambda pontuacao: f'A sua pontuação final é {pontuacao} pontos'
    },
    'Erro': {
        'TENTATIVA_INVALIDA': 'ERRO: São permitidos apenas números inteiros entre 0 e 10',
        'NOVA_PARTIDA_INVALIDA': 'ERRO: São permitidas apenas as opções: 1-Sim ou 2-Não',
    }
}

