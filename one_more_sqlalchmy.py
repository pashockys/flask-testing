from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# импортируем классы Book и Base из файла database_setup.py
from sqlAlchemy_testing import Book, Base

engine = create_engine('sqlite:///books-collection.db')
# Свяжeм engine с метаданными класса Base,
# чтобы декларативы могли получить доступ через экземпляр DBSession
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# Экземпляр DBSession() отвечает за все обращения к базе данных
# и представляет «промежуточную зону» для всех объектов,
# загруженных в объект сессии базы данных.
session = DBSession()

bookOne = Book(title="Чистый Python", author="Дэн Бейде", genre="компьютерная литература")
session.add(bookOne)
session.commit()

editedBook = session.query(Book).filter_by(id=1).one()
editedBook.author = "Дэн Бейдер"
session.add(editedBook)
session.commit()

bookToDelete = session.query(Book).filter_by(title='Чистый Python').one()
session.delete(bookToDelete)
session.commit()
