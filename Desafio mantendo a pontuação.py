print('''Quantos títulos de campeonato brasileiro o Flamengo tem?
a - 10
b - 8
c - 9''')
resposta = input().lower()
score = 0
pontuacao = score+1 
if resposta == 'a':
    print(f'Errado! Sua pontuação é {score}')
elif resposta == 'b':
    print(f'Perfeito, o maior do Brasil! Sua pontuação é {pontuacao}')
elif resposta == 'c':
    print(f'Ainda não! Sua pontuação é{score}')
else:
    print(f'Você não escolheu a, b ou c :(')


if resposta == 'b':
    print('Muito bem!')
else:
    print('Tente novamente!')
    

