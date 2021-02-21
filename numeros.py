
from util import calculo as calc, mensagem as mens
from colorama import init
init()


def aula22():
    mens.print_title('Aula sobre Módulo e Packages(PyCharm) - Aula 22', cor=mens.red_bold)

    print(f'{mens.yellow_} Entre com um número: {mens.green_}', end='')
    num = int(input(''))
    print(mens.default_)

    print(f' O fatorial de {mens.green_}{num}!{mens.default_} ={mens.yellow_}{calc.fatorial(num)}{mens.default_}')
    print()
    mens.print_end()


def moeda107():
    mens.print_title('Prática de uso de Módulo: import calculo')
    preco = float(input('  Digite o preço do produto   R$ : '))
    aumento = float(input('  Quanto foi aumento de preço(%) : '))
    reducao = float(input('  Quanto vai ser reduzido(%)     : '))
    print('-'*40)
    print(f'  A metade de R$ {preco:6.2f} é R$ {calc.metade(preco):.2f}.')
    print(f'  O dobro  de R$ {preco:6.2f} temos R$ {calc.dobro(preco):.2f}.')
    print(f'  Aumentando  {aumento:5.2f}%, temos R$ {calc.aumentar(preco, aumento):.2f}.')
    print(f'  Diminuindo  {reducao:5.2f}%, temos R$ {calc.diminuir(preco, reducao):.2f}.')
    print('-'*40)
    mens.print_end()


def moeda108():
    mens.print_title('Prática de uso de Módulo: import calculo')
    preco = float(input('  Digite o preço do produto   R$ : '))
    aumento = float(input('  Quanto foi aumento de preço(%) : '))
    reducao = float(input('  Quanto vai ser reduzido(%)     : '))
    print('-'*40)
    print(f'  A metade de {calc.fmoeda(preco)} é {calc.fmoeda(calc.metade(preco))}.')
    print(f'  O dobro  de {calc.fmoeda(preco)} temos {calc.fmoeda(calc.dobro(preco))}.')
    print(f'  Aumentando  {calc.fnumero(aumento)}%, temos {calc.fmoeda(calc.aumentar(preco, aumento))}.')
    print(f'  Diminuindo  {calc.fnumero(reducao)}%, temos {calc.fmoeda(calc.diminuir(preco, reducao))}.')
    print('-'*40)
    mens.print_end()


def moeda109():
    mens.print_title('Prática de uso de Módulo: import calculo')
    preco = float(input('  Digite o preço do produto   R$ : '))
    aumento = float(input('  Quanto foi aumento de preço(%) : '))
    reducao = float(input('  Quanto vai ser reduzido(%)     : '))
    print('-'*40)
    print(f'  A metade de {calc.fmoeda(preco)} é {calc.metade(preco, False)}.')
    print(f'  O dobro  de {calc.fmoeda(preco)} temos {calc.dobro(preco, True)}.')
    print(f'  Aumentando  {calc.fnumero(aumento)}%, temos {calc.aumentar(preco, aumento, True)}.')
    print(f'  Diminuindo  {calc.fnumero(reducao)}%, temos {calc.diminuir(preco, reducao,  True)}.')
    print('-'*40)
    mens.print_end()


def moeda110():
    mens.print_title('Prática de Módulo: import calculo')
    preco = float(input('  Digite o preço do produto   R$ : '))
    aumento = float(input('  Quanto foi aumento de preço(%) : '))
    reducao = float(input('  Quanto vai ser reduzido(%)     : '))
    calc.resumo(preco, aumento, reducao)
    mens.print_end()


def moeda111():
    mens.print_title('Prática de Módulo e Package: import calculo, mensagem')
    preco = mens.leianumero('  Digite o preço do produto   R$ : ')
    aumento = mens.leianumero('  Quanto foi aumento de preço(%) : ')
    reducao = mens.leianumero('  Quanto vai ser reduzido(%)     : ')
    calc.resumo(preco, aumento, reducao)
    mens.print_end()


def main():
    # moeda107() # ex.107
    # moeda108()
    # Moeda109()
    # moeda110()
    moeda111()


main()