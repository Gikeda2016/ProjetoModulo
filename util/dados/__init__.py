from util import calculo as calc

def resumo(preco, aumento, reducao):
    ''' apresenta de resumo '''
    print('-'*40)
    print('{0:^40}'.format('RESUMO DO VALOR'))
    print('-'*40)
    print(' {0} \t{1}'.format(' Preço analisado:', calc.fmoeda(preco)))
    print(' {0} \t{1}'.format(' Dobro do preço:', calc.dobro(preco, True)))
    print(' {0} \t{1}'.format(' Metade do preço:', calc.metade(preco, True)))
    print(' {0}% de aumento: \t{1}'.format(calc.fnumero(aumento), calc.aumentar(preco, aumento, True)))
    print(' {0}% de redução: \t{1}'.format(calc.fnumero(reducao), calc.diminuir(preco, reducao, True)))
    print(f'-'*40)