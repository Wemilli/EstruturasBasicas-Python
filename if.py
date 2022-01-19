'''PROPOSTA:
Crie um sistema para ser usado pelo time de controle de estoque de um centro de distribuição.
Imagine que ao fim de todo dia, o time conta quantas unidades de produto existem no estoque.
Se tivermos um estoque abaixo do estoque permitido para aquela categoria do produto,
o time deve ser avisado para fazer um novo pedido daquele produto.'''

produto = input('Qual o produto?')
categoria = input('Qual a categoria do produto?')
qtde = input('Qual a quantidade atual do produto?')

if produto and categoria and qtde:
    qtde = int(qtde)
    if categoria == 'bebidas':
        if qtde < 75:
            print('Solicitar {} à equipe de compras, temos apenas {} unidades em estoque'.format(produto, qtde))
    elif categoria == 'limpeza':
        if qtde < 30:
            print('Solicitar {} à equipe de compras, temos apenas {} unidades em estoque'.format(produto, qtde))
    else:
        if qtde < 50:
            print('Solicitar {} à equipe de compras, temos apenas {} unidades em estoque'.format(produto, qtde))
else:
    print('Preencha todas as informações')