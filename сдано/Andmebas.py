from sqlite3 import connect, Error

# Создаём базу данных
def create_connection(path): 
    connection = None
    try:
        connection = connect(path)
        print("OK")
    except Error as e:
        print(f"Error! '{e}'")
    return connection
       
    #----------------------------------------------------------------------------------------------------------------------#

# Подключаем БД по полному пути
conn = create_connection("C:/Users/opilane/source/repos/Nkk15-21/TARgv24_Python/AppData/data.db") 
       
    #----------------------------------------------------------------------------------------------------------------------#

# Создаём функцию для выполнения SQL-запросов
def execute_query(connection, query): 
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"Error '{e}'!")
       
    #----------------------------------------------------------------------------------------------------------------------#

# # Создаём таблицу users (не user!)
# create_users_table = """
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     age INTEGER,
#     gender TEXT,
#     nationality TEXT
# );
# """
# execute_query(conn, create_users_table)
       
    #----------------------------------------------------------------------------------------------------------------------#

# # Вставляем данные в таблицу users
# create_users = """
# INSERT INTO users (name, age, gender, nationality) 
# VALUES
#     ('Mati', 25, 'mees', 'USA'),
#     ('Nikolai', 20, 'mees', 'Russia'),
#     ('Aleksander', 36, 'mees', 'Belarus'),
#     ('Robert', 27, 'mees', 'Slovakia'),
#     ('Aleksander', 25, 'mees', 'Serbia');
# """
# execute_query(conn, create_users)
       
    #----------------------------------------------------------------------------------------------------------------------#

# Функция для выполнения запросов SELECT
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Error '{e}'")
        return None
       
    #----------------------------------------------------------------------------------------------------------------------#

# Получаем список пользователей
select_users  = "SELECT * FROM users"
users = execute_read_query(conn, select_users)

if users:
    for user in users:
        print(user)
else:
    print("No users found.")
       
    #----------------------------------------------------------------------------------------------------------------------#

def add_users_query(connection, user_data):
    query="INSERT INTO users(name, age, gender, nationality) VALUES("+user_data+")"
    execute_query(connection, query)

    #----------------------------------------------------------------------------------------------------------------------#

insert_user="'" + input("Nimi: ") + "','" + input("Vanus: ") + "','" + input("Sugu: ") + "','" + input("Riik: ") + "'"
add_users_query(conn, insert_user)

    #----------------------------------------------------------------------------------------------------------------------#

creaet_users_table2 = """
CREATE TABLE IF NOT EXISTS users (

id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
lname TEXT NOT NULL,
age INTEGER NOT NULL,
GenderId TEXT,
FOREIGN KEY (GenderId)

);
"""

insert_user2 = """
INSERT INTO
users2(Name,Lname,Age,GenderId)

VALUES
('Mati', Tamm, 25, 'mees'),
('Nikolai', 'Baskov'20, 'mees'),
('Aleksander', 'Lukašenko' 36, 'mees'),
('Robert', 'Fitso',  27, 'mees'),
"""

select_users = "SELECT + from users2"
select_users_gender = """
SELECT
users.NAME,
users.Lname,
gender.Nimetus,
from users2
INNER JOIN gender ON users2.GenderId = gender.Id
"""

filename=path.abspath(__file__)