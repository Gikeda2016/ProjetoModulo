
from time import sleep
from colorama import init
init()

default_ = '\33[m'      # cor padrão
green_ = '\33[0;32m'    # letra verde
green_bold = '\33[1;32m'    # letra verde, bold
red_ = '\33[0;31m'      #  letra vermelha
red_bold = '\33[1;31m'  #  letra vermelha, bold
yellow_ = '\33[0;33m'   #  letra amarela
yellow_bold = '\33[1;33m'  #  letra amarela, bold
blue_ = '\33[0;34m'     #  letra amarela
inversion_ = '\33[7;37;40m'  # padrão reverso -  fundo branco, letra preta
title_ = '\33[1;33m'    # padrão reverso -  fundo branco, letra preta, bold


def print_title(titulo, tipo='-', cor=title_):
    ''' imprime titulo centrado
        titulo: texto a ser impresso
        tipo: linha de separação do título
        cor: cor da letra do título
    '''
    tam = len(titulo)+12
    print(f'{tipo}'*tam)
    typewriter(f'{titulo:^{tam}}', cor=cor )
    print(f'{tipo}'*tam)
    print()


def typewriter(palavra, tempo=0.1, cor=default_):
    ''' O programa digita letra por letra com delay
    '''
    print(f'{cor}', end='')
    for letra in palavra:
        print(letra, end='')
        sleep(tempo)
        if letra in ',:"=!.':
            sleep(0.5)
    print(f'{default_}')


def efim():
    print()
    if str(input(' Quer continuar? [S/N]: ')).upper()[0] in 'N':
        return True
    else:
        return False


def print_end():
    print()
    typewriter(f'  .... {green_}Mais uma conquista, siga em frente !!{default_}  .....', 0.001)
    print()

def leianumero(mens):
    ''' Consiste entrada númerica'''
    while True:
        try:
            valor = str(input(mens))
            flvalor = float(valor)
        except ValueError:
            if valor.replace(',','').isdecimal():  ## retira virgula e verifica se é numero
                valor = valor.replace(',','.')  ## corrige o problema de vírgula por ponto
                break
            else:
                print(f' {red_bold} Por favor digite um valor válido!!{default_}')
            print()
            continue
        break

    return float(valor)
