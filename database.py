from mysql import connector

def connect():
    return connector.connect(
        host= '',
        user= '',
        passwd= '',
        database= ''
    )
        
def insert_product(product):
    db = connect()
    mycursor = db.cursor()
    try:
        mycursor.execute("INSERT INTO products (name, price) VALUES (%s,%f)",(product.name,product.price))
        db.commit()
    except Exception as error:
        print("Error: ",end='')
        print(error)
    
def insert_departament(departament):
    db = connect()
    
    mycursor = db.cursor()
    
    try:
        mycursor.execute("INSERT INTO departaments (name) VALUES (%s)",(departament.name))
        db.commit()
    except Exception as error:
        print("Error: ",end='')
        print(error)

def select_product():
    db = connect()
    
    mycursor = db.cursor()
    mycursor.execute("SELECT name FROM products")
    product = mycursor.fetchall()
    
    return product
    
def select_departament():
    db = connect()
    
    mycursor = db.cursor()
    mycursor.execute("SELECT name FROM departaments")
    departament = mycursor.fetchall()
    
    return departament