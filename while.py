'''Sistema de vendas:
 Nosso programa deve registrar os produtos e as quantidades e adicionar em uma lista.
O programa deve continuar rodando até o input ser vazio, ou seja, o usuário apertar enter sem digitar nenhum produto ou quantidade.
Ao final do programa, ele deve printar todos os produtos e quantidades vendidas.'''

vendas = []

while True:
    produto = input('Qual o produto?')
    if not produto:
        break
    qtde = int(input('Qual a quantidade?'))
    vendas.append([produto, qtde])

print(vendas)