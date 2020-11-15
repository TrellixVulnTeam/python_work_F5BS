#! /usr/bin/env python3

"""
NOME
    electric_car.py - Método __init__() de uma classe-filha.

SINOPSES
    chmod +x electric_car.py
    ./electric_car.py
    2016 Tesla Model S
    This car has a 70-kWh battery.
    This car doesn't need a gas tank!

    1990 Lamborghini Lm002
    Tank capacity is 290 L.

DESCRIÇÃO
    Começamos com Car. Quando criamos uma classe-filha, a classe-pai
    deve fazer parte do arquivo atual e deve aparecer antes da
    classe-filha no arquivo. Definimos a classe-filha, que é
    ElectricCar. O nome da classe-pai deve ser incluído entre
    parênteses na definição da classe-filha. O método __init__() aceita
    as informações necessárias para criar uma instância de Car.
    A função super() é uma função especial que ajuda Python a criar
    conexões entre a classe-pai e a classe-filha. Essa linha diz a
    Python para chamar o método __init__() da classe-pai de ElectricCar,
    que confere todos os atributos da classe-pai a ElectricCar. O nome
    super é derivado de uma convenção segundo a qual a classe-pai se
    chama superclasse e a classe-filha é a subclasse.
    Testamos se a herança está funcionando de forma apropriada tentando
    criar um carro elétrico com o mesmo tipo de informação que
    fornecemos quando criamos um carro comum. Criamos uma instância da
    classe ElectricCar e a armazenamos em my_tesla. Essa linha chama o
    método __init__() definido em ElectricCar que, por sua vez, diz a
    Python para chamar o método __init__() definido na classe-pai Car.
    Fornecemos os argumentos 'tesla', 'model s' e 2016.
    Além de __init__() não há outros atributos nem métodos que sejam
    particulares a um carro elétrico. A essa altura, estamos apenas
    garantindo que o carro elétrico tenha o comportamento apropriado de
    Car: 2016 Tesla Model S
    A instância de ElectricCar funciona exatamente como uma instância de
    Car, portanto podemos agora começar a definir atributos e métodos
    específicos aos carros elétricos.

    - Definindo atributos e métodos da classe-filha:

    Adicionamos um novo atributo self.battery_size e definimos seu valor
    inicial, por exemplo, com 70. Esse atributo será associado a todas
    as instâncias criadas a partir da classe ElectricCar, mas não será
    associado a nenhuma instância de Car. Também adicionamos um método
    chamado describe_battery(), que exibe informações sobre a bateria.
    Quando chamamos esse método, temos uma descrição que é claramente
    específica de um carro elétrico.

    Um atributo ou método que possa pertencer a qualquer carro, isto é,
    que não seja específico de um carro elétrico, deve ser adicionado à
    classe Car , em vez de ser colocado na classe ElectricCar.
    Então qualquer pessoa que usar a classe Car terá essa funcionalidade
    disponível também, e a classe ElectricCar conterá apenas códigos
    para as informações e comportamentos específicos de veículos
    elétricos.

HISTÓRICO
    20201411: João Paulo, novembro de 2020.
        - Método __init__() de uma classe-filha (pg 211-212).
        - Definindo atributos e métodos da classe-filha (pg 212-213).

    20201511: João Paulo, novembro de 2020.
        - Sobrescrevendo métodos da classe-pai (pg 214).

"""


class Car():
    """Uma tentativa simples de representar um carro."""

    def __init__(self, make, model, year):
        """Inicializa os atributos que descrevem um carro."""
        self.make = make
        self.model = model
        self.year = year

        self.odometer_reading = 0


    def get_descriptive_name(self):
        """Devolve um nome descritivo, formatado de modo elegante."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model

        return long_name.title()


    def read_odometer(self):
        """Exibe uma frase que mostra a milhagem do carro."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")


    # Modificando o valor de um atributo com um método:
    def update_odometer(self, mileage):
        """Define o valor de leitura do hodômetro com o valor
        especificado. Rejeita a alteração se for tentativa de definir
        um valor menor para o hodômetro."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


    # Incrementando o valor de um atributo com um método
    def increment_odometer(self, miles):
        """Soma a quantidade especificada ao valor de leitura do
        hodômetro."""
        self.odometer_reading += miles


    def fill_gas_tank(self):
        print("Tank capacity is 290 L.")


class ElectricCar(Car):
    """Representa aspectos específicos de veículos elétricos.
    """
    def __init__(self, make, model, year):
        """Inicializa os atributos da classe-pai. Em seguida, inicializa
        os atributos específicos de um carro elétrico.
        """
        super().__init__(make, model, year)
        self.battery_size = 70


    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria.
        """
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


    def fill_gas_tank(self):
        """Carros elétricos não têm tanques de gasolina.
        """
        print("This car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()

print()

my_car = Car('lamborghini', 'LM002', 1990)
print(my_car.get_descriptive_name())
my_car.fill_gas_tank()
