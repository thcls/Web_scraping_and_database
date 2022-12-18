class Product():
    def __init__(self, departament, price, name):
        self.departament = departament
        self.name = name
        self.price = price
        
    def show(self):
        print('Departament: {} | Name: {} | Price = R${}.'.format(self.departament.name, self.name, self.price))
    
class Department():
    def __init__(self, name, link):
        self.name = name
        self.link = link
    
    def show(self):
        print('Departament: {}.'.format(self.name))