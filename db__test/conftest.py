import pytest

from constants import ROOT_PATH
from db.sqllite_pack.books_repo import BooksRepo


@pytest.fixture(scope='module')
def books_repo(env):
    return BooksRepo(f"{ROOT_PATH}{env.db_param['path']}")


@pytest.fixture()
def fake_book(fake):
    data = {"name": fake.word(),
            "author": fake.name(),
            "category": fake.word(),
            "publication_year": fake.random_int(min=1900, max=2023),
            "price": fake.random_number(2),
            "availability": fake.random_element(elements=('В наявності', 'Немає в наявності'))
            }
    return data
