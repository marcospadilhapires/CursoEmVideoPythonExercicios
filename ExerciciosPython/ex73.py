times = ('Botafogo','Palmeiras','Flamengo','Atlético-MG','Fluminense','São Paulo','Grêmio',
        'Fortaleza','Athletico-PR','Cruzeiro','Internacional','Bragantino','Santos','Bahia',
        'Corinthians','Cuiabá','Goiás','América-MG','Vasco','Coritiba')

print("=-"*10)
print(f"Lista de Times do Brasileirão: {times}")
print("=-"*10)
print(f"Os 5 primeiros colocados são: {times[0:5]}")
print("=-"*10)
print(f"Os útimos 4 colocados são: {times[-4:]}")
print("=-"*10)
print(f"O times em ordem alfabética são:{sorted(times)}")
print("=-"*10)
print(f"O time Sâo Paulo está na {times.index('São Paulo') + 1}° posição do campeonato")