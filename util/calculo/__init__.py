
def fatorial(n):
    ''' Calcula o fatorial de n
        n: fatorial do número n
    '''
    fat = 1
    for i in range(n,0,-1):
        fat *= i
    return fat

def dobro(n, moeda=False):
    ''' moeda é opcional - False por default - não imprime 'R$', 
    mas converte para string no formato 100,00. 
    Essa modificação foi feita demais funções para adequar aos exercícios
    Todas funções retornam dados formatados por fnumero()
    '''  
    return fnumero(n*2, moeda)

def triplo(n, moeda=False):
    return fnumero(n*3, moeda)

def metade(n, moeda=False):
    return fnumero(n/2, moeda)

def aumentar(n, porc, moeda=False):
    ''' aumenta n porc(%) '''
    return fnumero(n*(1+porc/100), moeda)

def diminuir(n, porc, moeda=False):
    ''' aumenta n porc(%) 
        :moeda True- devolve no formato R$ 100,00    
    '''
    return fnumero(n*(1-porc/100), moeda)

def fmoeda(n):
    ''' Converte número no formato R$ 100,00 '''
    return f'R$ {n:>7.2f}'.replace('.',',')

def fnumero(n, moeda=False):
    ''' Converte número no formato 100,00 ou R$ 100.00 '''
    num = f'{n:>7.2f}'.replace('.',',')
    return num if not moeda else 'R$ ' + num

