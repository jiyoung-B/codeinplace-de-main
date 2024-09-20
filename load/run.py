# import psycopg2
import psycopg2

# install psycop2, uncomment the first line and implement your code below
db = psycopg2.connect(host='localhost', dbname='de_test',user='postgres',password='1234',port=5432)

cursor= db.cursor()

# insert one sample row using psycopg2
cursor.execute(
    "INSERT INTO person (first_name, last_name, score) VALUES (%s, %s, %s) RETURNING id;",
    ('jisung', 'park', 99)
)
inserted_id = cursor.fetchone()[0]  #
print(f"Inserted row with ID: {inserted_id}")
db.commit()

# select inserted row using psycopg2
cursor.execute("SELECT * FROM person WHERE id = %s;", (inserted_id,))
row = cursor.fetchone()
print(f"Selected Row: {row}")

# Close the connection
cursor.close()
db.close()


# '''
# create a database called de_test in postgresql # postresql 에서 진행
# create a table defined in table.sql # postresql 에서 진행
'''
    <table.sql>
    CREATE TABLE person (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(128),
        last_name VARCHAR(128),
        score INTEGER);
'''
#
# connect to the database using psycopg2 package
# insert one sample row using psycopg2
# select inserted row using psycopg2
# run command: python3 run.py
# '''
