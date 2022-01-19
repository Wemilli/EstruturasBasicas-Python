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