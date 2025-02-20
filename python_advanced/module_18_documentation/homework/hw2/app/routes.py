from apispec_webframeworks.flask import FlaskPlugin
from apispec.ext.marshmallow import MarshmallowPlugin
from flask import Flask, request
from flask_restful import Api, Resource
from flasgger import APISpec, Swagger, swag_from
from marshmallow import ValidationError
from werkzeug.serving import WSGIRequestHandler

from models import (
    DATA,
    DATA_AUTHORS,
    get_all_books,
    get_book_by_id,
    get_all_authors,
    init_db,
    add_book,
    add_authors,
    update_book_by_id,
    delete_author_by_id,
    get_book_by_author,
)
from schemas import BookSchema, AuthorSchema

app = Flask(__name__)
api = Api(app)


spec = APISpec(
    title='BookList',
    version='1.0.0',
    openapi_version='2.0',
    plugins=[
        FlaskPlugin(),
        MarshmallowPlugin(),
    ],
)


class Books(Resource):
    def get(self, book_id):
        schema = BookSchema()
        return schema.dump(get_book_by_id(book_id)), 200


class Authors(Resource):
    def delete(self, author_id):
        schema = AuthorSchema()
        return schema.dump(delete_author_by_id(author_id)), 200

    def get(self, author_id):
        schema = BookSchema()
        return schema.dump(get_book_by_author(author_id), many=True), 200


class BooksEdit(Resource):

    def get(self, book_id):
        schema = BooksEdit()
        return schema.dump(get_book_by_id(book_id)), 200

    def put(self, book_id):
        data = request.json
        book = DATA(title=data['title'], author=data['author'], id=book_id)
        return update_book_by_id(book), 200

    def delete(self, book_id):
        schema = BooksEdit()
        return schema.dump(get_book_by_id(book_id)), 200


class BookList(Resource):

    # @swag_from("spec/books_get.yml")
    def get(self) -> tuple[list[dict], int]:

        schema = BookSchema()
        return schema.dump(get_all_books(), many=True), 200

    # @swag_from("spec/books_post.yml")
    def post(self) -> tuple[dict, int]:

        data = request.json
        schema = BookSchema()
        try:
            book = schema.load(data)
        except ValidationError as exc:
            return exc.messages, 400

        book = add_book(book)
        return schema.dump(book), 201


class AuthorList(Resource):
    def get(self):
        schema = AuthorSchema()
        return schema.dump(get_all_authors(), many=True), 200

    def post(self):
        data = request.json
        schema = AuthorSchema()
        try:
            author = schema.load(data)
        except ValidationError as exc:
            return exc.messages, 400
        author = add_authors(author)
        return schema.dump(author), 201


Swagger(app, template_file='spec/swagger.json')
# Swagger(app, template_file='../swagger.yaml')

api.add_resource(BookList, '/api/books')
api.add_resource(AuthorList, '/api/authors')
api.add_resource(Books, '/api/books/<int:book_id>')
api.add_resource(Authors, '/api/authors/<int:author_id>')


if __name__ == '__main__':
    init_db(initial_records=DATA, initial_records_authors=DATA_AUTHORS)
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(debug=True)
