

class Restaurantes:
    restaurantes = [];
    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        Restaurantes.restaurantes.append(self)

    def __str__(self):
        return(f'{self.nome} | {self.categoria} | {self.ativo}')
    @property
    def ativo(self):
        return('⊠') if self._ativo == True else '☐'

    @classmethod
    def listar(cls):
        print(f'{"Nome do restaurante"} | {"categoria"} | {"status"}')
        for restauranted in cls.restaurantes:
            print(f'{restauranted.nome.ljust(20)} | {restauranted.categoria.ljust(20)} | {restauranted.ativo}')

restPraca = Restaurantes('Praça','praça')
restpizza = Restaurantes('pizza', 'pizza')


print(Restaurantes.listar())