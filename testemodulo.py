
from util import calculo as calc, mensagem as mens, dados as dad
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
    ''' Foi introduzido do package:util módulo:calculo as funções:
        metade, dobro, aumentar, diminuir
        Foi introduzido a entrada de preço do produto, e aumento e redução deste.
        Faz se uso de funções para criar título: mens.print(), finalização: mens.print_end()
        Todas as saídas apresentam formatação por default´ 
    '''
    mens.print_title('#107 - Prática de Módulo: import calculo')
    preco = float(input('  Digite o preço do produto   R$ : '))
    aumento = float(input('  Quanto foi aumento de preço(%) : '))
    reducao = float(input('  Quanto vai ser reduzido(%)     : '))
    print('-'*40)
    print(f'  A metade de R$ {preco:6.2f} é R$ {calc.metade(preco)}.')
    print(f'  O dobro  de R$ {preco:6.2f} temos R$ {calc.dobro(preco)}.')
    print(f'  Aumentando  {aumento:5.2f}%, temos R$ {calc.aumentar(preco, aumento)}.')
    print(f'  Diminuindo  {reducao:5.2f}%, temos R$ {calc.diminuir(preco, reducao)}.')
    print('-'*40)
    mens.print_end()


def moeda108():
    ''' Foi introduzido a funções:
        :fmoeda e fnumero para formatar o produto e porcentagem .
    '''
    mens.print_title('#108 -Prática de Módulo: import calculo')
    preco = float(input('  Digite o preço do produto   R$ : '))
    aumento = float(input('  Quanto foi aumento de preço(%) : '))
    reducao = float(input('  Quanto vai ser reduzido(%)     : '))
    print('-'*40)
    print(f'  A metade de {calc.fmoeda(preco)} é R${calc.metade(preco)}.')
    print(f'  O dobro  de {calc.fmoeda(preco)} temos R${calc.dobro(preco)}.')
    print(f'  Aumentando  {calc.fnumero(aumento)}%, temos R${calc.aumentar(preco, aumento)}.')
    print(f'  Diminuindo  {calc.fnumero(reducao)}%, temos R${calc.diminuir(preco, reducao)}.')
    print('-'*40)
    mens.print_end()


def moeda109():
    '''Foi modificado as funções:
        :metade, dobro, aumentar e diminuir do modulo(package) Calculo
        :cria novo parâmetro True/False para impressão no formato moeda
        :faz nova consi
    '''
    mens.print_title('#109 - Prática de Módulo: import calculo')
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
    ''' Foi criado uma nova função:resumo no modulo:dados.
        Apresenta um resumo do preço, dobro, metade, aumento e redução do preço
        Este programa o prof. Guanabara, pede o uso mais de um módulo: 
        :package: util  modulo: calculo, mensagem, dados, colorama(ativa cores ANSI)
    '''
    mens.print_title('#110 - Prática de Módulo: import calculo')
    preco = float(input('  Digite o preço do produto   R$ : '))
    aumento = float(input('  Quanto foi aumento de preço(%) : '))
    reducao = float(input('  Quanto vai ser reduzido(%)     : '))
    dad.resumo(preco, aumento, reducao)


def moeda111():
    ''' Valida a entrada do preço usando try / except(não mencionado até então).
        Foi extendido para todas entradas: aumento, redução em porcentagem.
    ''' 
    mens.print_title('#111 -Prática de Package:util e modulo:import calculo, mensagem')
    preco = mens.leianumero('  Digite o preço do produto   R$ : ')
    aumento = mens.leianumero('  Quanto foi aumento de preço(%) : ')
    reducao = mens.leianumero('  Quanto vai ser reduzido(%)     : ')
    dad.resumo(preco, aumento, reducao)
    mens.print_end()


def main():
    print()
    mens.print_title('Aula sobre Módulo e Package')
    while True:
        print('  (1): Exercício 107')
        print('  (2): Exercício 108')
        print('  (3): Exercício 109')
        print('  (4): Exercício 110')
        print('  (5): Exercício 111/112')
        print('-'*40)
        num = str(input('  Escolha um opção: [99-sair] '))
        if num.isnumeric(): 
            num1 = int(num)
            if num1 == 1:
                moeda107() # ex.107
            elif num1 == 2:
                moeda108()
            elif num1 == 3:
                moeda109()
            elif num1 == 4:
                moeda110()
            elif num1 == 5:
                moeda111()   ## mesmo de 112
            elif num1 == 99:
                break
            else:
                print('  Opção invalida, escolha [1,2,3,4,5]')
                print()               
        else:
            print('  Opção invalida, escolha [1,2,3,4,5]')
            print()
    print('-'*40)
    mens.print_end()




main()