from pydantic import BaseModel
from typing import List, Generator, Iterator, Dict, Any
from abc import ABC, abstractmethod
import logging
import json
from functools import wraps

DATA_FILE_PATH = 'data.json'

logging.basicConfig(
    filename='library_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class BookModel(BaseModel):
    title: str
    author: str
    year: int

class Publication(ABC):
    @abstractmethod
    def get_info(self) -> str:
        pass
    
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        pass

class Book(Publication):
    def __init__(self, model: BookModel):
        self._model = model

    def get_info(self) -> str:
        return f"Book: '{self._model.title}', by {self._model.author}, {self._model.year}"

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': 'book',
            'title': self._model.title,
            'author': self._model.author,
            'year': self._model.year
        }

class Journal(Book):
    def __init__(self, model: BookModel, issue: int):
        super().__init__(model)
        self._issue = issue

    def get_info(self) -> str:
        return f"Journal: '{self._model.title}', by {self._model.author}, {self._model.year}, Issue #{self._issue}"

    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data['type'] = 'journal'
        data['issue'] = self._issue
        return data

def log_add(func):
    @wraps(func)
    def wrapper(self, pub: Publication):
        result = func(self, pub)
        logging.info(f"Added: {pub.get_info()}")
        return result
    return wrapper

def check_remove(func):
    @wraps(func)
    def wrapper(self, pub: Publication):
        if pub not in self._items:
            print(f"Warning: {pub.get_info()} is not in library!")
            return False
        return func(self, pub)
    return wrapper

class FileManager:
    def __init__(self, filename: str, mode: str):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False

    def save(self, data: List[Publication]):
        items = [pub.to_dict() for pub in data]
        json.dump(items, self.file, ensure_ascii=False, indent=2)

    def load(self) -> List[Publication]:
        items = json.load(self.file)
        result: List[Publication] = []
        for i in items:
            if i.get('type') == 'journal':
                model = BookModel(title=i['title'], author=i['author'], year=i['year'])
                result.append(Journal(model, i.get('issue', 1)))
            else:
                model = BookModel(title=i['title'], author=i['author'], year=i['year'])
                result.append(Book(model))
        return result

class Library:
    def __init__(self):
        self._items: List[Publication] = []

    @log_add
    def add(self, pub: Publication):
        self._items.append(pub)

    @check_remove
    def remove(self, pub: Publication):
        self._items.remove(pub)
        logging.info(f"Removed: {pub.get_info()}")
        return True

    def __iter__(self) -> Iterator[Publication]:
        return iter(self._items)

    def by_author(self, author: str) -> Generator[Publication, None, None]:
        for pub in self._items:
            if pub._model.author == author:
                yield pub

    def save_to_file(self, fname: str):
        with FileManager(fname, 'w') as fm:
            fm.save(self._items)

    def load_from_file(self, fname: str):
        with FileManager(fname, 'r') as fm:
            new = fm.load()
            for pub in new:
                self.add(pub)
# створення бібліотеки
lib = Library()

# створення інстансу книги та журналу
b1 = Book(BookModel(title='Book_1', author='Author_1', year=2020))
b2 = Book(BookModel(title='Book_2', author='Author_2', year=2022))
j1 = Journal(BookModel(title='Book_3', author='Author_3', year=2024), issue=7)

# додавання їх у бібліотеку
lib.add(b1)
lib.add(b2)
lib.add(j1)

# виведення списку книг у бібліотеці
print('Виведення списку книг у бібліотеці:')
for i in lib:
    print('-', i.get_info())

# виведення списку книг бібліотеки по імені автора
print(f"Виведення списку книг бібліотеки по імені автора {b1._model.author}:")
for i in lib.by_author('Author_2'):
    print('-', i.get_info())

# збереження списку книг у файл
lib.save_to_file(DATA_FILE_PATH)
print(f'Збереження списку книг у файл {DATA_FILE_PATH}')

# видалення книги з бібліотеки
if lib.remove(b1):
    print('Видалення книги з бібліотеки:', b1.get_info())

# виведення списку книг після видалення
print('Виведення списку книг після видалення:')
for i in lib:
    print('-', i.get_info())

new_lib = Library()
#додавання книг з файлу в бібліотеку
new_lib.load_from_file(DATA_FILE_PATH)
print(f'Виведення списку книг бібліотеки після додавання у файл {DATA_FILE_PATH}')
for i in new_lib:

    # виведення списку книг бібліотеки після додавання
    print('-', i.get_info())
