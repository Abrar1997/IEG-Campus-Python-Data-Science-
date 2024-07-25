import mysql.connector as mysql

from os.path import exists

def keyboardInput(datatype, caption, errorMessage, default = None):
    value = None
    isInvalid = True
    while (isInvalid):
        try:
            if default == None:
                value = datatype(input(caption))
            else:
                value = input(caption)
                if (value.strip() == ""):
                    value = default
                else:
                    value = datatype(value)
        except:
            print(errorMessage)
        else:
            isInvalid = False
    return value

def doMenu(conn):
    choice = -1
    while choice != 0:
        print("-----------------")
        print("0  -  Exit       |")
        print("1  -  List       |")
        print("2  -  Add        |")
        print("3  -  Edit       |")
        print("4  -  Delete     |")
        print("-----------------")
        choice = keyboardInput(int, "Choice(0,1,2,3,4): ", "Choice must be Integer")
        if (choice == 0):
            print("Thnx")
        elif (choice == 1):
            printProduct(conn)
        elif (choice == 2):
            addProduct(conn)
        elif (choice == 3):
            editProduct(conn)
        elif (choice == 4):
            deleteProduct(conn)
        
        

filename = "fruits.txt"

# if not exists(filename):
#     open(filename, "xt")

def dbConnect():
    conn = mysql.connect(host="localhost", user="root", password="", database="peneraju")
    return conn


def addProduct(conn):
    try:
        product = keyboardInput(str, "Product: ", "Product must be string")
        desc = keyboardInput(str, "Description: ", "Description must be string")
        quantity = keyboardInput(int, "Quantity: ", "Quantity must be interger")
        price = keyboardInput(float, "Price: ", "Price must be float")

        sql = f"INSERT INTO products (name, description, quantity, price) VALUES ('{product}', '{desc}', {quantity}, {price})"
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit() # to permanently affect the table
    except Exception as e:
        print("Something went wrong when we append the product:", e)

def printProduct(conn):
    sql = f"SELECT id, name, description, quantity, price FROM products"
    cursor = conn.cursor()
    cursor.execute(sql)
    print(f"{'Id':6s}|{'Name':20s}|{'Description':40s}|{'Quantity':20s}|{'Price':20s}")
    print('=' * 110)
    for id, name, description, quantity, price in cursor:
        print(f"{id:<6d}|{name:20s}|{description:40s}|{quantity:20d}|{price:20.2f}")
    else:
        print('=' * 110)


def editProduct(conn):
    try:
        id = keyboardInput(int, "Plese enter the Product Id: ","Index must be Integer")
        sql = f"SELECT id, name, description, quantity, price FROM products WHERE id = {id}"
        cursor = conn.cursor()
        cursor.execute(sql)
        id, name, description, quantity, price = cursor.fetchone()
    except:
        print("Product of this ID does not exist")
    else:
        print(f"Product: {name}\nDescription: {description}\nQuantity: {quantity}\nPrice: {price}")
        confirm = keyboardInput(str, "Are you sure? (y/n): ", "Incorrect response")
        if (confirm == "y"):
            newproduct = keyboardInput(str, f"Product[{name}]: ", "Product must be string", name)
            newdesc = keyboardInput(int, f"Description[{description}]: ", "Description must be interger", description)
            newquantity = keyboardInput(int, f"Quantity[{quantity}]: ", "Quantity must be interger", quantity)
            newprice = keyboardInput(float, f"Price[{price}]: ", "Price must be float", price)
            sql = f"UPDATE products SET name='{newproduct}', description='{newdesc}', quantity={newquantity}, price={newprice} WHERE id = {id}"
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()

def deleteProduct(conn):
    try:
        id = keyboardInput(int, "Plese enter the Product Id: ","Index must be Integer")
        sql = f"SELECT id, name, description, quantity, price FROM products WHERE id = {id}"
        cursor = conn.cursor()
        cursor.execute(sql)
        id, name, description, quantity, price = cursor.fetchone()
    except:
        print("Product of this ID does not exist")
    else:
        print(f"Product: {name}\nDescription: {description}\nQuantity: {quantity}\nPrice: {price}")
        confirm = keyboardInput(str, "Are you sure? (y/n): ", "Incorrect response")
        if (confirm == "y"):
            sql = f"DELETE FROM products WHERE id = {id}"
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()


conn = dbConnect()
doMenu(conn)

# addProduct(filename)
# printProduct(filename)