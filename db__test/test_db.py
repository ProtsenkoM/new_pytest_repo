import random


def test_get_all_books(books_repo):
    db = books_repo
    all_books = db.get_all()
    assert all_books, 'DB is empty'


def test_add_book(fake_book, books_repo):
    db = books_repo
    count = db.get_count_rows()
    db.insert_one(**fake_book)
    all_book = db.get_all()
    assert len(all_book) == len(count) + 1, 'Row was not added'


def test_get_by_id(fake, books_repo):
    db = books_repo
    count = db.get_count_rows()
    book_by_id = db.get_one_by_id(book_id=random.choice(count))
    assert book_by_id, 'Row is empty'


def test_update_by_id(fake, books_repo):
    db = books_repo
    count = db.get_count_rows()
    test_book_id = random.choice(count)
    update_book_id = db.update_by_id(name=fake.word(),
                                     author=fake.name(),
                                     category=fake.word(),
                                     publication_year=fake.random_int(min=1900, max=2023),
                                     price=fake.random_number(2),
                                     availability=fake.random_element(elements=('В наявності', 'Немає в наявності')),
                                     book_id=test_book_id)
    assert db.get_one_by_id(test_book_id) == update_book_id, 'Rows was not updated'


def test_delete_by_id(books_repo, fake):
    db = books_repo
    count = db.get_count_rows()
    del_by_id = db.delete_by_id(book_id=random.choice(count))
    assert len(del_by_id) == len(count) - 1, 'Row was not deleted'


def test_get_by_fake_id(fake, books_repo):
    db = books_repo
    book_by_id = db.get_one_by_id(book_id=random.randint(100, 200))
    assert book_by_id is None, 'select returned is not None list'


def test_del_by_fake_id(books_repo, fake):
    db = books_repo
    count = db.get_count_rows()
    del_by_id = db.delete_by_id(book_id=random.randint(100,200))
    assert count == del_by_id, 'The are no rows were deleted'
