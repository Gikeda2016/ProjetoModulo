from util import calculo as calc
def resumo(preco, aumento, reducao):
    ''' apresenta de resumo '''
    print('-'*40)
    print('{0:^40}'.format('RESUMO DO VALOR'))
    print('-'*40)
    print(' {0:22} {1}'.format(' Preço analisado:', calc.fmoeda(preco)))
    print(' {0:22} {1}'.format(' Dobro do preço:', calc.dobro(preco, True)))
    print(' {0:22} {1}'.format(' Metade do preço:', calc.metade(preco, True)))
    print('{0:<5} {1:15} {2}'.format(calc.fnumero(aumento), '% de aumento:', calc.aumentar(preco, aumento, True)))
    print('{0:<5} {1:15} {2}'.format(calc.fnumero(reducao), '% de redução:', calc.diminuir(preco, reducao, True)))
    print(f'-'*40)