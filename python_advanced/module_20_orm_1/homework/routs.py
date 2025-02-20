
from datetime import datetime, timedelta, date
from sqlalchemy import Table, MetaData, create_engine, Column, Integer, String, Date, Float, Boolean, update
from sqlalchemy.orm import sessionmaker, mapper, declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from flask import Flask, jsonify, request

engine = create_engine("sqlite:///python.db")
Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)

Base = declarative_base()


class Books(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
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


@app.route('/books', methods=['GET'])
def get_all_books():
    books = session.query(Books).all()
    books_list = []
    for book in books:
        books_list.append({
            'id': book.id,
            'name': book.name,
            'count': book.count,
            'release_date': book.release_date.strftime('%Y-%m-%d'),
            'author_id': book.author_id
        })
    return jsonify(books_list)


@app.route('/debtors', methods=['GET'])
def get_debtors():
    current_date = datetime.now().date()
    deadline_date = current_date - timedelta(days=14)

    debtors = session.query(Receive, Students).join(
        Students, Receive.student_id == Students.id
    ).filter(
        (Receive.date_of_return.is_(None) & (Receive.date_of_issue <= deadline_date)) |
        (Receive.date_of_return > Receive.date_of_issue + timedelta(days=14))).all()

    debtors_list = []
    for receive, student in debtors:
        debtors_list.append({

            'student_id': student.id,
            'student_name': student.name,
            'student_surname': student.surname,
            'book_id': receive.book_id,
            'date_of_issue': receive.date_of_issue.strftime('%Y-%m-%d'),
            'date_of_return': receive.date_of_return.strftime('%Y-%m-%d') if receive.date_of_return else None,
            'days_overdue': (current_date - receive.date_of_issue).days - 14
        })

    return jsonify(debtors_list)


@app.route('/take_book', methods=['POST'])
def take_book():
    data = request.json
    book_id = data.get('book_id')
    student_id = data.get('student_id')

    if not book_id or not student_id:
        return jsonify({"error": "book_id and student_id are required"}), 400

    book = session.query(Books).filter(Books.id == book_id).first()
    student = session.query(Students).filter(Students.id == student_id).first()

    if not book:
        return jsonify({"error": "Book not found"}), 404

    if not student:
        return jsonify({"error": "Student not found"}), 404

    if book.count <= 0:
        return jsonify({"error": "Book is not available"}), 400

    book.count -= 1

    new_receive_entry = Receive(
        book_id=book_id,
        student_id=student_id,
        date_of_issue=datetime.now().date(),
        date_of_return=None
    )

    session.add(new_receive_entry)
    session.commit()

    return jsonify({
        'message': 'book issued successfully',
        'receive_entry': {
            'id': new_receive_entry.id,
            'book_id': new_receive_entry.book_id,
            'student_id': new_receive_entry.student_id,
            'date_of_issue': new_receive_entry.date_of_issue.strftime('%Y-%m-%d'),
            'date_of_return': None
        }
    }), 201


@app.route('/return_book', methods=['POST'])
def return_book():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    book_id = data.get('book_id')
    student_id = data.get('student_id')

    if not book_id or not student_id:
        return jsonify({"error": "book_id and student_id are required"}), 400

    receive_entry = session.query(Receive).filter(
        Receive.book_id == book_id,
        Receive.student_id == student_id,
        Receive.date_of_return.is_(None)
    ).first()

    if not receive_entry:
        return jsonify({"error": "No active book issue found for this student and book"}), 404

    receive_entry.date_of_return_datetime = datetime.now().date()

    book = session.query(Books).filter(Books.id == book_id).first()
    if book:
        book.count += 1

    session.commit()

    return jsonify({
        "message": "Book returned successfully",
        "receive_entry": {
            "id": receive_entry.id,
            "book_id": receive_entry.book_id,
            "student_id": receive_entry.student_id,
            "date_of_issue_datetime": receive_entry.date_of_issue.strftime('%Y-%m-%d'),
            "date_of_return_datetime": None
        }
    }), 200


if __name__ == '__main__':
   app.run(debug=True)