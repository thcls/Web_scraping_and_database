import mysql.connector

def connect():
    return mysql.connector.connect(
        host= 'mysql04-farm2.uni5.net',
        user= 'bessapontes22',
        passwd= 't13201415',
        database= 'bessapontes22'
    )

def insert_people(db,people):
    db = connect()
    mycursor = db.cursor()
    try:
        mycursor.execute("INSERT INTO usuario (cpf, nome, data_nasc) VALUES (%s,%s,%s)",(people.cpf,people.nome, people.datanasc))
        db.commit()
    except Exception as error:
        print("Error: ",end='')
        print(error)
        
def insert_produto(produto):
    db = connect()
    mycursor = db.cursor()
    try:
        mycursor.execute("INSERT INTO produto (nome, preco, qtd_estoque) VALUES (%s,%f,%s)",(produto.nome,produto.preco, produto.quant))
        db.commit()
    except Exception as error:
        print("Error: ",end='')
        print(error)
    
def insert_departamento(departamento):
    db = connect()
    mycursor = db.cursor()
    try:
        mycursor.execute("INSERT INTO departamentos (nome) VALUES (%s)",(departamento.nome))
        db.commit()
    except Exception as error:
        print("Error: ",end='')
        print(error)
        
def insert_oferta(departamento):
    db = connect()
    mycursor = db.cursor()
    try:
        mycursor.execute("INSERT INTO oferta (id_produto, id_departamento) VALUES (%d, %d)",(departamento.nome))
        db.commit()
    except Exception as error:
        print("Error: ",end='')
        print(error)