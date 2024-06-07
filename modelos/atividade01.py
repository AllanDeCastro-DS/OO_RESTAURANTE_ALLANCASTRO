# atividade 1

class carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo;
        self.cor = cor;
        self.ano = ano;

Mazda = carro('Miata MX5','vermelho',1995)

#atividade 2
class Restaurantes:
    nome = ''
    categoria = ''
    ativo = False
    periodo = ''
    local = ''

Outback = Restaurantes();

Outback.nome = 'Outback'
Outback.categoria = 'Churrasco'
Outback.periodo = "24 horas"
Outback.local = 'Curitiba'


#atividade 3
class Restaurants:
    def __init__(self, nome, categoria, periodo, local):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.periodo = periodo
        self.local = local

BK = Restaurants('Burguer King','Fast Food','24 horas','Campo Largo')

#atividade 4

class Restaurante:
    def __init__(self, nome, categoria, periodo, local):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.periodo = periodo
        self.local = local
    def __str__(self):
        return(f'O nome do restaurante é {self.nome} \n a categoria é {self.categoria}\n o periodo é {self.periodo}\n e o local é {self.local}\n\n ')

MC = Restaurante('Mc Donnalds','Fast Food','24 horas','Campo Largo')

print(str(MC))

#atividade 5


class Cliente:
    def __init__(self, nome, idade, altura, olhos):
        self.nome = nome;
        self.idade = idade;
        self.altura = altura;
        self.olhos = olhos;
    def __str__(self):
        return(f'Nome: {self.nome}\n idade: {self.idade} \n altura: {self.altura},\n cor dos olhos: {self.olhos} \n')

Clientes = []

Jubileu = Cliente('Jubileu', 97, 1.70, 'Azul')

Marta = Cliente('Marta', 56, 1.60, 'Castanho')

Pedro = Cliente('Pedro', 1, 0.50, 'preto')


Clientes.append(Jubileu)
Clientes.append(Marta)
Clientes.append(Pedro)



for pessoa in Clientes:
    print(str(pessoa))

