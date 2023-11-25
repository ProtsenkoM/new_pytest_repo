from db.sqllite_pack._base_db_conector import BaseDBConnector


class BooksRepo:
    def __init__(self, db_params):
        self._db = BaseDBConnector(db_params)
        self._table_name = "BOOKS"

    def get_all(self):
        res = self._db.conn.execute(f"select * from {self._table_name}")
        return res.fetchall()

    def get_count_rows(self):
        res = self._db.conn.execute(f"select id from {self._table_name}")
        return [item for tp1 in res.fetchall() for item in tp1]

    def get_one_by_id(self, book_id: int):
        res = self._db.conn.execute(f"select * from {self._table_name} where id={book_id}")
        return res.fetchone()

    def update_by_id(self, book_id: int, name: str, author: str, category: str, publication_year: int, price: float,
                     availability: str):
        query_update = f'''
            UPDATE {self._table_name} SET
            name = '{name}', author = '{author}', category = '{category}', publication_year = {publication_year},
            price = {price}, availability = '{availability}'
            WHERE
            id = {book_id};
            '''
        self._db.conn.execute(query_update)
        self._db.conn.commit()
        return self.get_one_by_id(book_id)

    def delete_by_id(self, book_id: int):
        res = self._db.conn.execute(f"DELETE from {self._table_name} where id={book_id}")
        res_after = self.get_count_rows()
        self._db.conn.commit()
        return res_after

    def insert_one(self, name: str, author: str, category: str, publication_year: int, price: float, availability: str):
        query_insert = f'''
               INSERT INTO {self._table_name} (name, author, category, publication_year, price, availability)
               VALUES
               ('{name}','{author}', '{category}', {publication_year}, {price}, '{availability}');
               '''
        self._db.conn.execute(query_insert)
        self._db.conn.commit()

    def __del__(self):
        self._db.cursor.close()
        self._db.conn.close()
