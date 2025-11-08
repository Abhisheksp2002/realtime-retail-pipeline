import psycopg2
from datetime import datetime

db_host= '<your_host>'
db_name= '<database_name>'
db_user= '<user_name>'
db_pass= '<password>'

conn = psycopg2.connect(host= db_host, database= db_name, user= db_user, password= db_pass)
print("connection established")

cursor = conn.cursor()



# create transactions table
create_query= '''CREATE TABLE IF NOT EXISTS transactions(
                transaction_id SERIAL PRIMARY KEY,
                store_id TEXT,
                customer_id TEXT,
                timestamp TIMESTAMP,
                items JSONB,
                total_amount DECIMAL,
                payment_type TEXT)'''

cursor.execute(create_query)
# conn.commit()
print("created successfully")




# insert into transaction table
insert_query = 'INSERT INTO transactions (store_id, customer_id, timestamp, items, total_amount, payment_type) VALUES (%s, %s, %s, %s, %s, %s)'
insert_values= ('S1', 'C1', datetime.now(), '[{"product_id":"P1","qty":2,"price":25}]', 50, 'card')
cursor.execute(insert_query, insert_values)
conn.commit()

print("insert successful")



cursor.execute('SELECT * from transactions')
print(cursor.fetchone())



# cursor.execute('''
#     SELECT table_schema, table_name
#     FROM information_schema.tables
# ''')

# tables= cursor.fetchall()
# for schema, table in tables:
#     print(f"{schema}.{table}")


# cursor.execute("select pg_typeof(items) from transactions limit 1;")
# print(cursor.fetchone())


cursor.close()
conn.close()