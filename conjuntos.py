"""
# Suponha que você foi contratado para desenvolver uma funcionalidade
# no sistema do RH de um novo banco digital. Esse banco teve acesso
# ao cadastro de clientes de outras três empresas concorrentes
# (Nubank, C6 e Inter) e gostaria de saber quais são os potenciais
# clientes. Para isso, pediu que você gerasse um relatório com 12
# items. Atenção, use apenas um print por item.
"""

nubank = set(['ana', 'bia', 'clara', 'duda', 'fabio'])
c6     = set(['bia', 'elena', 'fabio', 'gabriel', 'helio'])
inter  = set(['duda', 'fabio', 'ilma', 'joão', 'katia', 'luiza'])

""" # 01) Quais são os clientes de cada uma, separadamente.  """
for nome in nubank:
    print(f'Cliente banco nubank: {nome}', end=', ')
print('\n')

for nome in c6:
    print(f'Cliente banco c6: {nome}', end=', ')
print('\n')

for nome in inter:
    print(f'Cliente banco inter: {nome}', end=', ')
print('\n')


""" # 02) Quais são os clientes de todas as concorrentes.  """
todos_clientes = nubank | c6 | inter
for nome in todos_clientes:
    print(f'Cliente dos bancos (nubank, c6 ou inter): {nome}', end=', ')
print('\n')


""" # 03) Quais são os clientes da Nubank que também são clientes do C6.  """
nubank_c6 = nubank & c6
print(f'São clientes do nubank e c6 ao mesmo tempo: {nubank_c6}')
print('\n')
    
""" # 04) Quais são os clientes da Nubank que também são clientes do Inter.  """
nubank_inter = nubank & inter
print(f'São clientes do nubank e inter ao mesmo tempo: {nubank_inter}')
print('\n')

""" # 05) Quais são os clientes do C6 que também são clientes do Inter.  """
c6_inter = c6 & inter
print(f'São clientes do c6 e inter ao mesmo tempo: {c6_inter}')
print('\n')

""" # 06) Quais são os clientes apenas da Nubank.  """
nubank_menos_inter = nubank - inter
so_nubank = nubank_menos_inter - c6
print(f'São clientes só do Nubank: {so_nubank}')
print('\n')

""" # 07) Quais são os clientes apenas do C6.  """
c6_menos_nubank = c6 - nubank
so_c6 = c6_menos_nubank - inter
print(f'São clientes só do C6: {so_c6}')
print('\n')

""" # 08) Quais são os clientes apenas do Inter.  """
inter_menos_nubank = inter - nubank
so_inter = inter_menos_nubank - c6
print(f'São clientes só do Inter: {so_inter}')
print('\n')


""" # 09) Clientes da Nubank e C6, mas não dos dois ao mesmo tempo. """
nubank_c6_nao_ao_mesmo_tempo = nubank ^ c6
print(f'São clientes do Nubank ou C6, mas não ambos: {nubank_c6_nao_ao_mesmo_tempo}')
print('\n')

""" # 10) Clientes da Nubank e Inter, mas não das duas ao mesmo tempo.  """
nubank_inter_nao_ao_mesmo_tempo = nubank ^ inter
print(f'São clientes do Nubank ou Inter, mas não ambos: {nubank_inter_nao_ao_mesmo_tempo}')
print('\n')

""" # 11) Clientes do C6 e Inter, mas não dos dois ao mesmo tempo.  """
c6_inter_nao_ao_mesmo_tempo = c6 ^ inter
print(f'São clientes do C6 ou Inter, mas não ambos: {c6_inter_nao_ao_mesmo_tempo}')
print('\n')

""" # 12) Quais são os clientes das três simultaneamente.  """
tres_ao_mesmo_tempo = nubank & inter & c6
print(f'São clientes das três ao mesmo tempo: {tres_ao_mesmo_tempo}')
