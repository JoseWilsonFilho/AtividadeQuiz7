print('''Quantos títulos de campeonato brasileiro o Flamengo tem?
a - 10
b - 8
c - 9''')
resposta = input().lower()

if resposta == 'a':
    print('Errado!')
elif resposta == 'b':
    print('Perfeito, o maior do Brasil!')
elif resposta == 'c':
    print('Ainda não')
else:
    print('Você não escolheu a, b ou c :(')
    
