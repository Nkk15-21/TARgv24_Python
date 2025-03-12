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

# Создаём таблицу users (не user!)
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    nationality TEXT
);
"""
execute_query(conn, create_users_table)
       
    #----------------------------------------------------------------------------------------------------------------------#

# Вставляем данные в таблицу users
create_users = """
INSERT INTO users (name, age, gender, nationality) 
VALUES
    ('Mati', 25, 'mees', 'USA'),
    ('Nikolai', 20, 'mees', 'Russia'),
    ('Aleksander', 36, 'mees', 'Belarus'),
    ('Robert', 27, 'mees', 'Slovakia'),
    ('Aleksander', 25, 'mees', 'Serbia');
"""
execute_query(conn, create_users)
       
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
