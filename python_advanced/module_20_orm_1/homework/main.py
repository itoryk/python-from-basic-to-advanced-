from datetime import date

if __name__ == '__main__':
    from sqlalchemy import Table, MetaData, create_engine, Column, Integer, String, Date, Float, Boolean
    from sqlalchemy.orm import sessionmaker, mapper, declarative_base
    from sqlalchemy.ext.hybrid import hybrid_property

    engine = create_engine("sqlite:///python.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    Base = declarative_base()

    class Books(Base):
        __tablename__ = 'books'

        id = Column(Integer, primary_key=True)
        name = Column(String(16), nullable=False)
        count = Column(Integer, default=1)
        release_date = Column(Date, nullable=False)
        author_id = Column(Integer, nullable=False)

        def __repr__(self):
            return f"{self.id}, {self.name}, {self.count}, {self.release_date}, {self.author_id}"

    class Author(Base):
        __tablename__ = 'authors'

        id = Column(Integer, primary_key=True)
        name = Column(String(16), nullable=False)
        surname = Column(String(16), nullable=False)

        def __repr__(self):
            return f"{self.id}, {self.name}, {self.surname}"

    class Students(Base):
        __tablename__ = 'students'

        id = Column(Integer, primary_key=True)
        name = Column(String(16), nullable=False)
        surname = Column(String(16), nullable=False)
        phone = Column(String, nullable=False)
        email = Column(String(60), nullable=False)
        average_score = Column(Float, nullable=False)
        scholarship = Column(Boolean, nullable=False)

        def __repr__(self):
            return f"{self.id}, {self.name}, {self.surname}, {self.phone}, {self.email}, {self.average_score}, {self.scholarship}"

        @classmethod
        def get_students(cls):
            return session.query(cls).filter(cls.scholarship == True).all()

        @classmethod
        def get_students_above_average_score(cls, score_threshold):
            return session.query(cls).filter(cls.average_score > score_threshold).all()

    class Receive(Base):
        __tablename__ = 'receiving_books'

        id = Column(Integer, primary_key=True)
        book_id = Column(Integer, nullable=False)
        student_id = Column(Integer, nullable=False)
        date_of_issue = Column(Date, nullable=False)
        date_of_return = Column(Date)

        @hybrid_property
        def count_date_with_book(self):
            count_of_days = self.date_of_return - self.date_of_issue
            return count_of_days

        def __repr__(self):
            return f"{self.id}, {self.book_id}, {self.student_id}, {self.date_of_issue}, {self.date_of_return}"

    Base.metadata.create_all(bind=engine)

    receive1 = Receive(
        book_id=2,
        student_id=1,
        date_of_issue=date(2025, 2, 1),
        date_of_return=date(2025, 2, 6)

    )

    receive2 = Receive(
        book_id=1,
        student_id=3,
        date_of_issue=date(2025, 2, 1),
        date_of_return=date(2025, 2, 18)

    )

    receive3 = Receive(
        book_id=3,
        student_id=2,
        date_of_issue=date(2025, 2, 1),
        date_of_return=date(2025, 2, 3)

    )

    students1 = Students(
        name='Ivan',
        surname='Ivanov',
        phone='123-456-78',
        email='ivanivan@qwerty.com',
        average_score=7.9,
        scholarship=False

    )

    students2 = Students(
        name='Masha',
        surname='Mashkova',
        phone='123-456-78',
        email='mashamasha@qwerty.com',
        average_score=9.2,
        scholarship=True

    )

    students3 = Students(
        name='Nikita',
        surname='Nikitin',
        phone='123-456-78',
        email='niknik@qwerty.com',
        average_score=7.2,
        scholarship=False

    )

    book1 = Books(
        name='Peace and War',
        count=5,
        release_date=date(2003, 4, 13),
        author_id=1
    )

    book2 = Books(
        name='The green mile',
        count=10,
        release_date=date(2007, 8, 11),
        author_id=2
    )

    book3 = Books(
        name='Puzzles',
        count=8,
        release_date=date(2003, 9, 1),
        author_id=3
    )

    session.add_all([receive1, receive2, receive3])
    session.commit()

    session.add_all([students1, students2, students3])
    session.commit()

    session.add_all([book1, book2, book3])
    session.commit()

    print(receive1.count_date_with_book)
    print(Students.get_students())
    print(Students.get_students_above_average_score(9.0))

