# Gerador de risadas

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Gerador de risadas é um script em python que cria risos textuais de determinados tamanhos baseados em padrões de escrita (o qual pode ser modificado para se parecer com os seus).

Alguns exemplos:

  - djskdkskskdkskfl
  - slaldldjfl
  - akdjajajakdka
  - lskaj
  - flfjfkalfjdlajdkskakflflflfkdlflakdjakdkslsjskdjal
 
### Tecnologias

Gerador de risadas usa as seguintes tecnologias:

* [Python] - Linguagem de programação 

### Instalação

Gerador de risadas requer Python 3.

```sh
$ git clone https://github.com/Maicon-Moreira/gerador-de-risadas
```

### Uso

Para executar o script utilize o terminal:

Linux:
```sh
$ ./risada.py
```

Windows (requer Python3 no PATH do sistema):
```sh
$ python3 risada.py
```

### Modificação de padrões de risada

Para modificar a lógica de criação de um riso modifique a váriavel "chances" no arquivo risada.py

```py
chances = {
    'a': ['j', 'k', 'l'],
    's': ['j', 'k', 'l'],
    'd': ['j', 'k', 'l'],
    'f': ['j', 'k', 'l'],
    'j': ['a', 's', 'd', 'f'],
    'k': ['a', 's', 'd', 'f'],
    'l': ['a', 's', 'd', 'f']
}
```

no qual a chave representa a letra atual, e os valores dentro da lista correspondem a próxima letra escolhida aleatoriamente.


**MIT**
**Free Software, Hell Yeah!**

   [Python]: <https://www.python.org/>
