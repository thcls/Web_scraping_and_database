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
        mycursor.execute("INSERT INTO Products (name, price) VALUES (%s,%f)",(product.name, product.price))
        db.commit()
    except Exception as error:
        print("Error: ",end='')
        print(error)
    finally:
        mycursor.close()
        db.close()
    
def insert_departament(departament):
    db = connect()
    mycursor = db.cursor()
    
    try:
        mycursor.execute("INSERT INTO Departaments (name) VALUES (%s)",(departament.name))
        db.commit()
    except Exception as error:
        print("Error: {}.".format(error))
    finally:
        mycursor.close()
        db.close()

def select_product():
    db = connect()
    mycursor = db.cursor()
    
    try:
        mycursor.execute("SELECT name FROM Products")
        products = mycursor.fetchall()
    except Exception as error:
        print("Error: {}.".format(error))
        
    return products
    
def select_departament():
    db = connect()
    mycursor = db.cursor()
    
    try:
        mycursor.execute("SELECT name FROM Departaments")
        departaments = mycursor.fetchall()
    except Exception as error:
        print("Error: {}.".format(error))
    
    return departaments