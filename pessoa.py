from br_nome_gen import pessoa_random
import random
import randomtime

class Pessoa():
    def __init__(self):
        self.nome = ''
        self.cpf = ''
        self.datanasc = ''
        
    def gerar(self):
        self.nome = pessoa_random().nome
        self.cpf  = self.gcpf()
        self.datanasc = randomtime.random_date("1970/1/1", "2004/1/1", random.random())
        
    def show(self):
        print('Nome: {}, CPF: {}, Data de nascimento: {}.'.format(self.nome, self.cpf, self.datanasc))
        
    def gcpf(self):
        def calcula_digito(digs):
            s = 0
            qtd = len(digs)
            for i in range(qtd):
                s += n[i] * (1+qtd-i)
            res = 11 - s % 11
            if res >= 10: return 0
            return res                                                                              
        n = [random.randrange(10) for i in range(9)]
        n.append(calcula_digito(n))
        n.append(calcula_digito(n))
        return "%d%d%d.%d%d%d.%d%d%d-%d%d" % tuple(n)
    
class Produto():
    
    def __init__(self, departamento, preco, nome):
        self.departamento = departamento
        self.preco = preco
        self.nome = nome
        self.quant = random.randint(0,200)
        
    def show(self):
        print('{}|Nome: {}, Preço = {}, Quantidade = {}.'.format(self.departamento.nome, self.nome, self.preco, self.quant))
    
class Departamento():
    def __init__(self, nome, link) -> None:
        self.nome = nome
        self.link = link
    
    def show(self):
        print(self.nome)