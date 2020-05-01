import sqlite3

def connect():
    conn=sqlite3.connect("vehicle.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,customer_name text,vehicle_model text,chassis_no INTEGER,reg_no INTEGER)")
    conn.commit()
    conn.close()

connect()

def insert(customer_name,vehicle_model,chassis_no,reg_no):
    conn=sqlite3.connect("vehicle.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(customer_name,vehicle_model,chassis_no,reg_no))
    conn.commit()
    conn.close()

#insert("5225","Maahi",2024,8919473460)


def view():
    conn=sqlite3.connect("vehicle.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(customer_name=" ",vehicle_model=" ",chassis_no=" ",reg_no=" "):
    conn=sqlite3.connect("vehicle.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE customer_name=? OR vehicle_model=? OR chassis_no=? OR reg_no=?",(customer_name,vehicle_model,chassis_no,reg_no))
    rows=cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn=sqlite3.connect("vehicle.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()
#delete(3)

def update(id,customer_name,vehicle_model,chassis_no,reg_no):
    conn=sqlite3.connect("vehicle.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET customer_name=?,vehicle_model=?,chassis_no=?,reg_no=? WHERE id=?",(customer_name,vehicle_model,chassis_no,reg_no,id))
    conn.commit()
    conn.close()
    
    












