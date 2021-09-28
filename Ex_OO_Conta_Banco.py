
class Conta:
    def __init__(self, numero, titular, saldo, limite=1000.0):
        print("Criando objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O saldo do {} é de R$ {}".format(self.__titular, self.__saldo))

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self,valor_saque):
        valor_disponivel = self.__saldo + self. __limite
        return valor_saque <= valor_disponivel

    def sacar(self, valor):
        if(self.__pode_sacar()):
            self.__saldo -= valor
        else:
            print("O valor {} ultrapassou o limite.".format(valor))
    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'CAIXA':'104', 'BRADESCO':'237'}
