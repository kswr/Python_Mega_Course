import psycopg2

conn_string = "dbname='database1' user='postgres' password='admin' host='localhost' port ='5432'"


def create_table():
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def drop_table():
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()
    # cur.execute("DROP TABLE %s", (table,))
    cur.execute("DROP TABLE STORE")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()
    # more SQL injection vulnerable notation
    # cur.execute("INSERT INTO store VALUES ('%s', '%s', '%s')" % (item, quantity, price))
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)",  (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = %s", (item,))
    conn.commit()
    conn.close()


def update(item, quantity, price):
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = %s, price = %s WHERE item = %s", (quantity, price, item))
    conn.commit()
    conn.close()


drop_table()
create_table()
insert('Apple', 10, 5)
insert('Orange', 15, 4)
print(view())
delete('Apple')
print(view())
update('Orange', 20, 4)
print(view())
# print(view())

# insert('Water Glass', 10, 5)
# insert('Coffee Cup', 10, 5)
# insert('Wine Glass', 11, 2)
#
# print(view())
#
# update('Water Glass', 15, 20)
#
# print(view())
#
# delete('Wine Glass')
# delete('Water Glass')
# delete('Coffee Cup')
#
# print(view())
