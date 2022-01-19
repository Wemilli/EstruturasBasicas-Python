'''Temos uma lista de vendedores e queremos calcular o % de
vendedores que bateram a meta e qual foi o melhor vendedor.'''

meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]
'''
# cálculo diretamente na lista
qtde_vendedores_acima = 0

for venda in vendas:
    if venda[1] >= meta:
        qtde_vendedores_acima += 1

print('{:.1%} dos vendedores bateram a meta'.format(qtde_vendedores_acima / len(vendas)))'''


# criando lista auxiliar
acima_meta = []

for venda in vendas:
    if venda[1] >= meta:
        acima_meta.append(venda)

print(acima_meta)
print('{:.1%} dos vendedores bateram a meta'.format(len(acima_meta) / len(vendas)))

melhor_vendedor = ''
maior_vendas = 0

for venda in vendas:
    if venda[1] > maior_vendas:
        maior_vendas = venda[1]
        melhor_vendedor = venda[0]

print('O melhor vendedor foi {} com {} vendas'.format(melhor_vendedor, maior_vendas))