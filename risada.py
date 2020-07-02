#!/usr/bin/env python3

from random import randint, choice

chances = {
    'a': ['j', 'k', 'l'],
    's': ['j', 'k', 'l'],
    'd': ['j', 'k', 'l'],
    'f': ['j', 'k', 'l'],
    'j': ['a', 's', 'd', 'f'],
    'k': ['a', 's', 'd', 'f'],
    'l': ['a', 's', 'd', 'f']
}

default_interval = [10, 20]

print('-'*70)
print('😀 Bem Vindo ao gerador de risadas culturalmente aceitas no sul do 🇧🇷')
print('-'*70)

while True:
    print('Insira o número de caracteres desejados na risada')
    print(
        f'ou ENTER para gerar uma risada entre {default_interval[0]} e {default_interval[1]} caracteres')
    print(f'ou "0" + ENTER para sair')

    captured = input()

    if captured == '0':
        break

    elif captured == '':
        length = randint(*default_interval)

    else:
        try:
            length = int(captured)
        except:
            print('-'*15)
            print('NÚMERO INVÁLIDO')
            print('-'*15)
            continue

    actual_letter = choice(list(chances.keys()))
    risada = ''

    for i in range(length):
        risada += actual_letter
        actual_letter = choice(chances[actual_letter])

    print('-'*min(length, 100))
    print(f'Risada com {length} caracteres:')
    print(risada)
    print('-'*min(length, 100))
    print('')

print('Volte sempre ✊')
