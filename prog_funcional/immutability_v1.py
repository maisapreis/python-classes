
# Immutability: dados imutáveis.
# Estes métodos (map, filter, reduce) não modificam o objeto iniciam, eles criam novos objetos.

from calendar import mdays, month_name
from locale import setlocale, LC_ALL
from functools import reduce

setlocale(LC_ALL, 'pt_BR')

# Lista todos os meses do ano com 31 dias.
# 1 - Filter para pegar indices dos meses
# 2 - Map para transformar indices em nome
# 3 - Reduce para juntar tudo e imprimir

print(list(month_name))
print(list(month_name[1:13]))

meses_31 = filter(lambda mes: mdays[mes] == 31, range(1, 13))
meses_nomes = map(lambda mes: month_name[mes], meses_31)
juntar_meses = reduce(lambda todos, nome_mes: f'{todos}\n- {nome_mes}',
                      meses_nomes, 'Meses com 31 dias:')

print(juntar_meses)