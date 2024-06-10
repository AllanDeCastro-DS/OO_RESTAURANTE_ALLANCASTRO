# #Questão 1

# class Pessoa:
#     def __init__(self, nome, idade, profissao):
#         self.nome = nome;
#         self.idade = idade;
#         self.profissao = profissao;



#     def prof(self):
#             return(f' Você é um {self.profissao} | \n ')
    
#     def age(self):
#          return(f'Sua idade ano que vem será: {self.idade + 1} |')

#     def __str__(self):
#         return(f'\n Bem vindo/a: {self.nome} |\n Você tem {self.idade} anos! | \n{self.prof()} {self.age()}')
    
    

# pessoa1 = Pessoa('Antonio', 25, 'Mecanico')

# print(str(pessoa1))


# #Questão 2 3 4 5 6


class contabancaria:
    def __init__(self, saldo, titular):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False

    
    def ativarconta(self):
        if self.ativo == False: self.ativo = True 

    def retativo(self):
        if (self.ativo == True):
            return('Ativa!')
        else:
            return('Desativada')

    def __str__(self):
        return(f'O titular é {self.titular} \n O Saldo é de {self.saldo}\n Sua conta está {self.retativo()}\n\n')


Conta1 = contabancaria(30, 'Antonio')
Conta2 = contabancaria(120023, 'Jorge')

ativard = classmethod(contabancaria.ativarconta)


print(str(Conta2))

print(str(Conta1))
print(str(f'O titular é {Conta1.titular}'))



#Atividade 7 8



class ContaBanco:
    CONTAS = []
    def __init__(self, nome, idade, estado, saldo, status):
        self.nome = nome
        self.idade = idade
        self.estado = estado
        self.saldo = saldo
        self.status = status
        ContaBanco.CONTAS.append(self)
    
    @classmethod
    def printar(cls):
        for i in cls.CONTAS:
            print(f'\n\n{cls.nome} {cls.idade} {cls.estado} {cls.saldo} {cls.status} \n\n')
    

contab1 = ContaBanco('Jose', 17, 'PR', 0.2, 'SOLTEIRO')
contab2 = ContaBanco('Allan', 17, 'PR', 1203120321, 'SOLTEIRO')
contab3 = ContaBanco('Otavio', 16, 'PR', '3 pila', 'SOLTEIRO')



print(ContaBanco.printar())