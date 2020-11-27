#! /usr/bin/env python3

"""
NOME
    verificando_usuario.py - FAÇA VOCÊ MESMO.

SINOPSES
    chmod +x verificando_usuario.py
    ./verificando_usuario.py

------------------------------------------------------------------------

DESCRIÇÃO
    10.13 – Verificando se é o usuário correto:
        A última listagem de remember.py supõe que o usuário já forneceu
        seu nome ou que o programa está executando pela primeira vez.
        Devemos modificá-lo para o caso de o usuário atual não ser a
        pessoa que usou o programa pela última vez.
        Antes de exibir uma mensagem de boas-vindas de volta em
        greet_user(), pergunte ao usuário se seu nome está correto. Se
        não estiver, chame get_new_username() para obter o nome correto.

------------------------------------------------------------------------

HISTÓRICO
    20202611: João Paulo, novembro de 2020.
        - 10.13 – Verificando se é o usuário correto (pg 254).

"""



import json


def get_stored_username():
    """Obtém o nome do usuário já armazenado se estiver disponível."""

    filename = 'username.json'

    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)

    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Pede um novo nome de usuário."""
    username = input("- What is your name? ")
    filename = 'username.json'

    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)

    return username


def correct_user():
    """Verifica se é o usuário correto."""
    answers = input("Is your name correct, yes or no?")

    if answers == 'yes':
        return True
    else:
        return False

def greet_user():
    """Saúda o usuário pelo nome."""
    username = get_stored_username() 
    if username:
        print("- Welcome back, " + username.title() + "!")

    else:
        username = get_new_username()

        print("We'll remember you when you come back, " +
    username.title() + "!")


greet_user()
