from util import calculo as calc

def resumo(preco, aumento, reducao):
    ''' apresenta  resumo
        : preco - valor do produto
        : aumento - % de aumento do produto
        : redução - % de redução do produto
        usa funçoes:
        :fmoeda - converte em formato "R$ 100,00"
        :dobro, metade, aumentar e diminuir - calculos matemáticos
        :   True - indica que retorna valor em formato "R$ 100,00"
        :   False - simplesmente número "100,00"
        :fnumero - converte no formato "100,00" por default,
        :   True - retorna no formato "R$100,00"
        :\t - formatação tipo tabulação
    '''
    print('-'*40)
    print('{0:^40}'.format('RESUMO DO VALOR'))
    print('-'*40)
    print(' {0} \t{1}'.format(' Preço analisado:', calc.fmoeda(preco)))
    print(' {0} \t{1}'.format(' Dobro do preço:', calc.dobro(preco, True)))
    print(' {0} \t{1}'.format(' Metade do preço:', calc.metade(preco, True)))
    print(' {0}% de aumento: \t{1}'.format(calc.fnumero(aumento), calc.aumentar(preco, aumento, True)))
    print(' {0}% de redução: \t{1}'.format(calc.fnumero(reducao), calc.diminuir(preco, reducao, True)))
    print(f'-'*40)
