class Book:
    def __init__(self, **kwargs):
        self.isbn = kwargs.get('isbn')
        self.title = kwargs.get('title')
        self.subTitle = kwargs.get('subTitle')
        self.author = kwargs.get('author')
        self.pages = kwargs.get('pages')
        self.description = kwargs.get('description')


class DemoQaUser:
    def __init__(self, **kwargs):
        self.name = kwargs.get('username')
        self.user_id = kwargs.get('userId')
        self.password = kwargs.get('password')
        self.books = [Book(**b) for b in kwargs.get('books', [])]

    def __str__(self):
        return f'{self.name} ({self.user_id})'


class ErrorResponseAccount:
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        return f'{self.code}: {self.message}'

    def __eq__(self, other):
        return self.code == other.code and self.message == other.message