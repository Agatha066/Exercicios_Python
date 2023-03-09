#minha versao do jogo

from random import randint
import time
import os

pontuacao = 100
tentativas = 5
valor_computador = randint(0,10)
rodada = 1
sair = 0

def verifica(comp,user):
    return int(user) == comp

def pts(pontuacao, rodada):
    return pontuacao - (20*(rodada-1))

MENSAGENS = {
    'DEFAULT': {
        'SAUDACAO': 'Escolhi um número entre 0 e 10. Tente adivinhar',
        'VITORIA': 'Parabéns!! Você acertou',
        'DERROTA': 'Que pena!! Você não acertou',
        'Info_JOGADOR': 'Digite um número entre 0 e 10: ',
        'NOVA_PARTIDA': 'Deseja continuar? (1-Sim; 0-Não) ',
        'ENCERRAMENTO': 'Até a próxima!!!',
        'PONTUACAO': lambda pontuacao: f'A sua pontuação final é {pontuacao} pontos'
    },
    'ERRO': {
        'TENTATIVA_INVALIDA': 'ERRO: São permitidos apenas números inteiros entre 0 e 10',
        'NOVA_PARTIDA_INVALIDA': 'ERRO: São permitidas apenas as opções: 1-Sim ou 2-Não',
    }
}

while sair != 1:

    print('-'*70)
    print('\t'+MENSAGENS.get('DEFAULT').get('SAUDACAO'))
    print('-'*70)
    print(f'\nRodada: {rodada} / 6 \t Vidas: {tentativas}')
    print(valor_computador)
    valor_user = input(MENSAGENS.get('DEFAULT').get('Info_JOGADOR'))
    print('-'*70)

    if verifica(valor_computador, valor_user):
        print('\t'+MENSAGENS.get('DEFAULT').get('VITORIA'))
        print('\t'+MENSAGENS.get('DEFAULT').get('PONTUACAO')(pts(pontuacao, rodada)))
        print('-'*70)
        print('-'*70)
                        
        sair = int( input('\t'+MENSAGENS.get('DEFAULT').get('NOVA_PARTIDA')))
        if sair == 0 :     
            print('-'*70) 
            print('\t'+MENSAGENS.get('DEFAULT').get('PONTUACAO')(pts(pontuacao, rodada)))
            print('\t'+MENSAGENS.get('DEFAULT').get('ENCERRAMENTO'))
            print('-'*70) 
            time.sleep(3)
            os.system('clear')
            os.system('cls')
            break
        else: 
            rodada = 1
            tentativas = 5
            continue  
    else:
       for i in range(tentativas):
            rodada+=1
            tentativas-=1
            print('-'*70)
            print(f'\nRodada: {rodada} / 6 \t Vidas: {tentativas}')
            valor_user = input(MENSAGENS.get('DEFAULT').get('Info_JOGADOR'))
            print('-'*70)
            print(valor_computador)
            if verifica(valor_computador, valor_user):
                print('-'*70)
                print('\t'+MENSAGENS.get('DEFAULT').get('VITORIA'))
                print('\t'+MENSAGENS.get('DEFAULT').get('PONTUACAO')(pts(pontuacao, rodada)))
                print('-'*70)

                sair = int(input('\t'+MENSAGENS.get('DEFAULT').get('NOVA_PARTIDA')))
                if sair == 0 :     
                   print('-'*70) 
                   print('\t'+MENSAGENS.get('DEFAULT').get('PONTUACAO')(pts(pontuacao, rodada)))
                   print('\t'+MENSAGENS.get('DEFAULT').get('ENCERRAMENTO'))
                   print('-'*70) 
                   time.sleep(3)
                   os.system('clear')
                   os.system('cls')
                   break
                else: 
                   rodada = 1
                   tentativas = 5
                   continue  
            else:
                if tentativas == 0:
                    print('-'*70)
                    print('\t'+MENSAGENS.get('DEFAULT').get('PONTUACAO')(pts(pontuacao, rodada)))
                    print('\t'+MENSAGENS.get('DEFAULT').get('DERROTA'))
                    print('-'*70)
                    print('-'*70)
                    sair = int(input('\t'+MENSAGENS.get('DEFAULT').get('NOVA_PARTIDA')))
                    if sair == 0 :     
                        print('-'*70)
                        print('\t'+MENSAGENS.get('DEFAULT').get('PONTUACAO')(pts(pontuacao, rodada)))
                        print('\t'+MENSAGENS.get('DEFAULT').get('ENCERRAMENTO'))
                        print('-'*70) 
                        time.sleep(3)
                        os.system('clear')
                        os.system('cls')
                        break
                    else: 
                        rodada = 1
                        tentativas = 5
                        continue  