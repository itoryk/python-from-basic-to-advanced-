import json
import multiprocessing
import time
from multiprocessing.pool import ThreadPool

import requests

import logging

logging.basicConfig(level=logging.DEBUG)


class BookClient:
    URL: str = 'http://127.0.0.1:5000/api/books'
    TIMEOUT: int = 5

    def __init__(self):
        self.session = requests.Session()

    def get_all_books(self) -> dict:
        response = self.session.get(self.URL, timeout=self.TIMEOUT)
        return response.json()

    def add_new_book(self, data: dict):
        response = self.session.post(self.URL, json=data, timeout=self.TIMEOUT)
        if response.status_code == 201:
            return response.json()
        else:
            raise ValueError('Wrong params. Response message: {}'.format(response.json()))

    def delete_book_by_id(self, book_id: int):
        response = self.session.delete(self.URL + f'/{book_id}', timeout=self.TIMEOUT)
        return response.json()

    def get_book_by_id(self, book_id: int):
        response = self.session.get(self.URL + f'/{book_id}', timeout=self.TIMEOUT)
        return response.json()

    def patch_book_by_id(self, book_id: int, data: dict):
        response = self.session.patch(self.URL + f'/{book_id}', json=data, timeout=self.TIMEOUT)
        return response.json()

    def put_book_by_id(self, book_id: int, data: dict):
        response = self.session.put(self.URL + f'/{book_id}', json=data, timeout=self.TIMEOUT)
        return response.json()


class AuthorClient:
    URL: str = 'http://127.0.0.1:5000/api/authors'
    TIMEOUT: int = 5

    def __init__(self):
        self.session = requests.Session()

    def get_all_authors(self) -> dict:
        response = self.session.get(self.URL, timeout=self.TIMEOUT)
        return response.json()

    def add_new_author(self, data: dict):
        response = self.session.post(self.URL, json=data, timeout=self.TIMEOUT)
        if response.status_code == 201:
            return response.json()
        else:
            raise ValueError('Wrong params. Response message: {}'.format(response.json()))

    def get_all_books_by_author_id(self, author_id: int):
        response = self.session.get(self.URL + f'/{author_id}', timeout=self.TIMEOUT)
        return response.json()

    def delete_author_by_id(self, author_id: int):
        response = self.session.get(self.URL + f'/{author_id}', timeout=self.TIMEOUT)
        return response.status_code


execution_time_list = []


def start_end_timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        execution_time = time.time() - start
        execution_time_list.append(execution_time)
        return result
    return wrapper


def get_links(number, book_id):
    urls = []
    for i in range(number):
        urls.append(client.URL + f'/{book_id}')
    return urls


@start_end_timer
def many_requests_by_method(number):
    for i in range(number):
        # client.get_all_authors()
        client.session.get(client.URL)


@start_end_timer
def many_requests_by_threadpool(number):
    pool = ThreadPool(processes=multiprocessing.cpu_count())

    # pool.map(client.get_book_by_id, [1] * number)
    pool.map(client.session.get, get_links(number, book_id=1))

    pool.close()
    pool.join()


if __name__ == '__main__':
    client = BookClient()
    # client = AuthorClient()
    # many_requests_by_method(10)
    # many_requests_by_method(100)
    # many_requests_by_method(1000)
    many_requests_by_threadpool(10)
    many_requests_by_threadpool(100)
    many_requests_by_threadpool(1000)
    print('10: ', execution_time_list[0])
    print('100: ', execution_time_list[1])
    print('1000: ', execution_time_list[2])