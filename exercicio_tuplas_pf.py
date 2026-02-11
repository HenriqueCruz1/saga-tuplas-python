print('Estudando a tabela do Brasileirão 2026')

def cinco_primeiros(tabela):
    return tabela[:5]

def quatro_ultimos(tabela):
    return tabela[-4:]

def ordem_alfabetica(tabela):
    return sorted(tabela)

def posicao_time(tabela, time):
    return tabela.index(time)+1


tabela = ('Bragantino','Palmeiras','Chapecoense','Mirassol', 'Fluminense','Bahia','São Paulo','Botafogo',
                        'Grêmio','Athletico-PR','Coritiba','EC Vitória','Flamengo','Atlético-MG','Vasco da Gama',
                        'Internacional','Santos','Remo','Corinthians','Cruzeiro')

print(f'Os cinco primeiros colocados são:{cinco_primeiros(tabela)}')
print(f'Os quatro ultimos colocados são:{quatro_ultimos(tabela)}')
print(f'Todos os times em ordem alfabética fica:{ordem_alfabetica(tabela)}')
time = 'Chapecoense'
print(f'A {time} está na {posicao_time(tabela,time)}º posição')