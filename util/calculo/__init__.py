
def fatorial(n):
    ''' Calcula o fatorial de n
        n: fatorial do número n
    '''
    fat = 1
    for i in range(n,0,-1):
        fat *= i
    return fat

def dobro(n, moeda=False):
    return fnumero(n*2, moeda)

def triplo(n, moeda=False):
    return fnumero(n*3, moeda)

def metade(n, moeda=False):
    return fnumero(n/2, moeda)

def aumentar(n, porc, moeda=False):
    ''' aumenta n em porc(%) '''
    return fnumero(n*(1+porc/100), moeda)

def diminuir(n, porc, moeda=False):
    ''' diminui n em porc(%) '''
    return fnumero(n*(1-porc/100), moeda)

def fmoeda(n):
    ''' Converte número no formato R$ 100,00 '''
    return f'R$ {n:>7.2f}'.replace('.',',')

def fnumero(n, moeda=False):
    ''' Converte número no formato 100,00 ou R$ 100,00 '''
    num = f'{n:>7.2f}'.replace('.',',')
    if moeda:
        num = 'R$ ' + num
    return num

def resumo(preco, aumento, reducao):
    ''' apresenta de resumo '''
    print('-'*40)
    print('{0:^40}'.format('RESUMO DO VALOR'))
    print('-'*40)
    print(' {0:22} {1}'.format(' Preço analisado:', fmoeda(preco)))
    print(' {0:22} {1}'.format(' Dobro do preço:', dobro(preco, True)))
    print(' {0:22} {1}'.format(' Metade do preço:', metade(preco, True)))
    print('{0:<5} {1:15} {2}'.format(fnumero(aumento), '% de aumento:', aumentar(preco, aumento, True)))
    print('{0:<5} {1:15} {2}'.format(fnumero(reducao), '% de redução:', diminuir(preco, reducao, True)))
    print(f'-'*40)
