#! /usr/bin/env python3

"""
NOME
    privilegios.py - FAÇA VOÇE MESMO.

SINOPSES
    from nome_do_módulo import nome_da_classe, nome_da_classe, ...

DESCRIÇÃO
    9.8 – Privilégios: Escreva uma classe Privileges separada. A classe
    deve ter um atributo privileges que armazene uma lista de strings
    conforme descrita no Exercício 9.7. Transfira o método
    show_privileges() para essa classe. Crie uma instância de Privileges
    como um atributo da classe Admin. Crie uma nova instância de Admin e
    use seu método para exibir os privilégios.


    9.11 - Importando Admin: Comece com seu programa do Exercício 9.8
    (página 241). Armazene as classes User, Privileges e Admin em um
    módulo. Crie um arquivo separado e uma instância de Admin e chame
    show_privileges() para mostrar que tudo está funcionando de forma
    apropriada.


HISTÓRICO
    20201611: João Paulo, novembro de 2020.
        - 9.8 – Privilégios (pg 217).

    20201711: João Paulo, novembro de 2020.
        - 9.11 – Importando Admin (pg 224).

"""


class User():
    """Um modelo simples de um perfil de usuário.
    """
    def __init__(self, first_name, last_name, username, email):
        """Inicializa os atrinutos dos usuários.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.login_attempts = 0


    def describe_user(self):
        """Resumo das informações do usuário.
        """
        print("\nNome completo: " + self.first_name.title() + " " +
              self.last_name.title())
        print("Username: " + self.username.lower())
        print("e-mail: " + self.email.lower())


    def greet_user(self):
        """Mostra uma saudação personalizada para o usuário.
        """
        print("Olá, " + self.first_name.title() + ", obrigado por se cadastrar.")


    def increment_login_attempts(self):
        """Incrementa o valor de login_attempts em 1.
        """
        self.login_attempts += 1


    def reset_login_attempts(self):
        """Reinicia o valor de login_attempts com 0.
        """
        self.login_attempts = 0


class Privileges():
    """Modelo simplificado de privilégios do usuário.
    """
    def __init__(self, privileges=[]):
        """Inicializa os atributos dos privilégios dos usuários.
        """
        self.privileges = ['can add post', 'can delete post', 'can ban user']


    def show_privileges(self):
        """Lista o conjunto de privilégios de um administrador.
        """
        print("\nLista de privilégios de administrador: ")
        for self_privilege in self.privileges:
            print("- " + self_privilege)


class Admin(User):
    """Modelo simplificado do usuário Admin.
        """
    def __init__(self, first_name, last_name, username, email):
        """Inicializa os atributos do usuário Admin.
        """
        super().__init__(first_name, last_name, username, email)
        self.privileges = Privileges()
