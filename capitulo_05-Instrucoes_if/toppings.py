#! /usr/bin/env python3

"""
NOME
    toppings.py - Verificando a diferença

SINOPSES
    chmod +x toppings.py
    ./toppings.py
    Hold the anchovies!
    True
    False

DESCRIÇÃO
    Compara o valor de requested_topping com o valor 'anchovies'. Se esses
    dois valores não forem iguais, Python devolverá True e executará o
    código após a instrução if. Se esses dois valores forem iguais, Python
    devolverá  False e não executará o código após essa instrução.

    A palavra reservada in diz a Python para verificar a existência de
    'mushrooms' e de 'pepperoni' na lista requested_toppings.

    - Testando várias condições
    Começamos com uma lista contendo os ingredientes solicitados. A
    instrução if verifica se a pessoa pediu cogumelos ('mushrooms') em sua
    pizza. Em caso afirmativo, uma mensagem será exibida para confirmar esse
    ingrediente. O teste para pepperoni corresponde a outra instrução if
    simples, e não a uma instrução elif ou else, portanto esse teste é executado
    independentemente de o teste anterior ter passado ou não. 
    O código verifica se queijo extra ('extra cheese') foi pedido, não
    importando o resultado dos dois primeiros testes. Esses três testes 
    independentes são realizados sempre que o programa é executado.
----------------------------------------------------------------------

HISTÓRICO
    20202110: João Paulo, outubro de 2020.
        - Implementação da função para determinar se dois valores não são
        iguais;
        - Verificando se um valor está em uma lista;
        - Testando várias condições - Pag. 121;

"""


requested_topping = ['mushrooms']

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

requested_toppings = ['mushrooms', 'onions', 'pineapple','extra cheese']

print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

if 'mushrooms' in requested_toppings: print("\n- Adding mushrooms.")
if 'pepperoni' in requested_toppings: print("\n- Adding pepperoni.")
if 'extra cheese' in requested_toppings: print("\n- Adding extra cheese")

print("\nFinished making your pizza!")