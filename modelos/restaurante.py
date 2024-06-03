class Restaurante:
    nome=''
    categoria=''
    ativo = False



restaurante_praca = Restaurante()

restaurante_praca.nome = "praca"
restaurante_praca.categoria = "gourmet"




Restaurantes = [restaurante_praca]


print(vars(restaurante_praca))


#Questão 1

restaurante_praca.categoria = 'italiano'

#Questão 2

print(restaurante_praca.nome)

#Questão 3

print(f'O restaurante praca está: {restaurante_praca.ativo}')

if restaurante_praca.ativo == True: 
    print('Restaurante Ativo') 

else: 
    print('Restaurante Inativo')


#Questão 4

categoria = Restaurante.categoria
print(categoria)

#Questão 5

restaurante_praca.nome = "Bistrô"

#Questão 6

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza_place'
restaurante_pizza.categoria = 'Fast Food'


#Questão 7

print(restaurante_pizza.categoria,restaurante_pizza.categoria == 'Fast Food')

#Questão 8

restaurante_pizza.ativo = True

#Questão 9


print(vars(restaurante_praca))