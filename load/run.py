# import psycopg2
import psycopg2
'''

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

'''
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



# db 서버 연결 및 커서 생성
def connect_db():
    try:
        db = psycopg2.connect(host='localhost', dbname='de_test',user='postgres',password='1234',port=5432)
        return db
    except Exception as e:
        print(e)
        print("DB 연결 실패")
        return None

# 커서 및 db 종료
def close_db(db):
    if db:
        db.close()

# insert
def insert(db, first_name, last_name, score):
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO person (first_name, last_name, score) VALUES (%s, %s, %s) RETURNING id;",
        (first_name, last_name, score)
    )
    inserted_id = cursor.fetchone()[0]

    print(f"삽입 ID: {inserted_id}")
    return inserted_id

# select
def select(db, person_id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM person WHERE id = %s;", (person_id,))
    row = cursor.fetchone()
    print(f"검색: {row}")
    return row


def select_n(db, n):
    cursor = db.cursor()
    #cursor.execute("SELECT * FROM person;")
    #cursor.execute("SELECT first_name, last_name, score FROM person;")
    cursor.execute("SELECT first_name, last_name, score FROM person ORDER BY id DESC LIMIT %s;", (n,))
    rows = cursor.fetchall()
    print((f"리스트로 변환중 -----# tuple_to_list = [list(row) for row in rows]"))
    tuple_to_list = []
    for row in rows:
        tuple_to_list.append(list(row))
    print(f"Selected 최근 3개 데이터: {rows}")
    return tuple_to_list


def load_data():
    db = connect_db()
    if not db:
        print("Load_data 실패-db 연결x")
        return None

    try:
        # 데이터 삽입
        insert(db, 'lionel', 'messi', 97)
        insert(db, 'jisung', 'park', 99)
        insert(db, 'heungmin', 'son', 102)
        db.commit()

        all_data = select_n(db, 3) #최근 3개 데이터 조회
        return all_data
    except Exception as e:
        print(f"오류 : , {e}")
        return None
    finally:
        close_db(db)