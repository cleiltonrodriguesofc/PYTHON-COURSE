'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato 
Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Flamengo.'''

times = ("Botafogo", "Athletico-PR", "Bahia", "Bragantino", "Flamengo", "São Paulo", "Internacional", "Cruzeiro", "Atlético-MG", "Palmeiras", "Fortaleza", "Grêmio", "Vasco", "Juventude", "Fluminense", "Criciúma", "Corinthians", "Atlético-GO", "Vitória", "Cuiabá")
print('OS PRIMEIROS COLOCADOS SÃO:')
for time in range(0, 5):
    print(F'{time+1}° - {times[time]}')
print('OS QUATRO ÚLTIMOS COLOCADOS SÃO:')
for time in range(16, 20):
    print(F'{time}° - {times[time]}')
print('OS TIMES EM ORDEM ALFABÉTICA:')
ordem = sorted(times)
for time in ordem:
    print(time)
print(f'O Flamengo está na {times.index("Flamengo")}')
print({times.index('Flamengo')})