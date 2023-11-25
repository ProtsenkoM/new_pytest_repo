from utilities.sqlite_cm import Sqlite
from constants import ROOT_PATH

if __name__ == '__main__':
    with Sqlite(f'{ROOT_PATH}/db/book_shop.db') as c:
        query_create = '''
        CREATE TABLE BOOKS 
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        author TEXT,
        category TEXT,
        publication_year INTEGER,
        price REAL,
        availability TEXT);
        '''
        c.execute(query_create)
        query_insert = '''
        INSERT INTO Books (name, author, category, publication_year, price, availability)
        VALUES
        ('Книга 1', 'Автор 1', 'Фантастика', 2005, 25.99, 'В наявності'),
        ('Книга 2', 'Автор 2', 'Історія', 2010, 19.99, 'Немає в наявності');
        '''
        c.execute(query_insert)
        res = c.execute("select * from BOOKS")
        print(res.fetchall())
